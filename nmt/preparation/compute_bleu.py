# Compute BLEU with arguments
# Example Command: python3 compute_bleu.py [test_file_name] [mt_file_name]

import sys
import sacrebleu
import pyonmttok

tokenizer = pyonmttok.Tokenizer("char",
                                no_substitution=False,
                                with_separators=False,
                                case_feature=False)

target_test = sys.argv[1]  # Test file argument
target_pred = sys.argv[2]  # MTed file argument

refs = []

with open(target_test) as test:
    for line in test:
        line = line.strip().split()
        line = tokenizer.detokenize(line)
        refs.append(line)

print("Reference 1st sentence:", refs[0])

refs = [refs]  # It is a list of list(s) as required by sacreBLEU

# Open the translation file by the NMT model and detokenize the predictions
preds = []

with open(target_pred) as pred:
    for line in pred:
        line = line.strip().split()
        line = tokenizer.detokenize(line)
        preds.append(line)

print("MTed 1st sentence:", preds[0])

# Calculate and print the BLEU score
bleu = sacrebleu.corpus_bleu(preds, refs)
print("BLEU: ", bleu.score)

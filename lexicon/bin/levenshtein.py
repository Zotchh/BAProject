#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import unicodedata
import Levenshtein
from numpy import unicode


# Normalize token by replacing special char with default char
def normalize(token):
    norm_input = unicodedata.normalize('NFD', token)

    smooth_breathing = unicode(u"\N{COMBINING COMMA ABOVE}")
    rough_breathing = unicode(u"\N{COMBINING REVERSED COMMA ABOVE}")
    circumflex = unicode(u"\N{COMBINING GREEK PERISPOMENI}")
    acute_accent = unicode(u"\N{COMBINING ACUTE ACCENT}")
    grave_accent = unicode(u"\N{COMBINING GRAVE ACCENT}")
    iota_subscript = unicode(u"\N{COMBINING GREEK YPOGEGRAMMENI}")
    in_table = u'' + smooth_breathing + rough_breathing + circumflex + acute_accent + grave_accent + iota_subscript

    smooth_breathing_replacement = u'\u21b2'  # u')'
    rough_breathing_replacement = u'\u21b1'  # u'('
    circumflex_replacement = u'\u2194'  # u'~'
    acute_accent_replacement = u'\u2197'  # u'/'
    grave_accent_replacement = u'\u2196'  # u'\\'
    iota_subscript_replacement = u'\u2193'  # u'|'
    out_table = u'' + smooth_breathing_replacement + rough_breathing_replacement + circumflex_replacement + acute_accent_replacement + grave_accent_replacement + iota_subscript_replacement

    translation_table = dict((ord(a), b) for a, b in zip(in_table, out_table))
    return norm_input.translate(translation_table)


# Compute Levenshtein edit distance between 2 words
def levenshtein_distance(keyword, word):
    keyword_norm = normalize(keyword)
    word_norm = normalize(word)

    lev = Levenshtein.distance(keyword_norm, word_norm)

    return lev


def main():
    print(levenshtein_distance(sys.argv[1].decode('utf-8'), sys.argv[2].decode('utf-8')))


if __name__ == "__main__":
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/13 18:12
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : visualiser_28453093.py.py
# @Software: PyCharm
# @LastModi: 2018/05/27 18:21
# @Instructions : This file contains a class AnalysisVisualiser. This class is mainly for drawing figure and
#                 show them for users.

import matplotlib.pyplot as plt


class AnalysisVisualiser:

    def __init__(self, all_text_stats):
        self.visualise_df = all_text_stats

    # Figure for character frequency.
    def visualise_character_frequency(self, corpus_name):
        self.visualise_df.plot(kind='bar')
        plt.title(corpus_name)
        plt.xlabel("Characters")
        plt.ylabel("Frequency")
        plt.legend(loc="upper right")
        plt.show()

    # Figure for punctuation frequency.
    def visualise_punctuation_frequency(self, corpus_name):
        self.visualise_df.plot(kind='bar')
        plt.title(corpus_name)
        plt.xlabel("Punctuations")
        plt.ylabel("Frequency")
        plt.legend(loc="upper right")
        plt.show()

    # Figure for stop word frequency.
    def visualise_stopword_frequency(self, corpus_name):
        self.visualise_df.plot(kind='bar')
        plt.title(corpus_name)
        plt.xlabel("Stopwords")
        plt.ylabel("Frequency")
        plt.legend(loc="upper right")
        plt.show()

    # Figure for word length frequency.
    def visualise_word_length_frequency(self, corpus_name):
        self.visualise_df.plot(kind='bar')
        plt.title(corpus_name)
        plt.xlabel("Word length")
        plt.ylabel("Frequency")
        plt.legend(loc="upper right")
        plt.show()

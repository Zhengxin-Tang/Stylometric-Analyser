#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/13 16:39
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : word_28453093.py.py
# @Software: PyCharm
# @LastModi: 2018/05/27 18:21
# @Instructions : This file contains a class WordAnalyser. This class analyse words from many aspects. It counts
#                 the occurrences of different words, stop words and word length.

import numpy as np
import pandas as pd


class WordAnalyser:

    def __init__(self):
        self.word_df = pd.DataFrame(columns=["Occurrence"])
        self.word_list = []
        self.word_total_number = 0

    # Present the occurrences of different words.
    def __str__(self):
        return self.word_df.to_string()

    # Count the occurrences of different words.
    def analyse_words(self, tokenised_list):
        self.word_list = []
        for word in tokenised_list:
            if word.isalpha():
                # Count the total number of words.
                self.word_total_number += 1
                if word.lower() not in self.word_list:
                    self.word_list.append(word.lower())
                    temp_df = pd.DataFrame(1, index=[word.lower()], columns=["Occurrence"])
                    self.word_df = self.word_df.append(temp_df, ignore_index=False)
                elif word.lower() in self.word_list:
                    self.word_df.loc[word.lower(), "Occurrence"] += 1

    # Count the occurrences of all stop words.
    def get_stopword_frequency(self):
        # Get the stop word list from the file stopword_list.txt.
        stopword_list = []
        input_handle = open('stopword_list.txt','r')
        for word in input_handle.readlines():
            if word != '\n' and len(word.strip("\n")) != 1:
                stopword_list.append(word.strip("\n"))
        # This list save the stop words that appear in the given text.
        stopword_occurrence_list = []
        # This list save the occurrences of the relative stop words.
        stopword_frequency_list = []
        for word in self.word_list:
            if word in stopword_list:
                stopword_occurrence_list.append(word)
                stopword_frequency_list.append(self.word_df.loc[word, "Occurrence"])
        # Create a dataframe to store stop word frequency.
        stopword_frequency_df = pd.DataFrame(stopword_frequency_list, index=stopword_occurrence_list,
                                             columns=["Occurrence"])
        return stopword_frequency_df

    # Count the occurrences for different word length.
    def get_word_length_frequency(self):
        # Get the maximum word length first.
        max_length = 0
        for word in self.word_list:
            if len(word) > max_length:
                max_length = len(word)
        word_length_frequency_list = np.zeros(max_length, dtype=int)
        for i in range(1, max_length + 1):
            for word in self.word_list:
                if len(word) == i:
                    word_length_frequency_list[i - 1] += self.word_df.loc[word, "Occurrence"]
        # Create a dataframe to store word length data.
        word_length_frequency_df = pd.DataFrame(word_length_frequency_list, index=np.arange(1, max_length + 1),
                                                columns=["Occurrence"])
        return word_length_frequency_df

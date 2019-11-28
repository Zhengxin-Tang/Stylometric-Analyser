#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 16:52
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : character_28453093.py.py
# @Software: PyCharm
# @LastModi: 2018/05/27 18:21
# @Instructions : This file contains a class CharacterAnalyser. This class is used for analysing characters from
#                 the given token list, including saving occurrences of each characters and punctuations into instance
#                 character_df and total number of characters in the given token list.

import numpy as np
import pandas as pd


class CharacterAnalyser:

    def __init__(self):
        self.alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.!?;:'()[]-\"")
        self.character_df = pd.DataFrame(np.zeros([49, 1], dtype=int), index=self.alphabet, columns=["Occurrence"])
        self.character_total_number = 0

    # Present the occurrences of different characters and punctuations.
    def __str__(self):
        return self.character_df.to_string()

    # Count the occurrences of different characters and punctuations into character_df.
    def analyse_characters(self, tokenised_list):
        for item in tokenised_list:
            for character in item:
                # Count the total number of characters.
                self.character_total_number += 1
                if character.upper() in self.alphabet:
                    self.character_df.loc[character.upper(), "Occurrence"] += 1

    # Return a dataframe that includes occurrences of different punctuations
    def get_punctuation_frequency(self):
        return self.character_df[',':'\"']

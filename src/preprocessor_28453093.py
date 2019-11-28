#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 16:42
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : preprocessor_28453093.py.py
# @Software: PyCharm
# @LastModi: 2018/05/27 18:21
# @Instructions : This file contains a class Preprocessor. This class have one instance and is used to split an
#                 input text into individual tokens, then save them in the instance.


class Preprocessor:

    def __init__(self):
        self.token_list = []

    # Present the total number of tokens.
    def __str__(self):
        temp_str = str(len(self.token_list)) + "tokens in the list."
        return temp_str

    # Split input text into individual words and punctuations.
    def tokenise(self, input_sequence):
        self.token_list += input_sequence.split(" ")

    def get_tokenised_list(self):
        return self.token_list

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/13 18:20
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : main_28453093.py.py
# @Software: PyCharm
# @LastModi: 2018/05/27 18:21
# @Instructions : This file contains the main function, which drives the flow of execution of the program. It has
#                 two menus: Stylometry Analysis Main Menu is for choosing different corpus to analyse or compare
#                 two corpuses, or analyse all corpuses together; Frequency Analysis Menu  is a child menu and can
#                 lead users to analyse for different frequencies, and them show the figures.

import preprocessor_28453093
import character_28453093
import word_28453093
import visualiser_28453093
import pandas as pd


def main():
    file_list = ["Edward_II_Marlowe.tok", "Edward_II_Marlowe.tok", "Henry_VI_Part1_Shakespeare.tok",
                 "Henry_VI_Part2_Shakespeare.tok", "Jew_of_Malta_Marlowe.tok", "Richard_II_Shakespeare.tok"]
    while True:
        # The main menu.
        print("-----------Stylometry Analysis Main Menu----------- ")
        action = input("Please select the corpus for analysis:\n"
                       "[1]Edward_II_Marlowe\n"
                       "[2]Hamlet_Shakespeare\n"
                       "[3]Henry_VI_Part1_Shakespeare\n"
                       "[4]Henry_VI_Part2_Shakespeare\n"
                       "[5]Jew_of_Malta_Marlowe\n"
                       "[6]Richard_II_Shakespeare\n"
                       "[7]Analyse and compare two corpus\n"
                       "[8]Analyse all together\n"
                       "[9]Quit\n")
        if action not in "123456789" or len(action) != 1:
            print("Invalid input. Please input a number from 1-8.")
        elif action == "1":
            analysis_one("Edward_II_Marlowe.tok")
        elif action == "2":
            analysis_one("Hamlet_Shakespeare.tok")
        elif action == "3":
            analysis_one("Henry_VI_Part1_Shakespeare.tok")
        elif action == "4":
            analysis_one("Henry_VI_Part2_Shakespeare.tok")
        elif action == "5":
            analysis_one("Jew_of_Malta_Marlowe.tok")
        elif action == "6":
            analysis_one("Richard_II_Shakespeare.tok")
        # Compare two corpuses.
        elif action == "7":
            corpus1 = input("Please input the first corpus(from 1-6)")
            corpus2 = input("Please input the second corpus(from 1-6)")
            if corpus1 in "123456" and corpus2 in "123456" \
                    and len(corpus1) == 1 and len(corpus2) == 1 and corpus1 != corpus2:
                file_list_compare = [file_list[int(corpus1)-1], file_list[int(corpus2)-1]]
                analysis_more(file_list_compare)
            else:
                print("Invalid input. Please input two different number from 1-6.")
        # Analyse all corpuses.
        elif action == "8":
            analysis_more(file_list)
        elif action == "9":
            print("Quit main menu.")
            break


# Function of reading in texts.
def read_input(corpus_name):
    try:
        input_handle = open(corpus_name, 'r')
        temp_input_list = []
        for line in input_handle.readlines():
            temp_input_list.append(line.strip("\n"))
        return temp_input_list
    except IOError:
        print("Error: cannot access the file!")


# Function for analysing one corpus.
def analysis_one(corpus_name):
    list_for_tokenise = read_input(corpus_name)
    preprocessor = preprocessor_28453093.Preprocessor()
    character_analyser = character_28453093.CharacterAnalyser()
    word_analyser = word_28453093.WordAnalyser()
    for line in list_for_tokenise:
        preprocessor.tokenise(line)
    # Present the total number of tokens.
    print(preprocessor)
    print("Analysing...this may cost some time...")
    character_analyser.analyse_characters(preprocessor.get_tokenised_list())
    word_analyser.analyse_words(preprocessor.get_tokenised_list())
    print("Analyse successfully.")
    while True:
        # The frequency analysis menu.
        print("-----------Frequency Analysis Menu(for one corpus)----------- ")
        action = input("Visualising from which aspect?\n"
                       "[1]Character frequency\n"
                       "[2]Punctuation frequency\n"
                       "[3]Stopword frequency\n"
                       "[4]Word length frequency\n"
                       "[5]Show all words in console\n"
                       "[6]Quit\n")
        if action not in "123456" or len(action) != 1:
            print("Invalid input. Please input a number from 1-6.")
        elif action == "1":
            # Create a temp dataframe to calculate the percentage.
            temp_frequency_df = character_analyser.character_df.copy()
            for index in temp_frequency_df.index:
                temp_frequency_df.loc[index, "Occurrence"] = temp_frequency_df.loc[index, "Occurrence"] / character_analyser.character_total_number
            temp_frequency_df.columns = ["Character frequency"]
            # Present the occurrences of different characters and punctuations.
            print(character_analyser)
            # Use AnalysisVisualiser to show figure.
            visualiser_character = visualiser_28453093.AnalysisVisualiser(temp_frequency_df)
            visualiser_character.visualise_character_frequency(corpus_name)
        elif action == "2":
            temp_frequency_df = character_analyser.get_punctuation_frequency().copy()
            for index in temp_frequency_df.index:
                temp_frequency_df.loc[index, "Occurrence"] = temp_frequency_df.loc[index, "Occurrence"] / character_analyser.character_total_number
            temp_frequency_df.columns = ["Punctuation frequency"]
            visualiser_punctuation = visualiser_28453093.AnalysisVisualiser(temp_frequency_df)
            visualiser_punctuation.visualise_punctuation_frequency(corpus_name)
        elif action == "3":
            temp_frequency_df = word_analyser.get_stopword_frequency().copy()
            for index in temp_frequency_df.index:
                temp_frequency_df.loc[index, "Occurrence"] = temp_frequency_df.loc[index, "Occurrence"] / word_analyser.word_total_number
            temp_frequency_df.columns = ["Stopword frequency"]
            visualiser_stopword = visualiser_28453093.AnalysisVisualiser(temp_frequency_df)
            visualiser_stopword.visualise_stopword_frequency(corpus_name)
        elif action == "4":
            temp_frequency_df = word_analyser.get_word_length_frequency().copy()
            for index in temp_frequency_df.index:
                temp_frequency_df.loc[index, "Occurrence"] = temp_frequency_df.loc[index, "Occurrence"] / word_analyser.word_total_number
            temp_frequency_df.columns = ["Word length frequency"]
            visualiser_word_length = visualiser_28453093.AnalysisVisualiser(temp_frequency_df)
            visualiser_word_length.visualise_word_length_frequency(corpus_name)
        elif action == "5":
            # Present the occurrences of different words.
            print(word_analyser)
        elif action == "6":
            print("Quit visualising menu.")
            break


# Function for analysing two or all corpuses.
def analysis_more(file_list):
    while True:
        print("-----------Frequency Analysis Menu(for two or all corpuses)----------- ")
        action = input("Visualising from which aspect?\n"
                       "[1]Character frequency\n"
                       "[2]Punctuation frequency\n"
                       "[3]Stopword frequency\n"
                       "[4]Word length frequency\n"
                       "[5]Quit\n")
        if action not in "12345" or len(action) != 1:
            print("Invalid input. Please input a number from 1-5.")
        elif action == "1":
            print("Analysing...this may cost some time...")
            df_list = []
            # Read in file from the file list, and create preprocessor, character_analyser or word_analyser for
            # each analyses.
            for file in file_list:
                list_for_tokenise = read_input(file)
                preprocessor = preprocessor_28453093.Preprocessor()
                character_analyser = character_28453093.CharacterAnalyser()
                for line in list_for_tokenise:
                    preprocessor.tokenise(line)
                character_analyser.analyse_characters(preprocessor.get_tokenised_list())
                # Create a temp dataframe to calculate the percentage.
                temp_frequency_df = character_analyser.character_df.copy()
                for index in temp_frequency_df.index:
                    temp_frequency_df.loc[index, "Occurrence"] = temp_frequency_df.loc[index, "Occurrence"] / character_analyser.character_total_number
                temp_frequency_df.columns = [file]
                # Add each temp dataframe to df_list.
                df_list.append(temp_frequency_df)
            # Combine all dataframes together in the df_list.
            character_all_df = pd.concat(df_list, axis=1)
            print("Analyse successfully.")
            # Use AnalysisVisualiser to show figure.
            visualiser_character = visualiser_28453093.AnalysisVisualiser(character_all_df)
            visualiser_character.visualise_character_frequency("Character frequency of corpuses")
        elif action == "2":
            print("Analysing...this may cost some time...")
            df_list = []
            for file in file_list:
                list_for_tokenise = read_input(file)
                preprocessor = preprocessor_28453093.Preprocessor()
                character_analyser = character_28453093.CharacterAnalyser()
                for line in list_for_tokenise:
                    preprocessor.tokenise(line)
                character_analyser.analyse_characters(preprocessor.get_tokenised_list())
                temp_frequency_df = character_analyser.get_punctuation_frequency().copy()
                for index in temp_frequency_df.index:
                    temp_frequency_df.loc[index, "Occurrence"] = temp_frequency_df.loc[index, "Occurrence"] / character_analyser.character_total_number
                temp_frequency_df.columns = [file]
                df_list.append(temp_frequency_df)
            punctuation_all_df = pd.concat(df_list, axis=1)
            print("Analyse successfully.")
            visualiser_punctuation = visualiser_28453093.AnalysisVisualiser(punctuation_all_df)
            visualiser_punctuation.visualise_punctuation_frequency("Punctuation frequency of corpuses")
        elif action == "3":
            print("Analysing...this may cost some time...")
            df_list = []
            for file in file_list:
                list_for_tokenise = read_input(file)
                preprocessor = preprocessor_28453093.Preprocessor()
                word_analyser = word_28453093.WordAnalyser()
                for line in list_for_tokenise:
                    preprocessor.tokenise(line)
                word_analyser.analyse_words(preprocessor.get_tokenised_list())
                temp_frequency_df = word_analyser.get_stopword_frequency().copy()
                for index in temp_frequency_df.index:
                    temp_frequency_df.loc[index, "Occurrence"] = temp_frequency_df.loc[index, "Occurrence"] / word_analyser.word_total_number
                temp_frequency_df.columns = [file]
                df_list.append(temp_frequency_df)
            stopword_all_df = pd.concat(df_list, axis=1)
            print("Analyse successfully.")
            visualiser_stopword = visualiser_28453093.AnalysisVisualiser(stopword_all_df)
            visualiser_stopword.visualise_stopword_frequency("Stopword frequency of corpuses")
        elif action == "4":
            print("Analysing...this may cost some time...")
            df_list = []
            for file in file_list:
                list_for_tokenise = read_input(file)
                preprocessor = preprocessor_28453093.Preprocessor()
                word_analyser = word_28453093.WordAnalyser()
                for line in list_for_tokenise:
                    preprocessor.tokenise(line)
                word_analyser.analyse_words(preprocessor.get_tokenised_list())
                temp_frequency_df = word_analyser.get_word_length_frequency().copy()
                for index in temp_frequency_df.index:
                    temp_frequency_df.loc[index, "Occurrence"] = temp_frequency_df.loc[index, "Occurrence"] / word_analyser.word_total_number
                temp_frequency_df.columns = [file]
                df_list.append(temp_frequency_df)
            word_length_all_df = pd.concat(df_list, axis=1)
            print("Analyse successfully.")
            visualiser_word_length = visualiser_28453093.AnalysisVisualiser(word_length_all_df)
            visualiser_word_length.visualise_word_length_frequency("Word length frequency of corpuses")
        elif action == "5":
            print("Quit visualising menu.")
            break


if __name__ == '__main__':
    main()

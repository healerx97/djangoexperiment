#!/usr/bin/env python
# coding: utf-8



import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from collections import Counter
import collections
import re
from nltk.tokenize import word_tokenize
import json
import sys
import spacy






'''
the program finds keywords in reviews 

input:
    software: the name of a software or a sub-category
    number_words: the number of words, eg, 'expensive' contains 1 word, 'Battery life' contains 2 words
    number_keywords: the number of keywords to output 
    software_type: 'software' or 'category', this argument indicating whether the entered value for software is a software.name or category.name
    
output:
     a text file in JSON array format (called competitor.txt)

usage:
    python ProsCons_keywords.py software, number_words, number_keywords,  software_type 
    


'''
rp = 'review_base.csv'
sd = 'result_base.csv'
#download stopwords
#nltk.download('stopwords')
#nltk.download('punkt')
class ProsCons:
    def __init__(self, reviews_path, result_path):
        self.reviews = pd.read_csv(reviews_path, low_memory=False)
        self.software_data = pd.read_csv(result_path, low_memory=False)

        en = spacy.load('en_core_web_sm')
        self.sw_spacy = en.Defaults.stop_words
        self.sw_spacy.add('like')
        self.sw_spacy.add('thing')
        self.sw_spacy.add('things')
        self.sw_spacy.add('need')

    #reviews = pd.read_csv('data/base_data/review_base.csv', low_memory=False)
    #software_data = pd.read_csv('data/base_data/result_base.csv', low_memory=False )

    # reviews = pd.read_csv(r'review_base.csv', low_memory=False)
    # software_data = pd.read_csv(r'result_base.csv', low_memory=False)

    def listToString(self, s): 
        
        # initialize an empty string
        str1 = " " 
        
        # return string  
        return (str1.join(s))

    def pro_keyword(self, software):
        softwares_df = self.reviews.loc[self.reviews['software.name'] == software]
        #print(len(softwares_df))
        filtered_sentence = []
        for i in softwares_df['pros'].index:
            stop_words = set(stopwords.words('english'))
            if str(softwares_df['pros'][i] ) != 'nan':
                cleaned_list = re.split(r"[^A-Za-z]", softwares_df['pros'][i].strip())
                cleaned_list = [x for x in cleaned_list if x != '' and x != 'Pros']
                word_tokens = word_tokenize(self.listToString(cleaned_list))
                for w in word_tokens:
                    if (w.lower() not in stop_words) and (w.lower() not in self.sw_spacy):
                        filtered_sentence.append(w)
        occurrences = collections.Counter(filtered_sentence)
        return filtered_sentence, occurrences


    def con_keyword(self, software):
        softwares_df = self.reviews.loc[self.reviews['software.name'] == software]
        filtered_sentence = []
    
        for i in softwares_df['cons'].index:
            stop_words = set(stopwords.words('english'))
            if str(softwares_df['cons'][i] ) != 'nan':
                cleaned_list = re.split(r"[^A-Za-z]", softwares_df['cons'][i].strip())
                cleaned_list = [x for x in cleaned_list if x != '' and x != 'Cons']
                word_tokens = word_tokenize(self.listToString(cleaned_list))
                for w in word_tokens:
                    if (w.lower() not in stop_words) and (w.lower() not in self.sw_spacy):
                        filtered_sentence.append(w)
        occurrences = collections.Counter(filtered_sentence)
        return filtered_sentence, occurrences

    def create_ngrams(self, token_list, nb_elements):
        """
        Create n-grams for list of tokens
        Parameters
        ----------
        token_list : list
            list of strings
        nb_elements :
            number of elements in the n-gram
        Returns
        -------
        Generator
            generator of all n-grams
        """
        ngrams = zip(*[token_list[index_token:] for index_token in range(nb_elements)])
        return (" ".join(ngram) for ngram in ngrams)


    def frequent_words(self, list_words, ngrams_number, number_top_words):
        """
        Create n-grams for list of tokens
        Parameters
        ----------
        ngrams_number : int
        number_top_words : int
            output dataframe length
        Returns
        -------
        DataFrame
            Dataframe with the entities and their frequencies.
        """
        frequent = []
        if ngrams_number == 1:
            pass
        elif ngrams_number >= 2:
            list_words = self.create_ngrams(list_words, ngrams_number)
        else:
            raise ValueError("number of n-grams should be >= 1")
        

        counter = Counter(list_words)
        frequent = counter.most_common(number_top_words + 10)
        
        return frequent

    def process(self, data, number_keywords):
        
        empty_list = []
        result_list  = []
    
        if data != empty_list: 
            
            for i in range(len(data)):
                result_list.append(data[i][0])
        
        final_list = self.remove_duplicate(result_list,number_keywords)  
            
        return final_list

    def remove_duplicate(self, data,number_keywords):
        seen = set()
        unique_list = []
        for x in data:
            if x.lower() not in seen:
                unique_list.append(x)
                seen.add(x.lower())
        return unique_list[:number_keywords]
        
            
        

    def find_keywords(self, software, number_words, number_keywords):
        pros, occ = self.pro_keyword(software)
        cons, occ = self.con_keyword(software)
        
        
        pro_result = self.frequent_words(pros, ngrams_number= number_words, number_top_words= number_keywords )
        con_result = self.frequent_words(cons, ngrams_number= number_words, number_top_words= number_keywords )

        pro_cleaned = self.process(pro_result,number_keywords)
        con_cleaned = self.process(con_result,number_keywords)

        keyword_dic = {'pro': pro_cleaned, 'con': con_cleaned}
    
        result_dic = {software: keyword_dic}

        return result_dic


def main():
    
    proscons = ProsCons(rp, sd)

    result_list = []
    
    review_softwares_list = proscons.reviews['software.name'].unique()
    

    software, number_words, number_keywords, software_type = sys.argv[1], sys.argv[2], sys.argv[3],sys.argv[4]
    number_words, number_keywords= int(number_words), int(number_keywords)
    software, software_type  = str(software),str(software_type)
    #print(software)
    if software_type == 'software':
        result  = proscons.find_keywords(software, number_words, number_keywords)
        result_list.append(result)
    else:
        #find all softwares in the same category
        softwares_names_df = proscons.software_data.loc[proscons.software_data['Sub.cat1'] == software]
        softwares_names = softwares_names_df['software.name'].unique()
        for i in softwares_names:
            if i in review_softwares_list:
                result  = proscons.find_keywords(i, number_words, number_keywords)
                result_list.append(result)
  
    #with open('proscons_keywords.txt', 'w') as outfile:
        #json.dump(result_list , outfile)

    with open('proscons_keywords.json', 'w') as outfile:
        json.dump(result_list , outfile)

    
main()


 




#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 14:51:25 2023

@author: clemmie
"""

from collections import Counter

import pandas as pd
import sys
sys.path.append('/Users/clemmie/Desktop/Spyder')
import wordBank


the_big_scrape = "/Users/clemmie/Desktop/Spyder/theBigScrape.csv"

df = pd.read_csv(the_big_scrape)

#Checks if post has link and removes it
df['postText'] = df['postText'].str.replace(r'(http\S+)', '', regex=True)

#Checks if post has 'Click to expand...' and removes it
df['postText'] = df['postText'].str.replace(r'(Click to expand...)', '', regex=True)

#Check if post has punctuation and removes it
df['postText'] = df['postText'].str.replace(r'[^\w\s]+', '', regex=True)


# LEXICAL ANALYSIS  

df['words'] = df['postText'].fillna('').apply(lambda x: x.split())
# Group the DataFrame by user
groups = df.groupby('userName')


from empath import Empath


lexicon = Empath()
categories = lexicon.cats

    
CATEGORY_NAMES = {
 1: 'misogyny',
 2: 'flipping_the_narrative_injustice_victimhood_persecution',
 3: 'homophobia',
 4: 'violence',
 5: 'sexual_violence',
 6: 'racism_white_supremacy',
 7: 'high_divergence_incel_lexicon',
 8: 'martyrdom', 
 9: 'sex_sexuality', 
 10:'appearance'
}

#1 
df['misogyny_score'] = df['words'].apply(lambda x: lexicon.analyze(" ".join(x), categories=["misogyny"])["misogyny"])

#2 
df['flipping_the_narrative_injustice_victimhood_persecution_score'] = df['words'].apply(lambda x: lexicon.analyze(" ".join(x), categories=["flipping_the_narrative_injustice_victimhood_persecution"])["flipping_the_narrative_injustice_victimhood_persecution"])

#3
df['homophobia_score'] = df['words'].apply(lambda x: lexicon.analyze(" ".join(x), categories=["homophobia"])["homophobia"])

#4
df['violence_score'] = df['words'].apply(lambda x: lexicon.analyze(" ".join(x), categories=["violence"])["violence"])

#5
df['sexual_violence_score'] = df['words'].apply(lambda x: lexicon.analyze(" ".join(x), categories=["sexual_violence"])["sexual_violence"])

#6
df['racism_white_supremacy_score'] = df['words'].apply(lambda x: lexicon.analyze(" ".join(x), categories=["racism_white_supremacy"])["racism_white_supremacy"])

#7
df['high_divergence_incel_lexicon_score'] = df['words'].apply(lambda x: lexicon.analyze(" ".join(x), categories=["high_divergence_incel_lexicon"])["high_divergence_incel_lexicon"])

#8 
df['martyrdom_score'] = df['words'].apply(lambda x: lexicon.analyze(" ".join(x), categories=["martyrdom"])["martyrdom"])

#9 
df['sex_sexuality_score'] = df['words'].apply(lambda x: lexicon.analyze(" ".join(x), categories=["sex_sexuality"])["sex_sexuality"])

#10
df['appearance_score'] = df['words'].apply(lambda x: lexicon.analyze(" ".join(x), categories=["appearance"])["appearance"])



column_names = df.columns
print(column_names)
print(df['violence_score'].head())
print(df['postText'].head())



# Save the results to the same CSV file
df.to_csv(the_big_scrape, index=False)

df.to_csv('the_big_scrape_cool.csv', index=False)
    

#LOOK FOR SPECIFIC WORDS
# Loop over the groups and count the frequency of library words for each user
#for userName, group in groups: words = [word for post in group['words'] for word in post]
#word_freq = Counter(word for word in words if word in wordBank.library)
#print(f"UserName: {userName}")
#for word, freq in word_freq.items():
 #   print(f"{word}: {freq}")

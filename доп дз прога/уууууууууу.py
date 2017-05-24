import re
from math import log

punct = '[.,!«»?&@"$\[\]\(\):;%#&\'—-]'

def preprocessing(text):
    longwords=[]
    text_wo_punct = re.sub(punct, '', text.lower())
    words = text_wo_punct.strip().split()
    for word in words:
        if len(word)>=4:
            longwords.append(word)
    return longwords

import os
anek = ''
teh = ''
izvest = ''
for root, dirs, files in os.walk('texts'):
    for f in files:
        if 'anekdots' in root:
            num_anek = len(files)
            anek += open(os.path.join(root, f), encoding='utf-8').read()
        elif 'izvest' in root:
            num_izvest = len(files)
            izvest += open(os.path.join(root, f), encoding='utf-8').read()
        elif 'teh_mol' in root:
            num_teh = len(files)
            teh += open(os.path.join(root, f), encoding='utf-8').read()
            
words_anek = preprocessing(anek)
words_teh = preprocessing(teh)
words_izvest = preprocessing(izvest)

words = words_anek + words_teh + words_izvest

def bigram_dict(words):
    bigrams = []
    for ind in range(1, len(words) - 1):
        bigrams.append(' '.join([words[ind - 1], words[ind]]))
    
    bigram_freq = {}
    for b in bigrams:
        if b in bigram_freq:
            bigram_freq[b] += 1
        else:
            bigram_freq[b] = 1
    return bigram_freq

corpus_bfreq = bigram_dict(words)
anek_bfreq = bigram_dict(words_anek)
izvest_bfreq = bigram_dict(words_izvest)
teh_bfreq = bigram_dict(words_teh)

def pmi_for_cats(x, y):
    if y == 'anek':
        dic = anek_bfreq
        num = num_anek
    elif y == 'teh':
        dic = teh_bfreq
        num = num_teh
    elif y == 'izvest':
        dic = izvest_bfreq
        num = num_izvest
    p_xy = dic[x]/len(dic)
    p_x, p_y = corpus_bfreq[x]/len(corpus_bfreq), num/(num_izvest + num_teh + num_anek)
    pmi = log(p_xy/(p_x * p_y))
    return pmi


cat_pmi = {}
i = 0
for bigram in corpus_bfreq:
    if i > 100:
        break
    try:
        pmi_anek = pmi_for_cats(bigram, 'anek')
    except KeyError:
        pmi_anek = 0
    try:
        pmi_teh = pmi_for_cats(bigram, 'teh')
    except KeyError:
        pmi_teh = 0
    try:
        pmi_izvest = pmi_for_cats(bigram, 'izvest')
    except KeyError:
        pmi_izvest = 0
    max_pmi = max(pmi_anek, pmi_teh, pmi_izvest)
    if max_pmi == 0:
        continue
    if max_pmi == pmi_anek:
        cat = 'anek'
    elif max_pmi == pmi_teh:
        cat = 'teh'
    elif max_pmi == pmi_izvest:
        cat = 'izvest'
    print(bigram, cat, pmi_for_cats(bigram, cat))
    i += 1


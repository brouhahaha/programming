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
            anek += open(os.path.join(root, f), encoding = 'utf-8').read()
        elif 'izvest' in root:
            num_izvest = len(files)
            izvest += open(os.path.join(root, f), encoding = 'utf-8').read()
        elif 'teh_mol' in root:
            num_teh = len(files)
            teh += open(os.path.join(root, f), encoding = 'utf-8').read()
            
words_anek = preprocessing(anek)
words_teh = preprocessing(teh)
words_izvest = preprocessing(izvest)

words = words_anek + words_teh + words_izvest

def freq_dict(arr): # создаём частотный словарь
    dic = {}
    for element in arr:
        if element in dic:
            dic[element] += 1
        else:
            dic[element] = 1
    return dic

corpus_freq = freq_dict(words)
anek_freq = freq_dict(words_anek)
izvest_freq = freq_dict(words_izvest)
teh_freq = freq_dict(words_teh)

def first (dic): #берём первые сто самых частотных 
    i = 0
    for word in sorted(dic, key = lambda m: -dic[m]):
        if i > 100:
            break
        i += 1
    return dic

corpus_freq_first= first(corpus_freq)

def firstcat (dic):
    newdic = {}
    if word in words:
        newdic [word] = dic [word]
    return newdic

anek_freq_first = firstcat(anek_freq)
izvest_freq_first = firstcat(izvest_freq)
teh_freq_first = firstcat(teh_freq)

def pmi_for_cats(x, y): # вычисляем pmi для слова и категории
    words_ex = []
    freq_ex = {}
    if y == 'anek': # определяем, что за категория нам требуется, задаем её переменные (массив слов, число текстов)
        dic = anek_freq_first
        arr = words_anek
        num = num_anek
        words_ex = words - words_anek
        freq_ex = freqdict (words_ex)
    elif y == 'teh':
        dic = teh_freq_first
        arr = words_teh
        num = num_teh
        words_ex = words - words_teh
        freq_ex = freqdict (words_ex)
    elif y == 'izvest':
        dic = izvest_freq_first
        arr = words_izvest
        num = num_izvest
        words_ex = words - words_izvest
        freq_ex = freqdict (words_ex)
    p_xy = dic[x]/len(arr) # вероятность появления слова x в текстах категории y: частота этого слова на общ. кол-во слов
    p_x, p_y = freq_ex[x]/len(words_ex), num/(num_izvest + num_teh + num_anek) # вероятность появления слова в корпусе
    pmi = log(p_xy/(p_x * p_y))                                                 # и вероятность категории
    return pmi

cat_pmi = {}
i = 0
for word in corpus_freq: # для каждого слова вычисляем его PMI для всех категорий
    if i > 100:
        break
    try:
        pmi_anek = pmi_for_cats(word, 'anek') # интересующую нас категорию задаем вторым аргументов функции
    except KeyError: # не во всех категориях может встретиться это слово. "Глобализации" не будет в анекдотах...
        pmi_anek = 0
    try:
        pmi_teh = pmi_for_cats(word, 'teh')
    except KeyError:
        pmi_teh = 0
    try:
        pmi_izvest = pmi_for_cats(word, 'izvest')
    except KeyError:
        pmi_izvest = 0
    max_pmi = max(pmi_anek, pmi_teh, pmi_izvest) # выбираем максиальный коэффициент PMI
    if max_pmi == 0:
        continue
    if max_pmi == pmi_anek: # находим соответствующую этому коэффициенту категорию
        cat = 'anek'
    elif max_pmi == pmi_teh:
        cat = 'teh'
    elif max_pmi == pmi_izvest:
        cat = 'izvest'
    print(word, cat) 
    i += 1


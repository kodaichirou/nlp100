def ngram(n,lst):
    return list(zip(*[lst[i:] for i in range(n)]))

str='I am an NLPer'
words_bi_gram=ngram(2,str.split())
chars_bi_gram=ngram(2,str)

print('word_bi_gram:', words_bi_gram)
print('chars_bi_gram:', chars_bi_gram)



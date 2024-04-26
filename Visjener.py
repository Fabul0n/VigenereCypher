import itertools
import codecs
import json

def encrypt(word, key):
    res = ""
    j = 0
    for i in range(len(word)):
        if word[i] == ' ' or word[i] == ',' or word[i] == '.' or word[i] == '-':
            res += word[i]
            continue
        res += alph[(alph.find(word[i]) + alph.find(key[i%len(key)])) % 33]
        j += 1
    return res    

def decrypt(word, key):
    res = ""
    j = 0
    for i in range(len(word)):
        if word[i] == ' ' or word[i] == ',' or word[i] == '.' or word[i] == '-':
            res += word[i]
            continue
        res += alph[(alph.find(word[i]) - alph.find(key[j%len(key)]) + 33) % 33]
        j += 1
    return res    

def find_key(res, cypher):
    key = ""
    for i in range(len(res)):
        key += alph[(0 - alph.find(res[i]) + 33 + alph.find(cypher[i]) - 1) % 33]
    return key
alph = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

#cypher = "ЖИЪПЦДДЙЯПУЦ, ЩЧА ОА ЮРЛЦО МЯВЧН, ЯЧА ФУ, ИФУ ЮЭ ТЬЩЙФР ТЦ ЙТСЖС, Ъ ЯЧА ДАГЪНЫ СУЭЖЧ ИЖРАДЙИЖЦЬРО ЮХИВРЦДК."

cypher = "ПЬИВЬЖЧЬЕЛ - РЙЪ БЬ ЪЦЗЛБАГШЕФШ ИНВШЪЧТ. ИЁЁ ЪЁИРКЬЩЬЬ НЕЬОВ ГФЛЕРЦЁ."

decr = "Дисциплина- это не ограничение свободы. Это отсечение всего лишнего"

print(decrypt(cypher, "ЛУЧ"))

'''for i in range(1, 6):
    for _ in itertools.combinations(alph, i):
        key = "".join(_)
        ans = decrypt(cypher, key)
        if ans.find('') != -1:
            with codecs.open('otpt.out', 'a', encoding='utf-8') as fout:
                fout.write(ans+"\n")
            #print(key)
            #print(ans)
            #print()
    with codecs.open('otpt.out', 'a', encoding='utf-8') as fout:
        fout.write("\n")'''
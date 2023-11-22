#!/usr/bin/python3
# -*- coding: utf-8 -*-
#3
#Дано ошибочно написанное слово роцессорп. Путем перемещения его букв получить слово
#процессор.
word = "роцессорп"
print("Слово: ",word)
list = []
for i in word:
    list.append(i)
print("По буквам: " ,list)
try_word=["g"]
b = int(len(list)-1)
a =list[b]
try_word[0] = a
count = 0
for l in list:
    count+=1
    if count != b+1:
        try_word.append(l)
r = " "
print("По буквам: " ,try_word)  
for i in try_word:
    r +=i
print("Слово: " ,r)  
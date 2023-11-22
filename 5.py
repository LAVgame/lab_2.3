#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 19. Дано предложение. Найти длину его самого короткого слова.
str = "Дано предложение, найти длину его самого короткого слова." #его
arr_str = []
for i in str:
        arr_str.append(i) 

count = int(0)
min_index = -1
min = 99
for i in range(0,len(arr_str) - 1):
    if arr_str[i] != " ": 
          count += 1   
    if arr_str[i] == " ": 
        if min > count:
              min = count
              min_index = i - 1
        count = 0
word = ""
for i in range (0, min): 
    word += arr_str[min_index - min+1  + i ]
print(f"Полученное словов: {word}")

#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Дан текст. Сколько раз в нем встречается символ «+» и сколько раз символ «*»?
print("Введите текст")
string ="0"
string = input()
count = 0
for  i in string:
    if(i == "+" or i == "*"):
        count +=1

print(f"Колличестов + и *: {count}")
# -- coding: utf-8 --
# Дана строка Hi

def string():
    s = str(input("Введите строку: "))
    print(s[2])
    print(s[-2])
    print(s[:5])
    print(s[:-2])
    print(s[0::2])
    print(s[1::2])
    print(s[::-1])
    print(s[-1::-2])
    print(len(s))


string()

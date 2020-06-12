
a=int(input())
binary=bin(a)#конвертируем число в бинарный код
reverse=binary[-1:1:-1]#делаем обратный отчет
d=int(reverse,2)#конвертируем бинарный код в число
print(d)
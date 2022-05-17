h = int(input("Введите часы: "))
m = int(input("Введите минуты: "))
s = int(input("Введите секунды: "))
g = h*30+m*0.5+s*0.008
print('%.3f' % g)
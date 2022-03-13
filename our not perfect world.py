import matplotlib.pyplot as plt
print("здесь мы можете покидать монетку и убедьться, что школьная теория вероятностей плохо работает в реальном мире")
attempt = int(input("сколько раз хотете совршить серию из 100 подкидываний?"))
import random
c=[]
for r in range(attempt+1):
    b=0
    for i in range (101):
        a =random.randint(0,1)
        if a==1:
            b=b+1
    c.append(b) 
l = list(range(min(c),max(c)))
r=[]
h=min(c)#начинаем с минимального числа в списке
for o in range(len(l)): #прогоняем цикл столько раз, сколько элементов у нас в списке l (это нужно, чтобы график мог построиться)
    r.append(c.count(h))#счтаем сколько у нас элементов находится в основном списке "с" и заносим кол-во в список r
    h=+h#прибавляем к h 1 чтобы начать считать колл-во следующих элементов
print("вот резульаты ваших серий")
print(c)  
print("минимально колличество одной выповшей стороны в серии: ",min(c))
print("максимальное колличество одной выпавшей стороны в серии: ",max(c))
print("в скольки сериях вероятность составила идеальные 50/50: ",c.count(50))
print(l)
print(r)
plt.title("no perfect world")
plt.xlabel("i don't know")
plt.ylabel("numbers")
plt.plot(r, l)
plt.legend("legenda")
plt.show()
input()
import time
import random 
r = int((input("сколько попыток?")))
pl=["+", "-"]
print("Нажми на enter чтобы начать")
input()
ts = time.time()
for i in range(r):
    a = random.randint(1,9)
    b = random.randint(1,9)
    c = random.randint(1,9)
    d = random.choice(pl)
    e = random.choice(pl)
    print(a, d, b, e, c)
    input()
tsd = time.time()
print("потрачено вренени:", round(tsd-ts, 1), "секунды")
input()


import matplotlib.pyplot as plt
import random
import time
money = random.randint(100, 450)
value = random.randint(20, 250)
print("start money:", money)
print("start stock price:", value)
print(" ")
stock = 0
cooldown = 0
acc = 0
h1 = 0
h2 = 0
h3 = 0
h4 = 0
h5 = 0
h6 = 0
h7 = 0
h8 = 0
h9 = 0
h10 = 0
h11 = 0
h12 = 0
h13 = 0
h14 = 0
h15 = 0
h16 = 0
h17 = 0
h18 = 0
h19 = 0
h20 = 0
s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0
s6 = 0
s7 = 0
s8 = 0
s9 = 0
s10 = 0
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
y = [h20,h19,h18,h17,h16,h15,h14,h13,h12,h11,h10,h9,h8,h7,h6,h5,h4,h3,h2,h1,value]
def update():
  global h20,h19,h18,h17,h16,h15,h14,h13,h12,h11,h10,h9,h8,h7,h6,h5,h4,h3,h2,h1,value
  h20 = h19
  h19 = h18
  h18 = h17
  h17 = h16
  h16 = h15
  h15 = h14
  h14 = h13
  h13 = h12
  h12 = h11
  h11 = h10
  h10 = h9
  h9 = h8
  h8 = h7
  h7 = h6
  h6 = h5
  h5 = h4
  h4 = h3
  h3 = h2
  h2 = h1
  h1 = value
def tstock(cost):
  if s1 == 1:
    s1 = cost
    print("S1 is now:", s1)

def buy(amount):
  global money, stock, s1,s2,s3,s4,s5,s6,s7,s8,s9,s10
  money = money - amount
  stock = stock + 1
  s10 = s9
  s9 = s8
  s8 = s7
  s7 = s6
  s6 = s5
  s5 = s4
  s4 = s3
  s3 = s2
  s2 = s1
  s1 = amount
  print(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10)
  print("[BOUGHT] 1x for:", amount, "total stock:", stock)
  print("money left:", money)
  print(" ")

def sell(amount):
  global money, stock, value
  if amount > stock:
    print("selling what you dont have idiot")
    print(" ")
    return
  money += value * amount
  stock = stock -amount
  print("[SOLD]", amount, "each:", value, "total stock:", stock)
  print("money left:", money)
  print(" ")

while True:
  plt.clf()
  update()
  y = [h20,h19,h18,h17,h16,h15,h14,h13,h12,h11,h10,h9,h8,h7,h6,h5,h4,h3,h2,h1,value]
  plt.plot(x, y)
  plt.show()
  valrng = random.randint(1, 2)
  if valrng == 1:
    value = value + random.randint(0, 25)
  if valrng == 2:
    value = value - random.randint(0, 25)
    if value < 0:
      value = 1
  ave = value+h1+h2+h3+h4+h5+h6+h7+h8+h9+h10+h11+h12+h13+h14+h15+h16+h17+h18+h19+h20
  ave = ave / 21
  cooldown = cooldown + 1
  tts = ave + 50
  if value > tts and cooldown > 80 and stock > 0:
    sell(random.randint(1, stock))
  tts = ave +50
  rng = random.randint(1,150)
  if value < tts and cooldown > 80 and money > rng:
    buy(rng)













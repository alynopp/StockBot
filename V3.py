#  x = [1,2,3,4,5,6,7,8]
#  y = [h7,h6,h5,h4,h3,h2,h1,value]
#  plt.plot(x, y)
#  plt.show()

import matplotlib.pyplot as plt
import random
import time
money = random.randint(100, 450)
value = random.randint(20, 250)
print("start money:", money)
print("stock start price:", value)
print(" ")
stock = 0

def buy(amount):
  global money, stock
  money = money - amount
  stock = stock + 1
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
x = [1,2,3,4,5,6,7,8]
h1 = 0
h2 = 0
h3 = 0
h4 = 0
h5 = 0
h6 = 0
h7 = 0
hw = 1
oldval = 0
# ave = h1+h2+h3+h4+h5+h6+h7
# ave = ave / 7
cooldown = 0
while True:
  plt.clf()
  oldval = value
  if hw > 7:
    hw = 1
  if hw == 1:
    h7 = h6
    h6 = h5
    h5 = h4
    h4 = h3
    h3 = h2
    h2 = h1
    h1 = oldval
  if hw == 2:
    h7 = h6
    h6 = h5
    h5 = h4
    h4 = h3
    h3 = h2
    h2 = oldval
  if hw == 3:
    h7 = h6
    h6 = h5
    h5 = h4
    h4 = h3
    h3 = oldval
  if hw == 4:
    h7 = h6
    h6 = h5
    h5 = h4
    h4 = oldval
  if hw == 5:
    h7 = h6
    h6 = h5
    h5 = oldval
  if hw == 6:
    h7 = h6
    h6 = oldval
  if hw == 1:
    h7 = oldval
  # print("history:", h1, h2, h3, h4, h5, h6, h7)
  hw = hw + 1
  y = [h7,h6,h5,h4,h3,h2,h1,value]
  plt.plot(x, y)
  plt.show()
  valrng = random.randint(1, 2)
  if valrng == 1:
    value = value + random.randint(1, 25)
  if valrng == 2:
    value = value - random.randint(1, 25)
    if value < 0:
      value = 1
  cooldown = cooldown + 1
  ave = h1+h2+h3+h4+h5+h6+h7
  ave = ave / 7
  if value < ave and cooldown > 50:
    rng = random.randint(1, 150)
    aac = money - rng
    if aac > 1:
      buy(rng)
  if value > ave and stock > 0:
    rng = random.randint(1, stock)
    sell(rng)
  
    
  

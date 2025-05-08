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
h21 = 0
h22 = 0
h23 = 0
h24 = 0
h25 = 0
h26 = 0
h27 = 0
h28 = 0
h29 = 0
h30 = 0
h31 = 0
h32 = 0
h33 = 0
h34 = 0
h35 = 0
h36 = 0
h37 = 0
h38 = 0
h39 = 0
h40 = 0
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
s11 = 0
s12 = 0
s13 = 0
s14 = 0
s15 = 0
s16 = 0
s17 = 0
s18 = 0
s19 = 0
s20 = 0
s21 = 0
s22 = 0
s23 = 0
s24 = 0
s25 = 0
s26 = 0
s27 = 0
s28 = 0
s29 = 0
s30 = 0
s31 = 0
s32 = 0
s33 = 0
s34 = 0
s35 = 0
s36 = 0
s37 = 0
s38 = 0
s39 = 0
s40 = 0
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
y = [h40,h39,h38,h37,h36,h35,h34,h33,h32,h31,h30,h29,h28,h27,h26,h25,h24,h23,h22,h21,h20,h19,h18,h17,h16,h15,h14,h13,h12,h11,h10,h9,h8,h7,h6,h5,h4,h3,h2,h1,value]
def update():
  global h40,h39,h38,h37,h36,h35,h34,h33,h32,h31,h30,h29,h28,h27,h26,h25,h24,h23,h22,h21,h20,h19,h18,h17,h16,h15,h14,h13,h12,h11,h10,h9,h8,h7,h6,h5,h4,h3,h2,h1,value
  h40 = h39
  h39 = h38
  h38 = h37
  h37 = h36
  h36 = h35
  h35 = h34
  h34 = h33
  h33 = h32
  h32 = h31
  h31 = h30
  h30 = h29
  h29 = h28
  h28 = h27
  h27 = h26
  h26 = h25
  h25 = h24
  h24 = h23
  h23 = h22
  h22 = h21
  h21 = h20
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
def buy(amount):
  global money, stock, s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,s30,s31,s32,s33,s34,s35,s36,s37,s38,s39,s40
  money = money - amount
  stock = stock + 1
  s40 = s39
  s39 = s38
  s38 = s37
  s37 = s36
  s36 = s35
  s35 = s34
  s34 = s33
  s33 = s32
  s32 = s31
  s31 = s30
  s30 = s29
  s29 = s28
  s28 = s27
  s27 = s26
  s26 = s25
  s25 = s24
  s24 = s23
  s23 = s22
  s22 = s21
  s21 = s20
  s20 = s19
  s19 = s18
  s18 = s17
  s17 = s16
  s16 = s15
  s15 = s14
  s14 = s13
  s13 = s12
  s12 = s11
  s11 = s10
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
  print(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,s30,s31,s32,s33,s34,s35,s36,s37,s38,s39,s40)
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
  y = [h40,h39,h38,h37,h36,h35,h34,h33,h32,h31,h30,h29,h28,h27,h26,h25,h24,h23,h22,h21,h20,h19,h18,h17,h16,h15,h14,h13,h12,h11,h10,h9,h8,h7,h6,h5,h4,h3,h2,h1,value]
  plt.plot(x, y)
  plt.show()
  valrng = random.randint(1, 2)
  if valrng == 1:
    value = value + random.randint(0, 25)
  if valrng == 2:
    value = value - random.randint(0, 25)
    if value < 0:
      value = 1
  ave = value+h1+h2+h3+h4+h5+h6+h7+h8+h9+h10+h11+h12+h13+h14+h15+h16+h17+h18+h19+h20+h21+h22+h23+h24+h25+h26+h27+h28+h29+h30+h31+h32+h33+h34+h35+h36+h37+h38+h39+h40
  ave = ave / 41
  cooldown = cooldown + 1
  tts = ave + 50
  if value > tts and cooldown > 80 and stock > 0:
    if any (value > s for s in [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,s30,s31,s32,s33,s34,s35,s36,s37,s38,s39,s40]):
      sell(random.randint(1, stock))
  tts = ave +50
  rng = random.randint(1,150)
  if value < tts and cooldown > 80 and money > rng:
    buy(rng)


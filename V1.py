import random
import time
money = random.randint(50, 300)
value = random.randint(20, 250)
stock = 0
print("money:", money)
print("current market value:", value)
print("starting...")
print(" ")
time.sleep(1)

def buy(ammount):
  global money
  global stock
  stock = stock + 1
  money = money - ammount
  print("[BOUGHT] 1x for:", ammount, "totle stock:", stock)
  print("money left:", money)
  print(" ")
def sell():
  global money
  global stock
  stock = stock - 1
  money = money + value
  print("[SOLD] 1x for:", value, "totle stock:", stock)
  print("money now:", money)
  print(" ")
bstock = 0



while True:
  time.sleep(5)
  oldval = value
  value = random.randint(1, 300)
  print("old:", oldval, "new:", value)
  if oldval < value:
    print("stock went [UP].")
    if oldval < value and stock > 0:
      sell()
  if oldval > value:
    print("stock went [DOWN].")
    rng = random.randint(1, 150)
    if rng < money:
      bstock = rng
      buy(rng)
  print(" ")

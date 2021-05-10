import math
import time

regular_money = int(input("How much money will you put in each month? : "))
object_interset = int(input("How much percent is your object interset? : ")) / 100 + 1
term = int(input("How many years will you invest? : "))
total_money = 0

for i in range(1, term+1):
    total_money += regular_money * (object_interset ** i)

total_money = round(total_money)
split_money = []
while(total_money):
    split_money.append(str(int(total_money % 10000)))
    total_money = total_money // 10000

korean_money = ""
unit_money = ["원", "만", "억", "조"]

for i, money in enumerate(split_money):
    korean_money = money + unit_money[i] + korean_money

print()
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)


print()
print("-----------------------------------------" + "-"*(len(korean_money)))
print("| Money to receive after %d years :" %(term), korean_money, '|')
print("-----------------------------------------" + "-"*(len(korean_money)))


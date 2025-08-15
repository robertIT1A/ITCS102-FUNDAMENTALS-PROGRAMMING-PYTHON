name = input("Enter your Name : ")
age = int(input("Enter your Age : "))
address = input("Enter your Address : ")
amount = int(input("Enter amount to Deposit : "))

onethou = amount//1000
onethous = amount%1000
fivehund = onethous//500
fivehundr = onethous%500
twohund = fivehundr//200
twohundr = fivehundr%200
onehund = twohundr//100
onehundr = twohundr%100
fifty = onehundr//50
fiftys = onehundr%50
twe = fiftys//20
twent = fiftys%20
ten = twent//10
tens = twent%10
peso = tens//1
pesos = tens%1
print("Here is a breakdown using Philippine denominition:")
print(onethou,"-- 1000")
print(fivehund,"-- 500")
print(twohund,"-- 200")
print(onehund,"-- 100")
print(fifty,"-- 50")
print(twe,"-- 20")
print(ten,"-- 10")
print(peso,"-- 1")


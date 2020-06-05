# 금액을 입력받는다.
price = int(input("금액 : "))

# 딕셔너리 선언
moneys = {}

#딕셔너리에 아이템 추가
moneys[50000] = int(price / 50000)
price = price % 50000 # 50000원권을 사용하고 남은 금액

moneys[10000] = int(price / 10000)
price = price % 10000 # 10000원권을 사용하고 남은 금액 

moneys[5000] = int(price / 5000)
price = price % 5000 # 5000원권을 사용하고 남은 금액 

moneys[1000] = int(price / 1000)
price = price % 1000 # 1000원권을 사용하고 남은 금액 

moneys[500] = int(price / 500)
price = price % 500 # 500원권을 사용하고 남은 금액 

moneys[100] = int(price / 100)
price = price % 100 # 100원권을 사용하고 남은 금액 

moneys[50] = int(price / 50)
price = price % 50 # 50원권을 사용하고 남은 금액 

moneys[10] = int(price / 10)
price = price % 10 # 10원권을 사용하고 남은 금액 

moneys[5] = int(price / 5)
price = price % 5 # 5원권을 사용하고 남은 금액 

moneys[1] = price

types = 0 # 화폐의 종류 
counts = 0 # 총 개수 

for money in moneys:
    print(money,":",moneys[money])
    
    if moneys[money] != 0:
        types += 1
        counts += moneys[money]

print("총", types, "종류", counts, "개 필요")

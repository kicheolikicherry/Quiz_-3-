exchange_rates = {'달러': 1320, '엔': 950, '위안': 182}

money = [13, 200, 13]

total = money[0] * exchange_rates['달러'] + money[1] * exchange_rates['엔'] + money[2] * exchange_rates['위안']

print("철수가 가지고 있는 돈의 원화 가치는", total, "원 입니다.")


deposit = []
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму:"))
deposit.append(round(per_cent['ТКБ']*money/100))
deposit.append(round(per_cent['СКБ']*money/100))
deposit.append(round(per_cent['ВТБ']*money/100))
deposit.append(round(per_cent['СБЕР']*money/100))
print(deposit)
max_value = max(deposit)
print("Максимальная сумма, которую вы можете заработать - ", max_value)
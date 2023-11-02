from datetime import date

dates = [date.fromisoformat(input()) for _ in range(2)]

print(min(dates).strftime('%d-%m (%Y)'))

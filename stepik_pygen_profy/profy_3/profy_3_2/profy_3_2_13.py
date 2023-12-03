from datetime import date

dates = [date.fromisoformat(input()) for _ in range(int(input()))]
[print(d.strftime('%d/%m/%Y')) for d in sorted(dates)]

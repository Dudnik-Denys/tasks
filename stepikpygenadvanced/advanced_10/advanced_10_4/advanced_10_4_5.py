countries = {(lst := tuple(input().split()))[1:]: lst[0] for _ in range(int(input()))}
print(countries)

for _ in range(int(input())):
    city = input()
    for cities, country in countries.items():
        if city in cities:
            print(country)
            break

# d = {}
# for _ in range(int(input())):
#     country, *cities = input().split()
#     d.update(dict.fromkeys(cities, country))
# for _ in range(int(input())):
#     print(d[input()])

def decimal_ip_present(ip):
    ip = [int(num) for num in ip.split('.')]
    total = 0
    for i in range(4):
        total = total + (ip[i] * 256 ** abs(i - 3))

    return total


data = [input() for _ in range(int(input()))]

print(*sorted(data, key=lambda x: decimal_ip_present(x)), sep='\n')

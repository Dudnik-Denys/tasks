director = set(input().split())
assistant = set(input().split())
print(*sorted(director | assistant))

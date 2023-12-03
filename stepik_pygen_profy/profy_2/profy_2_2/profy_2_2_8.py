emails = [input() for _ in range(int(input()))]
new_emails = [input() for _ in range(int(input()))]

for email in new_emails:

    if email + '@beegeek.bzz' not in emails:
        emails.append(email + '@beegeek.bzz')

    elif email + '@beegeek.bzz' in emails:
        count = 1
        new = email + str(count) + '@beegeek.bzz'

        while new in emails:
            count += 1
            new = email + str(count) + '@beegeek.bzz'

        emails.append(new)

print(*emails[-len(new_emails):], sep='\n')

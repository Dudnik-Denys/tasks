names = [input() for _ in range(int(input()))]
shuffle_names = names[:]
size = len(shuffle_names)

for i in range(size):
    if names[i] != shuffle_names[-1]:
        print(names[i], '-', shuffle_names[-1])
        shuffle_names.remove(shuffle_names[-1])
    elif names[i] == shuffle_names[-1]:
        print(names[i], '-', shuffle_names[-2])
        shuffle_names.remove(shuffle_names[-2])

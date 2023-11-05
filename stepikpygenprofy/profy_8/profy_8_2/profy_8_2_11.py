def sands_of_time(index=1, size=16):
    if size > 4:
        print(f'{str(index) * size}'.center(size + ((index - 1) * 4)))
        sands_of_time(index + 1, size - 4)
        print(f'{str(index) * size}'.center(size + ((index - 1) * 4)))
    else:
        print(f'{str(index) * size}'.center(size + ((index - 1) * 4)))


sands_of_time()

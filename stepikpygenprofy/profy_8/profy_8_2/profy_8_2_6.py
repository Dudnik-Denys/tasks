def from_to(from_number: int = 1, to_number: int = 100):
    if from_number <= to_number:
        print(from_number)
        from_to(from_number + 1, to_number)


from_to()

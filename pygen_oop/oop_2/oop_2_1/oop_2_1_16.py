def annual_return(start: int, percent: int, years: int) -> None:
    while years > 0:
        start = start + (start * (percent / 100))
        yield start
        years -= 1

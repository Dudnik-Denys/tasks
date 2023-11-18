def average(salary: list[int]) -> float:
    salary.remove(max(salary))
    salary.remove(min(salary))
    return sum(salary) / len(salary)

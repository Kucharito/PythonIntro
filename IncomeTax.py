def income_calculator(income):
    if income <= 0:
        raise ValueError("Income must be a positive number")

    tax = 0
    if income > 20000:
        tax += (income - 20000) * 0.2
        income = 20000
    if income > 10000:
        tax += (income - 10000) * 0.1
        income = 10000
    tax += income * 0

    return tax


if __name__ == "__main__":
    income = int(input("Input your income: "))
    tax = income_calculator(income)
    print(f"Your tax is {tax}")
def main():
    try:
        income = int(input("Enter your salary: ").strip())
        print("Tax amount:", calcTax(income))
    except ValueError:
        print("Please enter a valid salary number.")
def calcTax(income):
    tax = 0
    if income < 10000:
        tax = 0
    elif income < 20000:
        tax = 0.1 * (income -10000)
    elif income < 30000:
        tax = 1500 + 0.15 * (income - 20000)
    elif income < 50000:
        tax = 2500 + 0.2 * (income - 30000)
    else:
        tax = 6500 + 0.3 * (income - 50000)

    return tax
main()


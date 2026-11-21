
# Christopher Aguilar
# CMP 131
# Week: 9
# Lab: 1
# Assignment: Future Value Calculator
# Date: 11/21/2026

def futureValue(present_value, monthly_interest_rate, months):
    future_value = present_value * (1 + monthly_interest_rate) ** months
    return future_value


def main():

    print("===== FUTURE VALUE CALCULATOR =====")

    present_value = float(input("Enter the present value ($): "))
    monthly_interest_percent = float(input("Enter the monthly interest rate (%): "))
    months = int(input("Enter the number of months: "))

    if present_value < 0:
        print("Error: Present value cannot be negative.")
        return

    if monthly_interest_percent < 0:
        print("Error: Monthly interest rate cannot be negative.")
        return

    if months <= 0:
        print("Error: Number of months must be greater than zero.")
        return

    monthly_interest_rate = monthly_interest_percent / 100

    future_value = futureValue(present_value, monthly_interest_rate, months)

    print("\n===== ACCOUNT SUMMARY =====")
    print(f"Present Value: ${present_value:,.2f}")
    print(f"Monthly Interest Rate: {monthly_interest_percent:g}%")
    print(f"Number of Months: {months}")
    print(f"Future Value: ${future_value:,.2f}")


main()

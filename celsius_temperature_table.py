
# Christopher Aguilar
# CMP 131
# Week: 9
# Lab: 1
# Assignment: Celsius Temperature Table
# Date: 11/21/2026

def celsius(fahrenheit):
    celsius_temp = (5 / 9) * (fahrenheit - 32)
    return celsius_temp


def main():

    print("===== FAHRENHEIT TO CELSIUS TABLE =====")
    print(f"{'Fahrenheit':<15}{'Celsius':>10}")
    print("-" * 25)

    for fahrenheit in range(0, 21):
        celsius_temp = celsius(fahrenheit)

        print(f"{fahrenheit:<15}{celsius_temp:>10.2f}")

main()

### EXERCICE 1


def main():
    annual_salary = float(input("Enter your annual salary in Lyon: "))
    portion_saved = float(input("Enter the portion of salary to be saved, as a decimal: "))
    total_cost = float(input("Enter the cost of your dream home in Lyon: "))

    r = 0.04
    portion_down_payment = 0.25

    down_payment = total_cost * portion_down_payment
    current_savings = 0.0
    months = 0
    monthly_salary = annual_salary / 12.0
    monthly_return = r / 12.0

    while current_savings < down_payment:
        current_savings += current_savings * monthly_return
        current_savings += monthly_salary * portion_saved
        months += 1

    print(f"Number of months: {months}")




### EXERCICE 3

def months_to_save(annual_salary, savings_rate, months=36, r=0.04, semi_annual_raise=0.07):
    """Simulate savings over a fixed number of months with semi-annual raises."""
    monthly_return = r / 12.0
    current_savings = 0.0
    monthly_salary = annual_salary / 12.0

    for m in range(1, months + 1):
        current_savings += current_savings * monthly_return
        current_savings += savings_rate * monthly_salary
        if m % 6 == 0:
            annual_salary *= (1.0 + semi_annual_raise)
            monthly_salary = annual_salary / 12.0
    return current_savings

def main():
    portion_down_payment = 0.25
    total_cost = 1_000_000.0
    target = portion_down_payment * total_cost  
    epsilon = 100.0  
    r = 0.04
    semi_annual_raise = 0.07

    starting_salary = float(input("Enter the starting salary in Lyon: "))

    max_savings = months_to_save(starting_salary, 1.0, 36, r, semi_annual_raise)
    if max_savings < target - epsilon:
        print("It is not possible to pay the down payment in three years.")
        return

    low = 0.0
    high = 1.0
    steps = 0
    best_rate = None

    while True:
        steps += 1
        mid = (low + high) / 2.0
        saved = months_to_save(starting_salary, mid, 36, r, semi_annual_raise)

        if abs(saved - target) <= epsilon:
            best_rate = mid
            break

        if saved < target:
            low = mid 

        if high - low < 1e-7:
            best_rate = mid
            break

    print(f"Best savings rate: {best_rate:.4f}")
    print(f"Steps in bisection search: {steps}")

if __name__ == "__main__":
    main()

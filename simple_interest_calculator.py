def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

principal_amount = 1000
interest_rate = 5
time_period = 2

result = calculate_simple_interest(principal_amount, interest_rate, time_period)
print(f"Simple Interest: ${result}")


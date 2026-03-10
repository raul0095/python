# Define the function to compute pay
def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        overtime_hours = hours - 40
        pay = (40 * rate) + (overtime_hours * rate * 1.5)
    return pay

# Prompt the user for input
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

# Convert input to float
hours = float(hours)
rate = float(rate)

# Call the function and print the result
gross_pay = computepay(hours, rate)
print("Pay:", gross_pay)



# advanced script

# Define the function to compute pay
def computepay(hours, rate):
    if hours <= 40:
        return hours * rate
    else:
        overtime = hours - 40
        return (40 * rate) + (overtime * rate * 1.5)

# Function to get valid, non-negative float input
def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Get user input
hours = get_valid_input("Enter Hours: ")
rate = get_valid_input("Enter Rate: ")

# Compute pay
gross_pay = computepay(hours, rate)
print("Pay:", gross_pay)

# Ask if user wants to save the result
save = input("Would you like to save the result to a file? (yes/no): ").strip().lower()
if save in ['yes', 'y']:
    filename = input("Enter filename to save (e.g., pay.txt): ").strip()
    try:
        with open(filename, "w") as file:
            file.write(f"Hours worked: {hours}\n")
            file.write(f"Hourly rate: {rate}\n")
            file.write(f"Gross pay: {gross_pay}\n")
        print(f"Result saved to {filename}")
    except Exception as e:
        print("An error occurred while saving the file:", e)

# 3 prompts for user inpu
import operator


operators = {
	1: {
		"operator": "+"
	},
	2: {
		"operator": "-"
	},
	3: {
		"operator": "*"
	},
	4: {
		"operator": "/"
	}
}








# print(operators[1]["operator"])

while True:
	try:
		number1 = int(input("Enter number:"))
		choice = int(input(f"""Choose operator:
1.	+ (Addition)
2.	- (Subtraction)
3.	* (Multiplication)
4.	/ (Division)
"""))
		operators[choice]
		number2 = int(input("Enter number:"))

		if choice == 1:
			print(f"Result: {number1} {operators[1]['operator']} {number2} =", int(number1 + number2))
			break
		elif choice == 2:
			print(f"Result: {number1} {operators[2]['operator']} {number2} =", int(number1 - number2))
			break
		elif choice == 3:
			print(f"Result: {number1} {operators[3]['operator']} {number2} =", int(number1 * number2))
			break
		elif choice == 4:
			print(f"Result: {number1} {operators[4]['operator']} {number2} =", number1 / number2)
			break

	except ValueError:
		print("Error: Enter a number")
	except KeyError:
		print("Error: Choose valid option.")
	except ZeroDivisionError:
		print("Cannot divide by zero.")
# birth_year = input("Enter your birth year: ")
# age = 2025 - int(birth_year)

# # int(birth_year) converts the string input "1990" to integer 1990

# print(age)



#--


# first = input("First: ")

# second = input("Second: ")

# total = float(first) + float(second)

# print("Total: ", total)


#-- To ensure the input fails if not floating point

# first = float(input("First: "))

# second = float(input("Second: "))

# total = first + second

# print("Total: ", str(total))




# string replacement

text = "This is a string."

print("Initial: ", text)

print("Folosim .replace() ca sa inlocuim parti din string: ", text.replace('string', 'how to replace a string'))
if "string" in text:
 	print("Good job!")





# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         print("Your input is: ", x)
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")

# number = 3
# assert (number < 5), f"The number should not exceed 5. ({number=})"
# print(number)

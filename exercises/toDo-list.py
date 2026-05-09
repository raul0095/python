


operators = {
	1: "1. Add task",
	2: "2. Remove task",
	3: "3. View Tasks",
	4: "4. Quit"
}

print(operators[2])

todo = ["Add task", "Remove task", "View Tasks", "Quit"]
for i, value in enumerate(todo, 1):
    print(i, value)


filled_dict = {1: "1. Add task", 2: "2. Remove task", 3: "3. View Tasks", 4: "4. Quit"}
our_iterable = filled_dict.keys()
print(our_iterable)  # => dict_keys(['one', 'two', 'three']). This is an object
                     # that implements our Iterable interface.


	# except ValueError:
	# 	print("Error: Enter a number")
	# except KeyError:
	# 	print("Error: Choose valid option.")
	# except ZeroDivisionError:
	# 	print("Cannot divide by zero.")
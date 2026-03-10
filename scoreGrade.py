# Prompt the user for a score
score = input("Enter score: ")

# Convert input to float
score = float(score)

# Check if score is within the valid range
if score < 0.0 or score > 1.0:
    print("Error: Score is out of range. Please enter a value between 0.0 and 1.0.")
else:
    # Determine the grade
    if score >= 0.9:
        grade = "A"
    elif score >= 0.8:
        grade = "B"
    elif score >= 0.7:
        grade = "C"
    elif score >= 0.6:
        grade = "D"
    else:
        grade = "F"
    print("Grade:", grade)

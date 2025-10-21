def get_valid_grade(prompt):
    while True:
        try:
            grade = float(input(prompt))
            if 0.0 <= grade <= 4.0:
                return grade
            else:
                print("Invalid input: Grade must be between 0.0 and 4.0.")
        except ValueError:
            print("Invalid input: Please enter a numeric value.")

def calculate_gpa(grades):
    return round(sum(grades) / len(grades), 2)

def main():
    print("Welcome to the Overly Verbose GPA Calculator!\n")

    while True:
        try:
            num_classes = int(input("How many classes are you in? (min 5): "))
            if num_classes >= 5:
                break
            else:
                print("You must have at least 5 classes. Try again.")
        except ValueError:
            print("Please enter a valid number.")

    grades = []
    for i in range(num_classes):
        grade = get_valid_grade(f"Enter grade {i + 1} (0.0 - 4.0): ")
        grades.append(grade)

    current_gpa = calculate_gpa(grades)
    print(f"\nCalculating... beep boop... Your current GPA is: {current_gpa}\n")

    print("Which semester do you want to analyze?")
    print("1. First semester (first half of classes)")
    print("2. Second semester (second half of classes)")

    while True:
        choice = input("Enter 1 or 2: ").strip()
        if choice in ("1", "2"):
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    midpoint = len(grades) // 2
    if choice == "1":
        semester_grades = grades[:midpoint]
        semester_name = "First semester"
    else:
        semester_grades = grades[midpoint:]
        semester_name = "Second semester"

    semester_gpa = calculate_gpa(semester_grades)
    print(f"\n{semester_name} GPA: {semester_gpa}")
    print(f"Overall GPA: {current_gpa}")

    if semester_gpa > current_gpa:
        print("Nice! You're trending upward.")
    elif semester_gpa < current_gpa:
        print("Looks like the second half was a bit tougher. You'll bounce back.")
    else:
        print("Consistent performance! Keep it steady.")

    while True:
        try:
            goal_gpa = float(input("\nWhat's your goal GPA? "))
            if 0.0 <= goal_gpa <= 4.0:
                break
            else:
                print("Goal GPA must be between 0.0 and 4.0.")
        except ValueError:
            print("Please enter a valid number.")

    print()
    if current_gpa >= goal_gpa:
        print(f"Congratulations! Your current GPA of {current_gpa} already meets or exceeds your goal of {goal_gpa}.")
        return

    achievable = False
    for i in range(len(grades)):
        new_grades = grades.copy()
        new_grades[i] = 4.0
        new_gpa = calculate_gpa(new_grades)
        if new_gpa >= goal_gpa:
            if not achievable:
                print(f"Good news! You can reach your goal of {goal_gpa} by improving just ONE grade:")
                achievable = True
            print(f"- If you raise your grade in class {i + 1} from {grades[i]} to 4.0, your GPA would be {new_gpa}")

    if not achievable:
        print(f"Sorry, raising only one grade to 4.0 won't reach your goal of {goal_gpa}.")
        print("You'll need to improve multiple grades. Time to hit the books.")
    else:
        print("\nTime to hit the books and make it happen.")

if __name__ == "__main__":
    main()

def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'

def main():
    try:
        score = float(input("Enter the student's score: "))
        if 0 <= score <= 100:
            grade = calculate_grade(score)
            print(f"The student's grade is: {grade}")
        else:
            print("Please enter a score between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()

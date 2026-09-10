def calculate_grade(average):
    grades = {
        90: "A+",
        80: "A",
        70: "B",
        60: "C",
        50: "D",
        0: "F"
    }

    for mark, grade in grades.items():
        if average >= mark:
            return grade


def main():
    subjects = {}
    n = int(input("Enter number of subjects: "))

    for i in range(n):
        subject = input(f"Enter subject {i + 1}: ")
        marks = float(input(f"Enter marks for {subject}: "))
        subjects[subject] = marks

    total = sum(subjects.values())
    average = total / n
    grade = calculate_grade(average)

    print("\n----- Grade Report -----")

    for subject, marks in subjects.items():
        print(f"{subject}: {marks}")

    print(f"\nTotal Marks: {total}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")


main()

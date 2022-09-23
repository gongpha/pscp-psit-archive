"""Something Something"""

def grade(score: float) -> float:
    """Calculate Grade from input"""
    return (
        4.0 if score >= 95 else
        3.5 if score >= 90 else
        3.0 if score >= 85 else
        2.5 if score >= 80 else
        2.0 if score >= 75 else
        1.5 if score >= 70 else
        1.0 if score >= 65 else
        0.5 if score >= 60 else
        0.0
    )

def main() -> int:
    """Main Function"""
    sum_grade = 0
    subjects = int(input())

    for _ in range(subjects):
        sum_grade += grade(float(input()))

    print((sum_grade/subjects)//0.01/100)

    return 0

if __name__ == "__main__":
    main()

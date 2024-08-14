def calculate_grade(marks):
    total_marks = sum(marks)
    percentage = (total_marks / 500) * 100
    if percentage >= 90:
        return 'Grade A'
    elif percentage >= 80:
        return 'Grade B'
    elif percentage >= 70:
        return 'Grade C'
    elif percentage >= 60:
        return 'Grade D'
    elif percentage >= 40:
        return 'Grade E'
    else:
        return 'Grade F'


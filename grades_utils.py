def calculate_average(grades_list):
    return sum(grades_list) / len(grades_list)
def is_passing(average):
    return average >= 70
def grade_to_letter(average):
    if 91 <= average <= 100:
        return "A"
    elif 81 <= average <= 90:
        return "B"
    elif 71 <= average <= 80:
        return "C"
    elif 61 <= average <= 70:
        return "D"
    else:
        return "F"

# Q7.py
def construct_dict(students, subjects):
    # Using for loops
    student_subject_dict = {}
    for i in range(len(students)):
        student_subject_dict[students[i]] = subjects[i]

    # Using dictionary comprehension
    student_subject_dict_comprehension = {students[i]: subjects[i] for i in range(len(students))}

    return student_subject_dict, student_subject_dict_comprehension

# Example usage
if __name__ == "__main__":
    students = ['Sam', 'Alice', 'Mona']
    subjects = ['Commerce', 'Science', 'Computer']
    dict_loops, dict_comprehension = construct_dict(students, subjects)
    print("Dictionary using for loops:", dict_loops)
    print("Dictionary using comprehension:", dict_comprehension)

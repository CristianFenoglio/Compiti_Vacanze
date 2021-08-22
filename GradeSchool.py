def add_student(name, grade):
    if not grade in students:
        students[grade] = [name]

    else:
        students[grade].append(name)
        students[grade].sort()


def students_in_grade(grade):
    return students[grade]

def all_students():
    all_string = ""
    everybody = []

    for grade in students:
        everybody.append(f"{grade}:{students[grade]}")
    
    everybody.sort()

    for i in everybody:
        all_string += " " + i

    return all_string

def main():
    global students
    students = {}

    add_student("Pippo", 2)
    add_student("Beppe", 3)
    add_student("Paolo", 1)
    add_student("Topolino", 2)
    add_student("Franco", 1)
    add_student("Ariasco", 2)

    print(f"Students in grade: {students_in_grade(2)}")
    
    print(f"All students: {all_students()}")




if __name__ == "__main__":
    main()
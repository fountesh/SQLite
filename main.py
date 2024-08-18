import sqlite3

conn = sqlite3.connect("colage.db")

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    major TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS courses(
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL, 
    instructor TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS student_courses(
    course_id INTEGER ,
    user_id INTEGER,
    FOREIGN KEY (course_id) REFERENCES courser(course_id),
    FOREIGN KEY (user_id) REFERENCES students(id)
)
''')

while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зареєструвати студента на курс")
    print("6. Показати студентів на конкретному курсі")
    print("0. Вийти")

    choice = input("Оберіть опцію (0-6): ")

    if choice == "0":
        break

    elif choice == "1":
        # Додавання нового студента
        _name = input("name: ")
        _age = input("age: ")
        _major = input("major: ")

        cursor = conn.cursor()

        conn.execute('''
        INSERT INTO students(name, age, major)
            VALUES(?, ?, ?);
        ''', (_name, _age, _major))
        conn.commit()

    elif choice == "2":
    # Додавання нового курсу
        course_name = input("course_name: ")
        instructor = input("instructor: ")

        cursor = conn.cursor()

        conn.execute('''
        INSERT INTO courses(course_name, instructor) 
            VALUES(?, ?);
        ''', (course_name, instructor))
        conn.commit()

    elif choice == "3":
        # Показати список студентів
        pass

    elif choice == "4":
        # Показати список курсів
        pass

    elif choice == "5":
        pass
        # Зареєструвати студента на курс

    elif choice == "6":
        # Показати студентів на конкретному курсі
       pass

    

    else:
        print("Некоректний вибір. Будь ласка, введіть число від 1 до 7.")
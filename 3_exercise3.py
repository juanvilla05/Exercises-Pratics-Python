# 1. Library Book Tracker
def add_book(library):
    print("\n--- Add Book ---")
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    while True:
        try:
            pages = int(input("Enter the number of pages: "))
            if pages > 0:
                break
            else:
                print("Number of pages must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer for the number of pages.")

    book = {
        "title": title,
        "author": author,
        "pages": pages
    }
    library.append(book)
    print(f"\nBook '{title}' by {author} added successfully.")
    return library


def find_book(library):
    print("\n--- Find Book ---")
    title_to_find = input("Enter the title of the book to find: ")
    found = False

    for book in library:
        if book["title"].lower() == title_to_find.lower():
            print("\nBook found!")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Pages: {book['pages']}")
            found = True
            break

    if not found:
        print(f"\nBook with title '{title_to_find}' not found.")


def show_books(library):
    print("\n--- Show Books ---")
    if not library:
        print("The library is empty.")
    else:
        for book in library:
            print(f"\n- Title: {book['title']}")
            print(f"  Author: {book['author']}")
            print(f"  Pages: {book['pages']}")


# 2. Student Grade Manager
def add_student(students):
    print("\n--- Add Student ---")
    name = input("Enter the student's name: ")
    while True:
        try:
            student_id = int(input("Enter the student's ID: "))
            break
        except ValueError:
            print("Invalid ID. Please enter an integer.")

    student = {
        "name": name,
        "id": student_id,
        "grades": []
    }
    students.append(student)
    print(f"\nStudent '{name}' with ID {student_id} added successfully.")
    return students


def add_grade(students):
    print("\n--- Add Grade ---")
    student_id = int(input("Enter the ID of the student to add the grade: "))
    grade = float(input("Enter the grade: "))

    for student in students:
        if student["id"] == student_id:
            student["grades"].append(grade)
            print(f"\nGrade {grade} added to {student['name']}.")
            return students

    print(f"\nNo student found with ID {student_id}.")
    return students


def get_average(students):
    print("\n--- Calculate Average ---")
    student_id = int(input("Enter the ID of the student to calculate the average: "))

    for student in students:
        if student["id"] == student_id:
            grades = student["grades"]
            if grades:
                average = sum(grades) / len(grades)
                print(f"\nThe average grade for {student['name']} is: {average:.2f}")
            else:
                print(f"\n{student['name']} has no grades recorded.")
            return

    print(f"\nNo student found with ID {student_id}.")


# 3. Restaurant Menu Editor
def add_dish(menu):
    print("\n--- Add Dish ---")
    name = input("Enter the dish name: ")
    while True:
        try:
            price = float(input("Enter the dish price: "))
            if price > 0:
                break
            else:
                print("Price must be greater than zero.")
        except ValueError:
            print("Invalid price. Please enter a number.")

    available = input("Is the dish available? (yes/no): ").lower() == "yes"

    dish = {
        "name": name,
        "price": price,
        "available": available
    }
    menu.append(dish)
    print(f"\nDish '{name}' added to the menu.")
    return menu


def change_availability(menu):
    print("\n--- Change Availability ---")
    dish_name = input("Enter the name of the dish to change availability: ")

    for dish in menu:
        if dish["name"].lower() == dish_name.lower():
            dish["available"] = not dish["available"]
            availability_str = "available" if dish["available"] else "not available"
            print(f"\nAvailability of '{dish['name']}' changed to: {availability_str}")
            return menu

    print(f"\nNo dish found with name '{dish_name}'.")
    return menu


def total_available_price(menu):
    print("\n--- Calculate Total Available Price ---")
    total = 0
    for dish in menu:
        if dish["available"]:
            total += dish["price"]

    print(f"\nThe total price of available dishes is: {total:.2f}")


# 4. Warehouse Box Counter
def add_box_type(warehouse):
    print("\n--- Add Box Type ---")
    box_type = input("Enter the box type name: ")
    while True:
        try:
            quantity = int(input(f"Enter the initial quantity of '{box_type}' boxes: "))
            if quantity >= 0:
                break
            else:
                print("Quantity must be a non-negative integer.")
        except ValueError:
            print("Invalid quantity. Please enter an integer.")

    warehouse[box_type] = quantity
    print(f"\nBox type '{box_type}' added to the warehouse with {quantity} units.")
    return warehouse


def update_quantity(warehouse):
    print("\n--- Update Quantity ---")
    box_type = input("Enter the name of the box type to update quantity: ")
    while True:
        try:
            change = int(input("Enter the quantity to add (positive) or remove (negative): "))
            break
        except ValueError:
            print("Invalid quantity. Please enter an integer.")

    if box_type in warehouse:
        warehouse[box_type] += change
        print(f"\nQuantity of '{box_type}' updated. New quantity: {warehouse[box_type]}")
    else:
        print(f"\nNo box type found with name '{box_type}'.")
    return warehouse


def has_enough(warehouse):
    print("\n--- Verify Sufficient Quantity ---")
    box_type = input("Enter the name of the box type to verify: ")
    while True:
        try:
            required_quantity = int(input("Enter the required quantity: "))
            if required_quantity >= 0:
                break
            else:
                print("Required quantity must be a non-negative integer.")
        except ValueError:
            print("Invalid quantity. Please enter an integer.")

    if box_type in warehouse:
        if warehouse[box_type] >= required_quantity:
            print(f"\nThere is sufficient quantity of '{box_type}'. Available quantity: {warehouse[box_type]}")
        else:
            print(f"\nThere is not enough quantity of '{box_type}'. Available quantity: {warehouse[box_type]}, required quantity: {required_quantity}")
    else:
        print(f"\nNo box type found with name '{box_type}'.")


# 5. Movie Rating System
def add_movie(movies):
    print("\n--- Add Movie ---")
    title = input("Enter the movie title: ")
    movies[title] = []
    print(f"\nMovie '{title}' added to the system.")
    return movies


def rate_movie(movies):
    print("\n--- Rate Movie ---")
    title = input("Enter the title of the movie to rate: ")
    while True:
        try:
            rating = int(input("Enter the rating (1-5): "))
            if 1 <= rating <= 5:
                break
            else:
                print("Rating must be between 1 and 5.")
        except ValueError:
            print("Invalid rating. Please enter an integer.")

    if title in movies:
        movies[title].append(rating)
        print(f"\nRating {rating} recorded for '{title}'.")
    else:
        print(f"\nNo movie found with title '{title}'.")
    return movies


def average_rating(movies):
    print("\n--- Calculate Average Rating ---")
    title = input("Enter the title of the movie to calculate the average rating: ")

    if title in movies:
        ratings = movies[title]
        if ratings:
            average = sum(ratings) / len(ratings)
            print(f"\nThe average rating for '{title}' is: {average:.2f}")
        else:
            print(f"\n'{title}' has no ratings recorded.")
    else:
        print(f"\nNo movie found with title '{title}'.")


# 6. Online Course Tracker
def register_course(courses):
    print("\n--- Register Course ---")
    title = input("Enter the course title: ")
    duration = input("Enter the course duration: ")
    while True:
        try:
            enrolled = int(input("Enter the number of enrolled students: "))
            if enrolled >= 0:
                break
            else:
                print("The number of enrolled students must be a non-negative integer.")
        except ValueError:
            print("Invalid number. Please enter an integer.")

    course = {
        "title": title,
        "duration": duration,
        "enrolled": enrolled
    }
    courses.append(course)
    print(f"\nCourse '{title}' registered successfully.")
    return courses


def update_enrollment(courses):
    print("\n--- Update Enrollment ---")
    title = input("Enter the title of the course to update enrollment: ")
    while True:
        try:
            change = int(input("Enter the number to add (positive) or remove (negative) from enrollment: "))
            break
        except ValueError:
            print("Invalid number. Please enter an integer.")

    for course in courses:
        if course["title"].lower() == title.lower():
            course["enrolled"] += change
            print(f"\nNumber of enrolled students in '{course['title']}' updated. New total: {course['enrolled']}")
            return courses

    print(f"\nNo course found with title '{title}'.")
    return courses


def filter_by_duration(courses):
    print("\n--- Filter by Duration ---")
    max_duration = input("Enter the maximum duration to filter (e.g., '10 weeks', '3 months'): ")

    print(f"\nCourses with a maximum duration of {max_duration}:")
    for course in courses:
        if course["duration"] <= max_duration:
            print(f"- {course['title']} ({course['duration']})")


# 7. To-Do List Organizer
def add_task(tasks):
    print("\n--- Add Task ---")
    description = input("Enter the task description: ")
    task = {
        "description": description,
        "completed": False
    }
    tasks.append(task)
    print(f"\nTask '{description}' added to the list.")
    return tasks


def complete_task(tasks):
    print("\n--- Complete Task ---")
    description = input("Enter the description of the task you want to mark as completed: ")

    for task in tasks:
        if task["description"].lower() == description.lower():
            task["completed"] = True
            print(f"\nTask '{task['description']}' marked as completed.")
            return tasks

    print(f"\nNo task found with description '{description}'.")
    return tasks


def filter_tasks(tasks):
    print("\n--- Filter Tasks ---")
    option = input("Do you want to see completed or pending tasks? (completed/pending): ").lower()

    print(f"\n{option.capitalize()} tasks:")
    for task in tasks:
        if (option == "completed" and task["completed"]) or \
           (option == "pending" and not task["completed"]):
            print(f"- {task['description']}")


# 8. Digital Wallet
def add_expense(expenses):
    print("\n--- Add Expense ---")
    description = input("Enter the expense description: ")
    while True:
        try:
            amount = float(input("Enter the expense amount: "))
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero.")
        except ValueError:
            print("Invalid amount. Please enter a number.")

    expense = {
        "description": description,
        "amount": amount
    }
    expenses.append(expense)
    print(f"\nExpense of ${amount:.2f} for '{description}' added.")
    return expenses


def total_spent(expenses):
    print("\n--- Calculate Total Spent ---")
    total = 0
    for expense in expenses:
        total += expense["amount"]

    print(f"\nThe total spent is: ${total:.2f}")


def expense_percentages(expenses):
    print("\n--- Calculate Expense Percentages ---")
    total = sum(expense["amount"] for expense in expenses)

    if total == 0:
        print("\nNo expenses recorded to calculate percentages.")
        return

    print("\nExpense percentages:")
    for expense in expenses:
        percentage = (expense["amount"] / total) * 100
        print(f"- {expense['description']}: {percentage:.2f}%")


# 9. Pet Adoption Center
def add_pet(pets):
    print("\n--- Add Pet ---")
    name = input("Enter the pet's name: ")
    species = input("Enter the pet's species: ")
    while True:
        try:
            age = int(input("Enter the pet's age: "))
            if age >= 0:
                break
            else:
                print("Age must be a non-negative integer.")
        except ValueError:
            print("Invalid age. Please enter an integer.")

    pet = {
        "name": name,
        "species": species,
        "age": age
    }
    pets.append(pet)
    print(f"\nPet '{name}' ({species}, {age} years) added.")
    return pets


def find_by_species(pets):
    print("\n--- Find by Species ---")
    species_to_find = input("Enter the species of the pets to find: ")

    print(f"\nPets of the species '{species_to_find}':")
    for pet in pets:
        if pet["species"].lower() == species_to_find.lower():
            print(f"- {pet['name']} ({pet['species']}, {pet['age']} years)")


def older_than(pets):
    print("\n--- Filter Older Than ---")
    while True:
        try:
            min_age = int(input("Enter the minimum age of the pets to show: "))
            if min_age >= 0:
                break
            else:
                print("Minimum age must be a non-negative integer.")
        except ValueError:
            print("Invalid age. Please enter an integer.")

    print(f"\nPets older than {min_age} years:")
    for pet in pets:
        if pet["age"] > min_age:
            print(f"- {pet['name']} ({pet['species']}, {pet['age']} years)")

# 10. Gym Membership System
def register_member(members):
    print("\n--- Register Member ---")
    name = input("Enter the member's name: ")
    plan = input("Enter the membership plan (e.g., 'monthly', 'annual'): ")
    member = {
        "name": name,
        "plan": plan,
        "payment_due": True
    }
    members.append(member)
    print(f"\nMember '{name}' registered with plan '{plan}'.")
    return members


def change_plan(members):
    print("\n--- Change Membership Plan ---")
    name = input("Enter the name of the member whose plan you want to change: ")
    new_plan = input("Enter the new membership plan: ")

    for member in members:
        if member["name"].lower() == name.lower():
            member["plan"] = new_plan
            print(f"\nMembership plan of '{member['name']}' changed to '{new_plan}'.")
            return members

    print(f"\nNo member found with name '{name}'.")
    return members


def unpaid_members(members):
    print("\n--- Show Unpaid Members ---")
    print("\nMembers with unpaid dues:")
    for member in members:
        if not member["payment_due"]:
            print(f"- {member['name']} ({member['plan']})")


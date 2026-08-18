class Course:
    def __init__(self, course_name, duration, fee, category):
        self.course_name = course_name
        self.duration = duration
        self.fee = fee
        self.category = category


class Institute:
    def __init__(self):
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def display_courses(self):
        print("\n--- Course Details ---")
        for course in self.courses:
            print("Course Name:", course.course_name)
            print("Duration:", course.duration)
            print("Fee:", course.fee)
            print("Category:", course.category)
            print("----------------------")


# Create Institute
institute = Institute()

# Add courses
institute.add_course(Course("Python Programming", "3 Months", 5000, "Short-Term"))
institute.add_course(Course("Data Science", "1 Year", 50000, "Long-Term"))
institute.add_course(Course("Web Development", "6 Months", 15000, "Short-Term"))
institute.add_course(Course("Artificial Intelligence", "2 Years", 80000, "Long-Term"))

# Display all courses
institute.display_courses()


#OUTPUT
--- Course Details ---
Course Name: Python Programming
Duration: 3 Months
Fee: 5000
Category: Short-Term
----------------------
Course Name: Data Science
Duration: 1 Year
Fee: 50000
Category: Long-Term
----------------------
Course Name: Web Development
Duration: 6 Months
Fee: 15000
Category: Short-Term
----------------------
Course Name: Artificial Intelligence
Duration: 2 Years
Fee: 80000
Category: Long-Term
----------------------

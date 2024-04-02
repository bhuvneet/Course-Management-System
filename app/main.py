from course_service_impl import CourseServiceImpl

def main():
    # Initialize the Course Management System
    course_service = CourseServiceImpl()

    # Create a new course
    course_id = course_service.create_course("Calculus")

    # Add assignments to the course
    assignment_id1 = course_service.create_assignment(course_id, "Assignment 1")
    assignment_id2 = course_service.create_assignment(course_id, "Assignment 2")

    # Enroll students in the course
    course_service.enroll_student(course_id, "Bhuvneet")
    course_service.enroll_student(course_id, "Rani")
    course_service.enroll_student(course_id, "Ajay")
    course_service.enroll_student(course_id, "Karan")
    course_service.enroll_student(course_id, "Aaron")
    course_service.enroll_student(course_id, "David")

    # Submit assignment 1 for students
    course_service.submit_assignment(course_id, "Bhuvneet", assignment_id1, 85)
    course_service.submit_assignment(course_id, "Rani", assignment_id1, 75)
    course_service.submit_assignment(course_id, "Ajay", assignment_id1, 90)
    course_service.submit_assignment(course_id, "Karan", assignment_id1, 64)
    course_service.submit_assignment(course_id, "Aaron", assignment_id1, 95)
    course_service.submit_assignment(course_id, "David", assignment_id1, 71)
    
    # Submit assignment 2 for students
    course_service.submit_assignment(course_id, "Bhuvneet", assignment_id2, 61)
    course_service.submit_assignment(course_id, "Rani", assignment_id2, 77)
    course_service.submit_assignment(course_id, "Ajay", assignment_id2, 54)
    course_service.submit_assignment(course_id, "Karan", assignment_id2, 71)
    course_service.submit_assignment(course_id, "Aaron", assignment_id2, 73)
    course_service.submit_assignment(course_id, "David", assignment_id2, 62)

    # Get average grades for assignments
    avg_grade1 = course_service.get_assignment_grade_avg(course_id, assignment_id1)
    avg_grade2 = course_service.get_assignment_grade_avg(course_id, assignment_id2)
    print("Average grade for Assignment 1:", avg_grade1)
    print("Average grade for Assignment 2:", avg_grade2)

    # Get average grade for a student
    avg_student_grade = course_service.get_student_grade_avg(course_id, "Bhuvneet")
    print("Average grade for Bhuvneet:", avg_student_grade)

    # Get top-performing students
    top_students = course_service.get_top_five_students(course_id)
    print("Top-performing students:", top_students)

if __name__ == "__main__":
    main()
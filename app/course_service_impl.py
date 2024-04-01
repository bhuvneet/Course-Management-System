from typing import Any, List
from course_service import CourseService

class CourseServiceImpl(CourseService):
    # this is the constuctor of the class which initializes the dictionaries
    def __init__(self):
        self.courses        = {}
        self.assignments    = {}
        self.enrollments    = {}
        self.grades         = {}
    
    # this method returns the list of courses
    def get_courses(self) -> List[str]:
        return list(self.courses.values())
    
    # this method is called to get course by it's ID
    def get_course_by_id(self, course_id: int) -> str:
        return self.courses.get(course_id, "Course not found")
    
    # this method is called to create a course and return it's ID
    def create_course(self, course_name: str) -> int:
        course_id = len(self.courses) + 1
        self.courses[course_id] = course_name
        return course_id
    
    # this method is called to delete course from the courses dictionary
    def delete_course(self, course_id) -> bool:
        # find course and remove it from dictionary
        if course_id in self.courses:
            del self.courses[course_id]
            return True
        return False
    
    def create_assignment(self, course_id, assignment_name) -> int:
            # check if assignment is in the courses dictionary
            # if not, add it to the dictionary
            if course_id not in self.assignments:
                self.assignments[course_id] = {}
            assignment_id = len(self.assignments[course_id]) + 1
            self.assignments[course_id][assignment_id] = assignment_name
            return assignment_id
    
    def enroll_student(self, course_id, student_id) -> bool:
        if course_id not in self.enrollments:
            self.enrollments[course_id] = set()
        self.enrollments[course_id].add(student_id)
        return True
    
    # this method is called when a student drops out of a course
    def dropout_student(self, course_id, student_id) -> bool:
        if course_id in self.enrollments and student_id in self.enrollments[course_id]:
            self.enrollments[course_id].remove(student_id)
            return True
        return False    
    
    def submit_assignment(self, course_id, student_id, assignment_id, grade: int) -> bool:
        if course_id in self.enrollments and student_id in self.enrollments[course_id]:
            if course_id not in self.grades:
                self.grades[course_id] = {}
            if assignment_id not in self.grades[course_id]:
                self.grades[course_id][assignment_id] = {}
            self.grades[course_id][assignment_id][student_id] = grade
            return True
        return False
    
    def get_assignment_grade_avg(self, course_id, assignment_id) -> int:
        if course_id in self.grades and assignment_id in self.grades:
            grades = [self.grades[course_id][assignment_id].values()
                for assignment_id in self.grades[course_id]]
            return sum(grades) // len(grades) if grades else 0
        return 0
    
    def get_student_grade_avg(self, course_id, student_id) -> int:
        if course_id in self.grades:
            student_grades = [self.grades[course_id][assignment_id].get(student_id, 0)
                              for assignment_id in self.grades[course_id]]
            return sum(student_grades) // len(student_grades) if student_grades else 0
        return 0
    
    def get_top_five_students(self, course_id) -> List[int]:
        if course_id in self.grades:
            avg_grades = {}
            for assignment_id in self.grades[course_id]:
                for student_id in self.grades[course_id][assignment_id]:
                    if student_id not in avg_grades:
                        avg_grades[student_id] = 0
                    avg_grades[student_id] += self.grades[course_id][assignment_id][student_id]
            sorted_students = sorted(avg_grades.items(), key=lambda x: x[1], reverse=True)
            return [student[0] for student in sorted_students[:5]]
        return []

# for testing
course_service = CourseServiceImpl()

course_list = course_service.get_courses()
print("Course list: ", course_list)
    
    
    
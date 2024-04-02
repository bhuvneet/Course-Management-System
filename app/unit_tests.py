import unittest

# Import CourseServiceImpl class
from course_service_impl import CourseServiceImpl

# this class tests and verifies the following methods of CourseServiceImpl class:
# - create_course
# - get_course_by_id
# - course_list
# - enroll_students
# - create_assignment
# - submit_assignment

class UnitTestCourseServiceImp(unittest.TestCase):
    def setUp(self):
        self.course_service = CourseServiceImpl()
        
    def test_create_course(self):
        course_id =  self.course_service.create_course("Mathetmatics")
        self.assertEqual(course_id, 1)
        
        course_id =  self.course_service.create_course("English")
        self.assertEqual(course_id, 2)
        
    def test_get_course_by_id(self):
        self.course_service.create_course("Mathematics")
        course_name = self.course_service.get_course_by_id(1)
        self.assertEqual(course_name, "Mathematics")
        
        # course not found
        course_name = self.course_service.get_course_by_id(3)
        
    def test_course_list(self):
        course_list = self.course_service.get_courses()
        
    def test_enroll_student(self):
        # enroll students
        student_id = 1
        self.course_service.enroll_student(1, student_id)
        student_id = 2
        self.course_service.enroll_student(1, student_id)
        student_id = 3
        self.course_service.enroll_student(1, student_id)
        student_id = 4
        self.course_service.enroll_student(1, student_id)
        
    def test_create_assignment(self):
        self.course_service.create_assignment(1, "Assignment 1")
        
    def test_submit_assignment(self):
        course_id=1
        assignment_id="Assignment 1"
        self.course_service.submit_assignment(course_id, student_id=1, assignment_id=assignment_id, grade=85)
        self.course_service.submit_assignment(course_id, student_id=2, assignment_id=assignment_id, grade=64)
        self.course_service.submit_assignment(course_id, student_id=3, assignment_id=assignment_id, grade=71)
        self.course_service.submit_assignment(course_id, student_id=4, assignment_id=assignment_id, grade=78)
        

if __name__ == '__main__':
    unittest.main()
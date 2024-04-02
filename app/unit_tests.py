import unittest

# Import CourseServiceImpl class
from course_service_impl import CourseServiceImpl

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
        
    def enroll_student(self):
        enroll_std = self.course_service.enroll_student(1, 1)
        

if __name__ == '__main__':
    unittest.main()
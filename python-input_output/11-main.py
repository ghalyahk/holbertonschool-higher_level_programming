#!/usr/bin/python3
"""Test Student class"""

from student_11 import Student

# إنشاء طالب
student_1 = Student("John", "Doe", 23)
print("Original student JSON:")
print(student_1.to_json())

# إنشاء طالب وهمي
new_student = Student("Fake", "Fake", 89)
print("\nFake student before reload:")
print(new_student.to_json())

# إعادة تحميل بيانات الطالب الأول على الطالب الوهمي
new_student.reload_from_json(student_1.to_json())
print("\nFake student after reload_from_json:")
print(new_student.to_json())

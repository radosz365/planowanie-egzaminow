import unittest
import re
import pandas as pd

# Load the CSV file
data_path = 'dataset1000.csv'
database = pd.read_csv(data_path).to_dict(orient='records')

class TestDatabase(unittest.TestCase):

    def test_unique_rows(self):
        # Test for unique rows in the database
        rows = [tuple(row.items()) for row in database]
        self.assertEqual(len(rows), len(set(rows)), "Not all rows are unique.")

    def test_non_empty_values(self):
        # Test for missing values
        for row in database:
            for key, value in row.items():
                self.assertIsNotNone(value, f"Missing value in column {key}")
                self.assertNotEqual(value, "", f"Empty value in column {key}")

    def test_course_format(self):
        # Test for course name format
        for row in database:
            course = row["course"]
            self.assertIsInstance(course, str, "Course name should be a string")

    def test_lecturer_format(self):
        # Test for lecturer name format
        lecturer_pattern = re.compile(r"^(Dr|Prof|Mgr|Dr hab)\.\s+[A-Za-z]+\s+[A-Za-z]+$")
        for row in database:
            lecturer = row["lecturer"]
            self.assertRegex(lecturer, lecturer_pattern, "Incorrect lecturer name format")

    def test_group_format(self):
        # Test for group code format (e.g., XX.XX.XXX.XXXX.XXX)
        group_pattern = re.compile(r"^[A-Z]{3}\.[A-Z]{2}[0-9]\.[A-Z]{3}\.[0-9]{4}\.[A-Z]{3}$")
        for row in database:
            group = row["group"]
            self.assertRegex(group, group_pattern, "Incorrect group format")

    def test_classroom_format(self):
        # Test for classroom format (e.g., H101)
        classroom_pattern = re.compile(r"^[A-Z][0-9]{3}$")
        for row in database:
            classroom = row["classroom"]
            self.assertRegex(classroom, classroom_pattern, "Incorrect classroom format")

    #def test_unique_classroom_per_course(self):
        # Optional: Check if each classroom is assigned to only one course
        #classrooms = [row["classroom"] for row in database]
        #self.assertEqual(len(classrooms), len(set(classrooms)), "Classrooms are assigned to multiple courses")

if __name__ == "__main__":
    unittest.main()

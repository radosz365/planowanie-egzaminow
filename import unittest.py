import unittest
import re

# Sample data representing the database
database = [
    {
        "course": "Międzynarodowe zarządzanie finansami",
        "lecturer": "Dr. Anna Lewandowska",
        "group": "TNW.AG3.GVN.7332.DQB",
        "classroom": "H236",
    },
    {
        "course": "Budowanie marki online",
        "lecturer": "Mgr. Tomasz Nowakiewicz",
        "group": "BFN.OF8.PWR.0279.RWQ",
        "classroom": "E353",
    },
    {
        "course": "Modelowanie finansowe",
        "lecturer": "Prof. Marek Wójcik",
        "group": "OOG.CU9.LTX.5149.CYJ",
        "classroom": "B135",
    },
    {
        "course": "Tworzenie treści cyfrowych",
        "lecturer": "Dr hab. Katarzyna Kamiński",
        "group": "QSC.TR2.PPG.1283.PVD",
        "classroom": "H251",
    },
    {
        "course": "Zarządzanie polem namiotowym",
        "lecturer": "Mgr. Jan Wiśniewski",
        "group": "SZY.OR3.WYO.6406.MXZ",
        "classroom": "H101",
    },
    {
        "course": "Transformacja cyfrowa",
        "lecturer": "Prof. Zofia Kowalska",
        "group": "TJV.BQ7.GMX.2994.NOH",
        "classroom": "B384",
    },
    {
        "course": "Zarządzanie zmianą",
        "lecturer": "Dr hab. Andrzej Wójcik",
        "group": "VVK.PE9.VAU.7412.MSK",
        "classroom": "E186",
    },
    {
        "course": "Zarządzanie innowacjami",
        "lecturer": "Dr. Anna Zielińska",
        "group": "SGT.TY6.GYI.6888.DBD",
        "classroom": "C320",
    },
    {
        "course": "Studia kulturowe",
        "lecturer": "Dr hab. Ewa Zielińska",
        "group": "UIK.YG2.MZB.0483.FSE",
        "classroom": "B198",
    },
    {
        "course": "Zarządzanie transportem kolejowym",
        "lecturer": "Mgr. Maria Kamińska",
        "group": "JSI.BX2.UAJ.4340.SGP",
        "classroom": "D280",
    },
    {
        "course": "Ekonomia nieruchomości",
        "lecturer": "Mgr. Zofia Kowalska",
        "group": "CXC.RY5.YNN.8006.FCS",
        "classroom": "C379",
    },
]


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
        lecturer_pattern = re.compile(
            r"^(Dr|Prof|Mgr|Dr hab)\.\s+[A-Za-z]+\s+[A-Za-z]+$"
        )
        for row in database:
            lecturer = row["lecturer"]
            self.assertRegex(
                lecturer, lecturer_pattern, "Incorrect lecturer name format"
            )

    def test_group_format(self):
        # Test for group code format (e.g., XX.XX.XXX.XXXX.XXX)
        group_pattern = re.compile(
            r"^[A-Z]{3}\.[A-Z]{2}[0-9]\.[A-Z]{3}\.[0-9]{4}\.[A-Z]{3}$"
        )
        for row in database:
            group = row["group"]
            self.assertRegex(group, group_pattern, "Incorrect group format")

    def test_classroom_format(self):
        # Test for classroom format (e.g., H101)
        classroom_pattern = re.compile(r"^[A-Z][0-9]{3}$")
        for row in database:
            classroom = row["classroom"]
            self.assertRegex(classroom, classroom_pattern, "Incorrect classroom format")

    def test_unique_classroom_per_course(self):
        # Optional: Check if each classroom is assigned to only one course
        classrooms = [row["classroom"] for row in database]
        self.assertEqual(
            len(classrooms),
            len(set(classrooms)),
            "Classrooms are assigned to multiple courses",
        )


if __name__ == "__main__":
    unittest.main()

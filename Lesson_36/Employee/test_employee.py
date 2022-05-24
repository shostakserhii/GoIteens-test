import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        self.emp_1 = Employee('Vova', 'Zelenyi', 3000)
        self.emp_2 = Employee('Borya', 'Johnsonyk', 10000)
        print('SetUP')

    def tearDown(self):
        print('TearDown')
        print()

    def test_email(self):
        """Test email."""
        print('Testing email')
        self.assertEqual(self.emp_1.email, 'Vova.Zelenyi@email.com')
        self.assertEqual(self.emp_2.email, 'Borya.Johnsonyk@email.com')

        self.emp_1._first = 'Kolya'
        self.emp_2._first = 'Serhii'

        self.assertEqual(self.emp_1.email, 'Kolya.Zelenyi@email.com')
        self.assertEqual(self.emp_2.email, 'Serhii.Johnsonyk@email.com')

    def test_fullname(self):
        """Test fullname to return fullname."""
        print('Testing Fullname')
        self.assertEqual(self.emp_1.fullname, 'Vova Zelenyi')
        self.assertEqual(self.emp_2.fullname, 'Borya Johnsonyk')

        self.emp_1._first = 'Kolya'
        self.emp_2._first = 'Serhii'

        self.assertEqual(self.emp_1.fullname, 'Kolya Zelenyi')
        self.assertEqual(self.emp_2.fullname, 'Serhii Johnsonyk')

    def test_apply_raise(self):
        """Test apply raise to increase pay."""
        print('Testing Apply_Raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1._pay, 3150)
        self.assertEqual(self.emp_2._pay, 10500)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Successfully found record!'
            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Zelenyi/May')
            self.assertEqual(schedule, 'Successfully found record!')

            mocked_get.return_value.ok = False
            schedule_2 = self.emp_2.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Johnsonyk/May')
            self.assertEqual(schedule_2, 'Bad Response!')


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest import TestCase

class TestClass1(TestCase):
    @classmethod
    def setUpClass(cls):
        print("Set up class method. Runs once before all test cases")

    def setUp(self):
        print("Set up method. Runs before every test case")

    def test_class1_method_a(self):
        print("test class:1 method: A")

    def test_class1_method_b(self):
        print("test class:1 method: B")

    def tearDown(self):
        print("Teardown method. Runs after every test case")

    @classmethod
    def tearDownClass(cls):
        print("Teardown class method. Runs once after all test cases")

if __name__ == '__main__':
     unittest.main()
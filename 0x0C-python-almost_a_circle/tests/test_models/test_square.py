#!/usr/bin/python3

"""Unittest for square"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import io
from contextlib import redirect_stdout


class Test_Square(unittest.TestCase):
    def test_00_case_base_success(self):
        new_obj = Square(5)
        self.assertEqual(new_obj.size, 5)

    def test_00_case_all_args_success(self):
        new_obj = Square(15, 4, 7, 15)
        self.assertEqual(new_obj.x, 4)

    def test_00_case_all_args_fail(self):
        with self.assertRaises(TypeError):
            new_obj = Square(15, 4, "40", 15)

    def test_00_case_all_args_fail_negatives(self):
        with self.assertRaises(ValueError):
            new_obj = Square(-15, -5, -2, 8)

    def test_00_case_all_args_fail_zero(self):
        with self.assertRaises(ValueError):
            new_obj = Square(0, 0, 0, 8)

    def test_01_case_fail_01_without_args(self):
        with self.assertRaises(TypeError):
            new_obj = Square()

    def test_02_setter_size_height_success(self):
        new_obj = Square(8, 5, 3, 26)
        new_obj.size = 40
        self.assertEqual(new_obj.height, 40)

    def test_02_setter_size_width_success(self):
        new_obj = Square(8, 5, 3, 26)
        new_obj.size = 40
        self.assertEqual(new_obj.width, 40)

    def test_02_setter_size_fail(self):
        new_obj = Square(8, 5, 3, 26)
        with self.assertRaises(ValueError):
            new_obj.size = -8

    def test_02_setter_x_success(self):
        new_obj = Square(8, 5, 3, 26)
        new_obj.x = 40
        self.assertEqual(new_obj.x, 40)

    def test_02_setter_y_success(self):
        new_obj = Square(8, 5, 3, 26)
        new_obj.y = 81
        self.assertEqual(new_obj.y, 81)

    def test_02_setter_x_fail(self):
        new_obj = Square(8, 5, 3, 26)
        with self.assertRaises(ValueError):
            new_obj.x = -8

    def test_02_setter_y_fail(self):
        new_obj = Square(8, 5, 3, 26)
        with self.assertRaises(ValueError):
            new_obj.y = -8

    def test_03_area_success(self):
        new_obj = Square(7, 5, 3, 26)
        self.assertEqual(new_obj.area(), 49)

    def test_03_area_fail(self):
        new_obj = Square(8, 5, 3, 26)
        self.assertNotEqual(new_obj.area(), 49)

    def test_dimensions(self):
        """ check if w & h dimensions are validate """
        rDim = Square(5)
        self.assertEqual(rDim.width, 5)
        self.assertEqual(rDim.height, 5)
        rDim.width = 10
        rDim.height = 3
        self.assertEqual(rDim.width, 10)
        self.assertEqual(rDim.height, 3)
        rDim.width = 0x0F
        rDim.height = 0x0F
        self.assertEqual(rDim.width, 15)
        self.assertEqual(rDim.height, 15)
        self.assertRaises(TypeError, Square, 'Cinco', 10)
        self.assertRaises(TypeError, Square, 10, '5')
        self.assertRaises(TypeError, Square, None, 10)
        self.assertRaises(TypeError, Square, 10, None)
        self.assertRaises(TypeError, Square, True, 10)
        self.assertRaises(TypeError, Square, 10, True)
        self.assertRaises(ValueError, Square, -5, 10)
        self.assertRaises(ValueError, Square, 5, -10)
        self.assertRaises(ValueError, Square, 0)

    def test_update_args(self):
        """ check the update function with 'no-keyword' arguments """
        rUpdateArg = Square(5)
        rUpdateArg.update(6)
        self.assertEqual(rUpdateArg.id, 6)
        rUpdateArg.update(10, 5)
        self.assertEqual(rUpdateArg.id, 10)
        self.assertEqual(rUpdateArg.area(), 5 * 5)
        rUpdateArg.update(10, 10, 10)
        self.assertEqual(rUpdateArg.area(), 10 * 10)
        self.assertEqual(rUpdateArg.x, 10)
        rUpdateArg.update(10, 10, 10, 10)
        self.assertEqual(rUpdateArg.y, 10)
        self.assertEqual(rUpdateArg.id, 10)
        self.assertEqual(rUpdateArg.area(), 100)
        self.assertEqual(rUpdateArg.x, 10)

    def test_update_kwargs(self):
        """ check update function with 'key-worded' argument """
        rUpdateKarg = Square(5)
        rUpdateKarg.update(id=6)
        self.assertEqual(rUpdateKarg.id, 6)
        rUpdateKarg.update(id=10, size=5)
        self.assertEqual(rUpdateKarg.id, 10)
        self.assertEqual(rUpdateKarg.area(), 5 * 5)
        rUpdateKarg.update(id=10, size=7)
        self.assertEqual(rUpdateKarg.id, 10)
        self.assertEqual(rUpdateKarg.area(), 7 * 7)
        rUpdateKarg.update(id=10, size=7, x=9)
        self.assertEqual(rUpdateKarg.id, 10)
        self.assertEqual(rUpdateKarg.area(), 7 * 7)
        self.assertEqual(rUpdateKarg.x, 9)
        rUpdateKarg.update(y=14, id=6, x=19, size=3)
        self.assertEqual(rUpdateKarg.id, 6)
        self.assertEqual(rUpdateKarg.area(), 9)
        self.assertEqual(rUpdateKarg.x, 19)
        self.assertEqual(rUpdateKarg.y, 14)

    def test_base_case(self):
        """Checks the base case"""
        s1 = Square(10, 2, 1)
        d = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, d)

    def test_if_dictionary(self):
        """checks if the result is a dictionary"""
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertIsInstance(s1_dictionary, dict)

    def test_base_case(self):
        """checks the correct output for other square"""
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        f = io.StringIO()
        with redirect_stdout(f):
            print(s2)
        self.assertEqual(f.getvalue(), "[Square] (29) 2/1 - 10\n")

    def test_diferents_squares(self):
        """checks that squares are differents"""
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        f = io.StringIO()
        with redirect_stdout(f):
            print(s1 == s2)
        self.assertEqual(f.getvalue(), "False\n")

    def test_json_file(self):
        """Check the json file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(14, 2, 5, 8)
        dictionary = r1.to_dictionary()
        dictionary1 = r2.to_dictionary()
        ss = [dictionary, dictionary1]
        json_dictionary = Square.to_json_string(ss)
        self.assertEqual(ss, json.loads(json_dictionary))

    def test_argument_passed(self):
        """check when a argument is pased"""
        s1 = Square(10, 2, 1)
        with self.assertRaises(TypeError):
            dictionary = s1.to_dictionary(32)

    def test_unexpected_keyword(self):
        """check a keyword argument is passed"""
        s1 = Square(10, 2, 1)
        with self.assertRaises(TypeError):
            dictionary = s1.to_dictionary(width=2)

    def test_json(self):
        """test of Base.to_json_string([ { 'id': 12 }]) returning a string"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(isinstance(json_dictionary, str))

    def test_args_order(self):
        """Checks correct order of arguments"""
        f = io.StringIO()
        s = "[Square] (10) 10/10 - 89"
        r1 = Square(10, 10, 10, 10)
        r1.update(size=89)
        with redirect_stdout(f):
            print(r1, end="")
        self.assertEqual(f.getvalue(), s)

        r1.update(size=1, x=2)
        f = io.StringIO()
        s = "[Square] (10) 2/10 - 1"
        with redirect_stdout(f):
            print(r1, end="")
        self.assertEqual(f.getvalue(), s)

        r1.update(y=1, size=2, x=3, id=89)
        f = io.StringIO()
        s = "[Square] (89) 3/1 - 2"
        with redirect_stdout(f):
            print(r1, end="")
        self.assertEqual(f.getvalue(), s)

        r1.update(x=1, size=2, y=3)
        f = io.StringIO()
        s = "[Square] (89) 1/3 - 2"
        with redirect_stdout(f):
            print(r1, end="")
        self.assertEqual(f.getvalue(), s)

    def test_args_valid_types_str(self):
        """Check valid types, str"""
        r1 = Square(10, 10, 10)
        s = "string"
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(43, 43, 32, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_list(self):
        """Check valid types, str"""
        r1 = Square(10, 10, 10)
        s = [32, 32]
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(43, 43, 32, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_tuple(self):
        """Check valid types, tuple"""
        r1 = Square(10, 10, 10)
        s = (2, 3)
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(43, 43, 32, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_area(self):
        """Test for area"""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
        s1.update(2, 4)
        self.assertEqual(s1.area(), 16)

    def test_wrong_keywords(self):
        """Test keywords"""
        s1 = Square(10, 2, 1)
        s1.update(key=23, school=32)
        self.assertEqual(getattr(s1, "key", 0), 23)
        self.assertEqual(getattr(s1, "school", 0), 32)

    def test_args_value_zero_1(self):
        """Check valid value"""
        msg = " must be > 0"
        err = ValueError
        try:
            Square(-10)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)

        try:
            Square(0)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)

        msg = " must be >= 0"
        try:
            Square(10, -2)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            Square(10, 2, -3)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

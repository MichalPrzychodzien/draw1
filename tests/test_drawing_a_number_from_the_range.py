from drawing_a_number_from_the_range.drawings import Drawings
from unittest import TestCase


class TestDrawingANumberFromTheRange(TestCase):
    def test_init(self):
        drawings = Drawings()
        self.assertEqual(drawings.draw_number, 0)
        self.assertNotEqual(drawings.draw_number, 1)
        self.assertIsNone(drawings.user_number)

    def test_drawing1(self):
        drawings = Drawings()
        drawings.drawing1()
        self.assertEqual(drawings.user_number, 1)
        self.assertEqual(drawings.random_number, None)
        self.assertEqual(drawings.chances, 0)
        self.assertEqual(drawings.start, drawings.end)
        self.assertNotEqual(drawings.user_number, 2)
        self.assertNotEqual(drawings.random_number, 3)
        self.assertNotEqual(drawings.chances, 4)
        self.assertNotEqual(drawings.start, 2)
        self.assertNotEqual(drawings.end, -1)





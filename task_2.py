# https://adventofcode.com/2021/day/2

import unittest


file_name = 'task_2_input.txt'

with open(file_name, 'r') as f:
    directions = [line.split() for line in f.read().splitlines()]


def multiply_position(directions):
    horizontal, vertical = 0, 0
    for direction, num in directions:
        num = int(num)
        if direction == 'forward':
            horizontal += num
        elif direction == 'down':
            vertical += num
        elif direction == 'up':
            vertical -= num
    return horizontal * vertical


def multiply_aim_position(directions):
    horizontal, depth, aim = 0, 0, 0
    for direction, num in directions:
        num = int(num)
        if direction == 'forward':
            horizontal += num
            depth += aim * num
        elif direction == 'down':
            aim += num
        elif direction == 'up':
            aim -= num
    return horizontal * depth


class TestMultiplyPosition(unittest.TestCase):
    def test_simple(self):
        file_name = 'task_2_input_test.txt'
        with open(file_name, 'r') as f:
            directions = [line.split() for line in f.read().splitlines()]
        self.assertEqual(multiply_position(directions), 150)

    def test_multiply_aim_position(self):
        file_name = 'task_2_input_test.txt'
        with open(file_name, 'r') as f:
            directions = [line.split() for line in f.read().splitlines()]
        self.assertEqual(multiply_aim_position(directions), 900)


if __name__ == '__main__':
    print(multiply_position(directions))
    print(multiply_aim_position(directions))
    unittest.main()

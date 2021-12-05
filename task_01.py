# https://adventofcode.com/2021/day/1
# count the measurements which are larger than the previous measurement

import unittest
from random import randint

file_name = 'task_1_input.txt'


def line_counter(file_name):
    f = open(file_name, 'r')
    # making two counters: one will be the control, second will be the main
    control_counter, counter = 1, 0

    # read the first line
    line = f.readline()
    if not line:
        return 0, 0
    line1 = line

    # in circle read the lines and count the increased measures until the end
    while True:
        line = f.readline()
        if not line:
            break
        if int(line) > int(line1):
            counter += 1
        line1 = line
        control_counter += 1

    f.close()

    return control_counter, counter


def sum_line_counter(file_name):
    f = open(file_name, 'r')
    counter = 0
    num_list = []

    while True:
        line = f.readline()
        if not line:
            break
        num_list.append(int(line))

    f.close()

    for i in range(0, len(num_list)-3):
        sum1 = sum(num_list[i:i+3])
        sum2 = sum(num_list[i+1:i+4])
        if sum2 > sum1:
            counter += 1
        sum1 = sum2

    return counter


def day1_pt2(file_name):
    with open(file_name, 'r') as f:
        nums = [int(i) for i in f.read().splitlines()]
    return sum(nums[i] > nums[i-3] for i in range(3, len(nums)))


class TestLineCounter(unittest.TestCase):
    def test_line_counter(self):
        result = (10, 7)
        self.assertEqual(line_counter('task_1_input_test.txt'), result)

    def test_sum_line_counter(self):
        result = 5
        self.assertEqual(sum_line_counter('task_1_input_test.txt'), result)

    def day1_pt2(self):
        result = 5
        self.assertEqual(day1_pt2('task_1_input_test.txt'), result)

    def test_my_vs_his(self):
        filename = 'temp.txt'
        with open(filename, 'w') as t:
            for _ in range(2000):
                t.write(f'{str(randint(1, 2000))}\n')
        self.assertEqual(sum_line_counter(filename), day1_pt2(filename))


if __name__ == '__main__':
    print(line_counter(file_name))
    print(sum_line_counter(file_name))
    print(day1_pt2(file_name))

    unittest.main()

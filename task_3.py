# https://adventofcode.com/2021/day/3

"""
NOTE:
two good ways to reverse bits in str:

''.join('1' if x == '0' else '0' for x in '100')
'100'.replace('1', '2').replace('0', '1').replace('2', '0')

but second much faster

"""

from statistics import mode, multimode
import unittest


file_name = 'task_3_input.txt'
with open(file_name, 'r') as f:
    bite_list = [line for line in f.read().splitlines()]

test_file_name = 'task_3_input_test.txt'
with open(test_file_name, 'r') as tf:
    test_bite_list = [line for line in tf.read().splitlines()]


def power_consumption_of_the_submarine(bits_list):
    temp_num = ''
    gamma_rate = ''
    for bit_index in range(len(bits_list[0])):
        temp_num = ''  # temp var init
        for line_index in range(len(bits_list)):
            # first - collect the bits from positions
            temp_num = ''.join(temp_num + bits_list[line_index][bit_index])

        # take the most common of the temp_num (using statistics.mode) and add its to gamma_rate
        gamma_rate = ''.join(gamma_rate + mode(temp_num))

    # to find epsilon - reverse 1 and 0:
    epsilon_rate = gamma_rate.replace('1', '2').replace('0', '1').replace('2', '0')

    # convert binary str to decimal int
    gamma_rate = int(gamma_rate, base=2)
    epsilon_rate = int(epsilon_rate, base=2)

    # return all just for debug, all we need is the multiply
    return gamma_rate, epsilon_rate, gamma_rate * epsilon_rate


def life_support_rate(bite_list):
    def ox_gen_rate(bites, pos=0):
        if len(bites) == 1:
            return bites[0]

        # collect bites in position
        bit_str = ''
        for bite in bites:
            bit_str = ''.join(bit_str + bite[pos])

        # finding the most common, if equal - take 1
        mmode = multimode(bit_str)
        most_common = mmode[0] if len(mmode) == 1 else '1'

        # filter bite list by most common
        bites = list(filter(lambda x: x[pos] == most_common, bites))

        return ox_gen_rate(bites, pos+1) if pos < (len(bites[0])-1) else ox_gen_rate(bites)

    ox_gen_rate_bin = ox_gen_rate(bite_list)

    return int(ox_gen_rate_bin, base=2)


def co2_rate(bite_list):
    def co2_rate_helper(bites, pos=0):
        if len(bites) == 1:
            return bites[0]

        # collect bites in position
        bit_str = ''
        for bite in bites:
            bit_str = ''.join(bit_str + bite[pos])

        # finding the most rare, but i skip the instruction about what i should do when i found equally occurring
        # its not right, but lucky me - its working
        most_rare = min(set(bit_str), key=bit_str.count)

        # filter bite list by most common
        bites = list(filter(lambda x: x[pos] == most_rare, bites))

        return co2_rate_helper(bites, pos+1) if pos < (len(bites[0])-1) else co2_rate_helper(bites)

    co2_rate_bin = co2_rate_helper(bite_list)

    return int(co2_rate_bin, base=2)


class TestPowerConsumption(unittest.TestCase):
    def test_gamma_rate(self):
        self.assertEqual(power_consumption_of_the_submarine(test_bite_list)[0], 22)

    def test_epsilon_rate(self):
        self.assertEqual(power_consumption_of_the_submarine(test_bite_list)[1], 9)

    def test_power_consumption_of_the_submarine(self):
        self.assertEqual(power_consumption_of_the_submarine(test_bite_list)[2], 198)

    def test_ox_gen_rate(self):
        self.assertEqual(life_support_rate(test_bite_list), 23)

    def test_co2_rate(self):
        self.assertEqual(co2_rate(test_bite_list), 10)

    def test_ox_co2_rate_mult(self):
        self.assertEqual(life_support_rate(test_bite_list) * co2_rate(test_bite_list), 230)


if __name__ == '__main__':
    print(power_consumption_of_the_submarine(bite_list))
    print(life_support_rate(bite_list) * co2_rate(bite_list))
    unittest.main()

# https://adventofcode.com/2021/day/4

import unittest
from typing import List, Optional


class BingoBoard:
    def __init__(self, board: List[List[List[Optional[str]]]]):
        if isinstance(board, list) \
                and isinstance(board[0], list) \
                and isinstance(board[0][0], list) \
                and isinstance(board[0][0][0], str)\
                and isinstance(board[0][0][1], bool):
            self.board = board
        else:
            raise TypeError('Bingo Board format must be: List[List[List[str, bool]]]')

    def __repr__(self):
        return f'<BingoObj: {self.board[0][:2]}...>'

    # mark num to true in board
    def mark_num(self, num: str):
        """
        find num in board and mark it as True
        :param num: num to find
        :return: bool
        """

        if not isinstance(num, str):
            num = str(num)
        for row in self.board:
            for col in row:
                # if find the num - mark as True and return True
                if num in col:
                    col[1] = True
                    return True
        # else - return False
        return False

    # win check
    def win_check(self):
        """
        search for row or column all True
        :return: bool
        """

        # row check
        for line in self.board:
            if all(mark for num, mark in line):
                return True

        # column check
        if any(all(self.board[j][i][1] for j in range(5)) for i in range(5)):
            return True
        return False

    # take sum of unmarked elements
    def sum_unmarked(self):
        # make list of unmarked elements, int them, then - return the sum
        return sum(map(int, [num for line in self.board for num, mark in line if not mark]))


file_name = 'task_4_input.txt'
test_file_name = 'task_4_input_test.txt'


# prepare the data. Returns move list + row list
def source_preparing(file_name):
    with open(file_name, 'r') as f:
        row_list = [line for line in f.read().splitlines()]

    # remove empty strings
    for elem in row_list:
        if elem == '':
            row_list.remove(elem)

    # take first string as move list and remove it from row_list
    move_list = row_list.pop(0).split(',')

    return move_list, row_list


# make the list of bingo boards from row list
def make_bingo_list(row_list):
    boards = []  # list of bingo boards objects

    boards_count = len(row_list)//5
    for _ in range(boards_count):
        # take first 5 rows and make list of lists of lists, then remove them from row_list
        # and append as bingo board in list
        board = [[[num, False] for num in row_list[i].split()] for i in range(5)]
        boards.append(BingoBoard(board))
        del row_list[:5]

    return boards


def find_winner(moves, boards):
    for move in moves:
        for board in boards:
            board.mark_num(move)
            if board.win_check():
                return int(move), board.sum_unmarked(), boards.index(board)


def find_last_winner(moves, boards):
    last_move, sum_unmark, win_board, new_boards = 0, 0, 0, []
    for move in moves:
        for board in boards:
            # mark num in boards
            board.mark_num(move)

            # check for win
            if board.win_check():
                last_move, sum_unmark, win_board = int(move), board.sum_unmarked(), boards.index(board)
                continue  # not append win board into list - this is correct remove board

                # code before we can replace by function that we use to find the one winner
                
            new_boards.append(board)

        boards = new_boards[:]  # make copy, not link
        new_boards.clear()  # clear temp board list

    return last_move, sum_unmark


class TestBingo(unittest.TestCase):
    def test_find_winner(self):
        move_list, row_list = source_preparing(test_file_name)
        bingo_list = make_bingo_list(row_list)
        winner = find_winner(move_list, bingo_list)

        self.assertEqual(winner, (24, 188, 2))
        self.assertEqual(winner[0] * winner[1], 4512)

    def test_last_winner(self):
        move_list, row_list = source_preparing(test_file_name)
        bingo_list = make_bingo_list(row_list)
        last_winner = find_last_winner(move_list, bingo_list)

        self.assertEqual(last_winner, (13, 148))


if __name__ == '__main__':
    # TESTS
    unittest.main(exit=False)

    # PREPARING
    move_list, row_list = source_preparing(file_name)
    bingo_list = make_bingo_list(row_list)

    # PART 1
    win_move, sum_unmark, who_win = find_winner(move_list, bingo_list)
    print(f'last move: {win_move}\n'
          f'sum of unmarked: {sum_unmark}\n'
          f'final score: {win_move * sum_unmark}\n'
          f'board-winner index: {who_win}\n')

    # PART 2
    last_win_move, last_sum_unmarked = find_last_winner(move_list, bingo_list)
    print(f'Last win move: {last_win_move}\n'
          f'Last sum unmarked: {last_sum_unmarked}\n'
          f'Multiply them: {last_win_move * last_sum_unmarked}')

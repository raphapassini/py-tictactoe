import unittest
import tic_tac_toe as ttt


class TicTacToeTest(unittest.TestCase):

    def setUp(self):
        self.board = ttt.make_board()
        self.p1 = '#'
        self.p2 = '*'

    def test_can_create_board(self):
        """Can create a board"""
        self.assertEqual(len(self.board), 3)

    def test_move_allowed(self):
        """Move should be allowed"""
        assert ttt.move_allowed('0,0', self.board)

    def test_move_out_of_range(self):
        """Cant do a move in a position out of range"""
        self.assertFalse(ttt.move_allowed('10,10', self.board))

    def test_move_already_done(self):
        """Cant do a move already done"""
        self.board = ttt.make_move('0,0', self.board, self.p1)
        self.assertFalse(ttt.move_allowed('0,0', self.board))

    def test_move_has_to_be_valid(self):
        """Move has to be in a valid format"""
        self.assertFalse(ttt.move_allowed('foo,bar', self.board))

    def test_move_should_contain_a_comma(self):
        """Move has to have a comma"""
        self.assertFalse(ttt.move_allowed('foobar', self.board))

    def test_get_correct_line_col(self):
        """Can get the correct line/col from a move"""
        self.assertEqual(ttt.get_line_col('2,0'), [2, 0])

    def test_can_make_move(self):
        """Can make a move"""
        self.board = ttt.make_move('0,0', self.board, self.p1)
        self.assertEqual(self.board[0][0], self.p1)

    def test_status_tie_game(self):
        """Should be no winner in a tie game"""

        #player1 moves
        self.board = ttt.make_move('0,0', self.board, self.p1)
        self.board = ttt.make_move('0,2', self.board, self.p1)
        self.board = ttt.make_move('1,1', self.board, self.p1)
        self.board = ttt.make_move('1,2', self.board, self.p1)
        self.board = ttt.make_move('2,1', self.board, self.p1)

        #player2 moves
        self.board = ttt.make_move('0,1', self.board, self.p2)
        self.board = ttt.make_move('1,0', self.board, self.p2)
        self.board = ttt.make_move('2,0', self.board, self.p2)
        self.board = ttt.make_move('2,2', self.board, self.p2)

        ttt.print_board(self.board)
        self.assertFalse(ttt.status(self.board, [self.p1, self.p2]))

    def test_winner_by_line(self):
        """Player1 should win wen complete a line"""
        self.board = ttt.make_move('0,0', self.board, self.p1)
        self.board = ttt.make_move('0,1', self.board, self.p1)
        self.board = ttt.make_move('0,2', self.board, self.p1)

        ttt.print_board(self.board)
        self.assertEqual(ttt.status(self.board, [self.p1, self.p2]), '#')

    def test_winner_by_col(self):
        """Player1 should win wen complete a col"""
        self.board = ttt.make_move('0,0', self.board, self.p1)
        self.board = ttt.make_move('1,0', self.board, self.p1)
        self.board = ttt.make_move('2,0', self.board, self.p1)

        ttt.print_board(self.board)
        self.assertEqual(ttt.status(self.board, [self.p1, self.p2]), '#')

    def test_winner_by_1st_diagonal(self):
        """Player1 should win wen complete the 1st diagonal"""
        self.board = ttt.make_move('0,0', self.board, self.p1)
        self.board = ttt.make_move('1,1', self.board, self.p1)
        self.board = ttt.make_move('2,2', self.board, self.p1)

        ttt.print_board(self.board)
        self.assertEqual(ttt.status(self.board, [self.p1, self.p2]), '#')

    def test_winner_by_2nd_diagonal(self):
        """Player1 should win wen complete the 2nd diagonal"""
        self.board = ttt.make_move('0,2', self.board, self.p1)
        self.board = ttt.make_move('1,1', self.board, self.p1)
        self.board = ttt.make_move('2,0', self.board, self.p1)

        ttt.print_board(self.board)
        self.assertEqual(ttt.status(self.board, [self.p1, self.p2]), '#')

    def test_should_be_no_moves_at_the_end(self):
        """Should be no moves at the end of the game"""

        #player1 moves
        self.board = ttt.make_move('0,0', self.board, self.p1)
        self.board = ttt.make_move('0,2', self.board, self.p1)
        self.board = ttt.make_move('1,1', self.board, self.p1)
        self.board = ttt.make_move('1,2', self.board, self.p1)
        self.board = ttt.make_move('2,1', self.board, self.p1)

        #player2 moves
        self.board = ttt.make_move('0,1', self.board, self.p2)
        self.board = ttt.make_move('1,0', self.board, self.p2)
        self.board = ttt.make_move('2,0', self.board, self.p2)
        self.board = ttt.make_move('2,2', self.board, self.p2)

        self.assertEqual(ttt.moves_left(self.board), 0)

    def test_should_be_nine_moves_at_the_begining(self):
        """Shold be nine moves at the begning of the game"""
        self.assertEqual(ttt.moves_left(self.board), 9)

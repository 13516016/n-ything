import unittest
from model import Queen, Bishop, Rook, Knight, Color

def generate_test_chess_pieces():
  chess_pieces = []

  q1_black = Queen(0,1,Color.BLACK)
  q2_white = Queen(1, 6, Color.WHITE)
  q3_black = Queen(3, 4, Color.BLACK)
  r1_white = Rook(0,4, Color.WHITE)
  r2_black = Rook(1, 7, Color.BLACK)
  b1_white = Bishop(1, 2, Color.WHITE)
  b2_white = Bishop(5, 3, Color.WHITE)
  k1_white = Knight(2, 3, Color.WHITE)
  k2_black = Knight(3, 1, Color.BLACK)
  
  chess_pieces.append(q1_black)
  chess_pieces.append(r1_white)
  chess_pieces.append(b1_white)
  chess_pieces.append(q2_white)
  chess_pieces.append(r2_black)
  chess_pieces.append(k1_white)
  chess_pieces.append(k2_black)
  chess_pieces.append(q3_black)
  chess_pieces.append(b2_white)
  
  piece_dict = {
    "queen": [q1_black, q2_white, q3_black],
    "bishop": [b1_white, b2_white],
    "rook": [r1_white, r2_black],
    "knight": [k1_white,k2_black]
  }

  piece_attacked = {
    "queen": 7,
    "bishop": 3,
    "rook": 3,
    "knight":3 
  }

  return chess_pieces, piece_dict, piece_attacked



class ModelUnitTest(unittest.TestCase):
  def test_queen(self):
    chess_pieces, piece_dict, piece_attacked = generate_test_chess_pieces()
    queens = piece_dict["queen"]

    attacked_pawns = sum([queen.count_attacked_pawns(chess_pieces) for queen in queens])

    self.assertEqual(attacked_pawns, piece_attacked["queen"], "Queen count attacked pawns" )

  def test_bishop(self):
    chess_pieces, piece_dict, piece_attacked = generate_test_chess_pieces()
    bishops = piece_dict["bishop"]

    attacked_pawns = sum([bishop.count_attacked_pawns(chess_pieces) for bishop in bishops])

    self.assertEqual(attacked_pawns, piece_attacked["bishop"], "Bishop count attacked pawns" )

  def test_rook(self):
    chess_pieces, piece_dict, piece_attacked = generate_test_chess_pieces()
    rooks = piece_dict["rook"]

    attacked_pawns = sum([rook.count_attacked_pawns(chess_pieces) for rook in rooks])

    self.assertEqual(attacked_pawns, piece_attacked["rook"], "Rook count attacked pawns" )
  
  def test_knight(self):
    chess_pieces, piece_dict, piece_attacked = generate_test_chess_pieces()
    knights= piece_dict["knight"]

    attacked_pawns = sum([knight.count_attacked_pawns(chess_pieces) for knight in knights])

    self.assertEqual(attacked_pawns, piece_attacked["knight"], "Knight count attacked pawns" )

if __name__ == '__main__':
    unittest.main()

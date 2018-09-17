from abc import ABC,abstractmethod

class ChessPiece(ABC):
  def __init__(self,x,y,color):
    self.x = x
    self.y = y
    self.color = color
    super().__init__()

  def is_color_different(self, chess_piece):
    return self.color != chess_piece.color

  def is_position_different(self, chess_piece):
    return not (self.x == chess_piece.x and self.y == chess_piece.y)

  @abstractmethod
  def count_attacked_pawns(self,chess_pieces):
    pass

# Find chess piece with the given coordinate
def find_chess_piece(chess_pieces,x,y):
  for chess_piece in chess_pieces:
    if (chess_piece.x == x and chess_piece.y == y):
      return chess_piece
  return None
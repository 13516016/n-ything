from .ChessPiece import ChessPiece
from .Color import Color
class Knight(ChessPiece):
  def __init__(self,x,y,color):
    super().__init__(x,y,color)
  def __str__(self):
    if (self.color == Color.BLACK):
        return "k"
    else:
        return "K"

  def __check_knight(self,chess_pieces):
    attacked_enemy = []
    attacked_ally = []
    for chess_piece in chess_pieces:
      if(self.is_position_different(chess_piece)
         and
          ( ((chess_piece.x+2 == self.x) and (chess_piece.y+1 == self.y)) or
            ((chess_piece.x-2 == self.x) and (chess_piece.y+1 == self.y)) or
            ((chess_piece.x+2 == self.x) and (chess_piece.y-1 == self.y)) or
            ((chess_piece.x-2 == self.x) and (chess_piece.y-1 == self.y)) or
            ((chess_piece.x+1 == self.x) and (chess_piece.y+2 == self.y)) or
            ((chess_piece.x-1 == self.x) and (chess_piece.y+2 == self.y)) or
            ((chess_piece.x+1 == self.x) and (chess_piece.y-2 == self.y)) or
            ((chess_piece.x-1 == self.x) and (chess_piece.y-2 == self.y)) )
        ):
        if (self.is_color_different(chess_piece)):
            attacked_enemy.append(chess_piece)
        else:
            attacked_ally.append(chess_piece)

    return attacked_ally, attacked_enemy

  def list_attacked_ally(self,chess_pieces):
    return self.__check_knight(chess_pieces)[0]

  def list_attacked_enemy(self,chess_pieces):
      return self.__check_knight(chess_pieces)[1]

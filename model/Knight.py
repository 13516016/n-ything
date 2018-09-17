from .ChessPiece import ChessPiece

class Knight(ChessPiece):
  def __init__(self,x,y,color):
    super().__init__(x,y,color)

  def count_attacked_pawns(self,chess_pieces):
    attacked_pawns = 0

    for chess_piece in chess_pieces:
      if((self.is_color_different(chess_piece) and self.is_position_different(chess_piece)) 
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

        attacked_pawns+=1

    return attacked_pawns

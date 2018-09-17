from .ChessPiece import ChessPiece, find_chess_piece

class Rook(ChessPiece):
  def __init__(self,x,y,color):
    super().__init__(x,y,color)

  def __check_north(self, chess_pieces):
    for y in range(self.y+1,8):
      x = self.x

      chess_piece = find_chess_piece(chess_pieces,x,y)
      if (chess_piece != None):
        if (self.is_color_different(chess_piece)):
          return 1
        else:
          return 0

    return 0

  def __check_east(self, chess_pieces):
    for x in range(self.x+1,8):
      y = self.y

      chess_piece = find_chess_piece(chess_pieces,x,y)
      if (chess_piece != None):
        if (self.is_color_different(chess_piece)):
          return 1
        else:
          return 0

    return 0
  
  def __check_south(self, chess_pieces):
    for y in range(self.y-1,-1,-1):
      x = self.x

      chess_piece = find_chess_piece(chess_pieces,x,y)
      if (chess_piece != None):
        if (self.is_color_different(chess_piece)):
          return 1
        else:
          return 0

    return 0

  def __check_west(self, chess_pieces):
    for x in range(self.x-1,-1,-1):
      y = self.y
      
      chess_piece = find_chess_piece(chess_pieces,x,y)
      if (chess_piece != None):
        if (self.is_color_different(chess_piece)):
          return 1
        else:
          return 0

    return 0

  def count_attacked_pawns(self,chess_pieces):
    attacked_pawns = 0
    attacked_pawns += self.__check_north(chess_pieces)
    attacked_pawns += self.__check_east(chess_pieces)
    attacked_pawns += self.__check_south(chess_pieces)
    attacked_pawns += self.__check_west(chess_pieces)

    return attacked_pawns

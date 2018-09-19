from .ChessPiece import ChessPiece, find_chess_piece

class Bishop(ChessPiece):
  def __init__(self,x,y,color):
    super().__init__(x,y,color)

  def __str__(self):
    if (self.color == Color.BLACK):
        return "b"
    else:
        return "B"

  def __check_northeast(self, chess_pieces):
    for x in range(self.x+1,8):
      y = self.y + abs(self.x-x)

      chess_piece = find_chess_piece(chess_pieces,x,y)
      if (chess_piece != None):
        if (self.is_color_different(chess_piece)):
          return None, chess_piece
        else:
          return chess_piece, None

    return None,None

  def __check_southeast(self, chess_pieces):
    for x in range(self.x+1,8):
      y = self.y - abs(self.x-x)

      chess_piece = find_chess_piece(chess_pieces,x,y)
      if (chess_piece != None):
        if (self.is_color_different(chess_piece)):
          return None, chess_piece
        else:
          return chess_piece, None

    return None,None

  def __check_southwest(self, chess_pieces):
    for x in range(self.x-1,-1,-1):
      y = self.y - abs(self.x-x)

      chess_piece = find_chess_piece(chess_pieces,x,y)
      if (chess_piece != None):
        if (self.is_color_different(chess_piece)):
          return None, chess_piece
        else:
          return chess_piece, None

    return None,None

  def __check_northwest(self, chess_pieces):
    for x in range(self.x-1,-1,-1):
      y = self.y + abs(self.x-x)

      chess_piece = find_chess_piece(chess_pieces,x,y)
      if (chess_piece != None):
        if (self.is_color_different(chess_piece)):
          return None, chess_piece
        else:
          return chess_piece, None

    return None,None

  def __check_bishop(self,chess_pieces):
    attacked_ally = []
    attacked_ally.append(self.__check_northeast(chess_pieces)[0]) if self.__check_northeast(chess_pieces)[0] != None else None
    attacked_ally.append(self.__check_southeast(chess_pieces)[0]) if self.__check_southeast(chess_pieces)[0] != None else None
    attacked_ally.append(self.__check_southwest(chess_pieces)[0]) if self.__check_southwest(chess_pieces)[0] != None else None
    attacked_ally.append(self.__check_northwest(chess_pieces)[0]) if self.__check_northwest(chess_pieces)[0] != None else None

    attacked_enemy = []
    attacked_enemy.append(self.__check_northeast(chess_pieces)[1]) if self.__check_northeast(chess_pieces)[1] != None else None
    attacked_enemy.append(self.__check_southeast(chess_pieces)[1]) if self.__check_southeast(chess_pieces)[1] != None else None
    attacked_enemy.append(self.__check_southwest(chess_pieces)[1]) if self.__check_southwest(chess_pieces)[1] != None else None
    attacked_enemy.append(self.__check_northwest(chess_pieces)[1]) if self.__check_northwest(chess_pieces)[1] != None else None

    return attacked_ally, attacked_enemy

  def list_attacked_ally(self,chess_pieces):
    return self.__check_bishop(chess_pieces)[0]

  def list_attacked_enemy(self,chess_pieces):
    return self.__check_bishop(chess_pieces)[1]

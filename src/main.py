import sys
from util.printer import print_board, print_attacked_pieces
from util.parser import parse
from util.interface import show_file_prompt, show_landing_screen, show_option_prompt, choose_algorithm
from algorithm import annealing, genetic, hill_climbing


if (__name__ == '__main__'):
  show_landing_screen()

  # Get external file
  filename = show_file_prompt()
  try:
    chess_pieces = parse(filename)
  
    # Show options
    option = show_option_prompt()

    result = choose_algorithm(option, chess_pieces)
    print_board(result)
    print_attacked_pieces(result)
    
  except IOError as error:
    sys.exit("Error : " +  str(error))

  # Parse external file
  
  # hill_climbing(chess_pieces, generate_move, 25)


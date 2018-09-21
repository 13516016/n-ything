import sys
from util.printer import print_board, print_attacked_pieces
from util.parser import parse
from util.interface import show_file_prompt, show_landing_screen, show_option_prompt, choose_algorithm
from algorithm import annealing, genetic, hill_climbing
from nything import generate_random_solution


if (__name__ == '__main__'):
  show_landing_screen()

  # Get external file
  if (len(sys.argv) < 2): 
    filename = show_file_prompt()
  else :
    filename = sys.argv[1]
  
  # Show options
  option = show_option_prompt()
  
  # Parse external file
  try:
    chess_pieces = parse(filename)
  except IOError as error:
    sys.exit("Error : " +  str(error))
  
  # result = choose_algorithm(option, chess_pieces)
  chess_pieces = generate_random_solution(chess_pieces)
  print_board(chess_pieces)
  print_attacked_pieces(chess_pieces)

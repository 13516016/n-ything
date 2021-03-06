import sys
from util.printer import print_board, print_attacked_pieces
from util.parser import parse
from util.interface import show_file_prompt, show_landing_screen, show_option_prompt, choose_algorithm
from algorithm import annealing, genetic, hill_climbing
from nything import generate_random_solution
import time


if (__name__ == '__main__'):
  show_landing_screen()

  # Get external file
  filename = ''
  if (len(sys.argv) >= 2):
    filename = sys.argv[1]
  else:
    filename = show_file_prompt()

  try:
    chess_pieces = parse(filename)

    # Generate initial state
    chess_pieces = generate_random_solution(chess_pieces)
    print_board(chess_pieces)
    print_attacked_pieces(chess_pieces)
    
    # Show options
    option = show_option_prompt()
    
    # Solve N-y thing 
    result, runtime = choose_algorithm(option, chess_pieces)
    print("\nSolved in {} seconds\n".format(runtime))
    print_board(result)
    print_attacked_pieces(result)
  
  except IOError as error:
    sys.exit("Error : " +  str(error))
  

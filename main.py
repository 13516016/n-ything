from util import parse, printboard, printattack
from algorithm import annealing, genetic, hill_climbing
from model import Color, Queen
from nything import generate_random_solution


def show_landing_screen():
  print(
    '''
                                                                    ███╗   ██╗              ██╗   ██╗    ████████╗██╗  ██╗██╗███╗   ██╗ ██████╗
                                                                    ████╗  ██║              ╚██╗ ██╔╝    ╚══██╔══╝██║  ██║██║████╗  ██║██╔════╝
                                                                    ██╔██╗ ██║    █████╗     ╚████╔╝        ██║   ███████║██║██╔██╗ ██║██║  ███╗
                                                                    ██║╚██╗██║    ╚════╝      ╚██╔╝         ██║   ██╔══██║██║██║╚██╗██║██║   ██║
                                                                    ██║ ╚████║                 ██║          ██║   ██║  ██║██║██║ ╚████║╚██████╔╝
                                                                    ╚═╝  ╚═══╝                 ╚═╝          ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝
    '''
  )

def show_file_prompt():
  print("Enter filename: ", end='')
  filename = input()
  return filename

def show_option_prompt():
  option = 0
  while (option < 1 and option >3):
    print("Press 1 to use Hill Climbing Algorithm")
    print("Press 2 to use Simulated Annealing Algorithm")
    print("Press 3 to use Genetic Algorithm")
    option = int(input())

  return option

def choose_algorithm(chess_pieces, option):
  # result = chess_pieces
  if option == 1:
    pass
    # result =  annealing(chess_pieces)
  elif option == 2:
    pass
    # result =  genetic(chess_pieces)
  elif option == 3:
    pass
    # result =  hill_climbing(chess_pieces)
  return result

if (__name__ == '__main__'):
  show_landing_screen()
  filename = show_file_prompt()
  option = show_option_prompt()

  chess_pieces = parse(filename)
  # result = choose_algorithm(option, chess_pieces)
  chess_pieces = generate_random_solution(chess_pieces)
  printboard(chess_pieces)
  printattack(chess_pieces)

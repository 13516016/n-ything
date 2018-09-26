from algorithm import hill_climbing, annealing, genetic
from util.printer import print_board, print_attacked_pieces
import time

OPTION_HILL_CLIMBING = 1
OPTION_SIMULATED_ANNEALING = 2
OPTION_GENETIC_ALGORITHM = 3

def __do_hill_climbing(chess_pieces):
    max_iteration = int(input("Max iterations: "))

    start_time = time.time()
    result = hill_climbing(chess_pieces, max_iteration)
    return result, time.time() - start_time

def __do_simulated_annealing(chess_pieces):
    max_iteration = int(input("Max iterations: "))
    initial_temperature = int(input("Initial temperature: "))
    descent_rate = int(input("Descent rate: "))
    iteration_per_change = int(input("Iteration descent rate: "))
    
    start_time = time.time()    
    result = annealing(chess_pieces, max_iteration, initial_temperature, descent_rate, iteration_per_change)
    return result, time.time() - start_time

def __do_genetic_algorithm(chess_pieces):
    max_iteration = int(input("Max iterations: "))
    state_generation = int(input("Initial state generation: "))
    
    start_time = time.time()    
    result = genetic(chess_pieces, state_generation, max_iteration)
    return result, time.time() - start_time

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
  filename = input("Enter filepath: ")
  return filename

def show_option_prompt():
  option = 0
  while (option < 1 or option > 3):
    print()
    print("Press 1 to use Hill Climbing Algorithm")
    print("Press 2 to use Simulated Annealing Algorithm")
    print("Press 3 to use Genetic Algorithm")
    print()
    option = int(input("Input : "))

  return option

def choose_algorithm(option, chess_pieces):
  result = chess_pieces
  runtime = 0
  if option == OPTION_HILL_CLIMBING:
    print("\n>> Using Hill Climbing Algorithm")
    result, runtime =  __do_hill_climbing(chess_pieces)
  elif option == OPTION_SIMULATED_ANNEALING:
    print("\n>> Using Simulated Annealing Algorithm")
    result, runtime =  __do_simulated_annealing(chess_pieces)
  elif option == OPTION_GENETIC_ALGORITHM:
    print("\n>> Using Genetic Algorithm")
    result, runtime =  __do_genetic_algorithm(chess_pieces)
  return result, runtime
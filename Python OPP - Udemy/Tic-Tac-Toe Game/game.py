from board import Board
from player import Player

class TicTacToeGame:
  
    def start(self):
      print("============================")
      print("\nWelcome to Tic-Tac-Toe")
      print("============================")
      
      board = Board()
      player = Player()
      computer = Player(False)
      board.print_board()
      
      #Ask player if the would like to play the round
      while True:       #Game   
          #Get move, check Tie, check game over
          while True:   #Round
            player_move = player.get_human_move()
            board.submit_move(player, player_move)
            board.print_board()
            
            if board.check_is_tie():
              print("It is a tie! please try again. ")
              break
            elif board.check_game_over(player,player_move):
              print("You won the game! ")
              break
            else:  
              computer_move = computer.get_computer_move()
              board.submit_move(computer, computer_move)
              board.print_board()
              if board.check_game_over(computer,computer_move):
                print("The computer won the game! ")
                break
          
          play_again = input("Would you like to play the game again. Enter y (Yes) or n (No): ")
          if play_again != 'y' and play_again != 'Y':
            print("Bye! Come back soon")
            break
          else:
            self.start_new_round(board)
            
    def start_new_round(self,board):
      print("=================")
      print("New round")
      print("=================")
      board.reset_board()
      board.print_board()
      
      
start_game = TicTacToeGame()
start_game.start()
            
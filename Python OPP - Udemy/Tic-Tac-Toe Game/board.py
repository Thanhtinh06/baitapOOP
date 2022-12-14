from move import Move
from player import Player


class Board:
  
    Empty_cell = 0
    
    def __init__(self):
        self.game_board = [[0,0,0],
                           [0,0,0],
                           [0,0,0],]
        
    def print_board(self):
        
        print("\nPositions: ")
        self.print_board_with_positions()
        
        print("\nBoard: ")
        for row in self.game_board:
            print("|", end="")
            for column in row:
              if column == Board.Empty_cell:
                print("   |", end="")
              else:
                print(f" {column} |",end="")
            print()
        print()
    
    def print_board_with_positions(self):  
        print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")
        
    def submit_move(self,player,move):
        row = move.get_row()
        col = move.get_column()
        value = self.game_board[row][col]
        
        if value == Board.Empty_cell:
          self.game_board[row][col] = player.marker
        else:
          print("This position is already taken. Please enter another one. ")
          
    def check_game_over(self, player, last_move):

        return ((self.check_row(player, last_move))
                or self.check_column(player, last_move)
                or self.check_diagonal(player, last_move)
                or self.check_antidiagonal(player, last_move))
        

    def check_row(self, player, last_move):
      row_index = last_move.get_row()
      board_row = self.game_board[row_index]
      return board_row.count(player.marker) == 3
    
    def check_column(self, player, last_move):
      markers_count = 0
      column_index = last_move.get_column()
      for i in range(3):
        if self.game_board[i][column_index] == player.marker:
            markers_count += 1
      
      return markers_count == 3
    
    
    def check_diagonal(self, player, last_move):
      markers_count = 0
      for i in range(3):
        if self.game_board[i][i] == player.marker:
            markers_count += 1
      
      return markers_count == 3
    
    def check_antidiagonal(self, player, last_move):
      markers_count = 0
      for i in range(3):
        if self.game_board[i][2-i] == player.marker:
            markers_count += 1
      
      return markers_count == 3
    
    def check_is_tie(self):
      empty_count = 0
      for row in self.game_board:
        empty_count += row.count(Board.Empty_cell)
      return empty_count == 0
    
    def reset_board(self):
      self.game_board = [[0,0,0],
                         [0,0,0],
                         [0,0,0],]
          
          
          
          
          

# board = Board()
# move = Move(8)
# player = Player()

# board.print_board()
# board.submit_move(player, move)
# board.print_board()
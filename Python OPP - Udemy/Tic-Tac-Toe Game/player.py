import random
from move import Move

class Player:
    player = "X"
    computer = "O"
    def __init__(self, is_human=True):
      self._is_human = is_human
     
      if is_human:
        self._marker = Player.player
      else:
        self._marker = Player.computer
    
    @property
    def is_computer(self):
      return self._is_human
    
    @property
    def marker(self):
      return self._marker
    
    def get_move(self):
      
      if self._is_human:
          return self.get_human_move()
      else:
          return self.get_computer_move()
        
    def get_human_move(self):
      while True:
        user_input = int(input('Please enter your move (1-9): '))
        move = Move(user_input)
        if  move.is_value():
          break
        else:
          print("Please enter an interger between 1 and 9.")
      return move
    
    
    def get_computer_move(self):
      ramdom_choice = random.choice(list(range(1,10)))
      move = Move(ramdom_choice)
      print("Computer move (1-9): ", move.value)
      return move



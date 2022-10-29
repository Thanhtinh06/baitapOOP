import random
class Die:

    def __init__(self):
        self._value = None
    
    @property
    def value(self):
      return self._value
    
    def roll(self):
        result_rolled = random.randrange(1,6)
        self._value = result_rolled
        return result_rolled
      

class Player:
   
    def __init__(self,die,is_computer=False):
      self._die = die
      self._is_computer = is_computer
      self._counter = 10
      
    @property
    def die(self):
      return self._die
    
    @property
    def is_computer(self):
      return self._is_computer
    
    @property
    def counter(self):
      return self._counter
    
    
    def increment_counter(self):
      self._counter += 1
    
    def decrement_counter(self):
      self._counter -= 1
    
    def roll_die(self):
      return self._die.roll()
      


class DiceGame:
  
  
    def __init__(self,human_player,computer_player):
      self._human_player = human_player
      self._computer_player = computer_player


    def start_game(self):
      
      self.print_game_welcome()
      
      count_round = 1
      while True:
        print(f' 🎲 The round {count_round} ')
        self.start_round()
        count_round += 1
        game_over = self.ckeck_game_over()
        if game_over:
          break
    
        
    def start_round(self):
      
      #Welcome user
      self.print_round_welcome()
      
      #Roll the dice
      human_value = self._human_player.roll_die()
      computer_value = self._computer_player.roll_die()
      
      #Show the values
      self.show_value(human_value,computer_value)
      
      #Determine winner and loser
      
      if human_value > computer_value:
        print('\nYou won the round! 🎉 ')
        self.update_counters(winner=self._human_player,loser=self._computer_player)
        
      elif human_value < computer_value:
        print('\nThe computer won the round. 😢 Try again.')
        self.update_counters(winner=self._computer_player,loser=self._human_player)
        
      else:
        print("It's a tie! 😎")
      
      #show counter
      self.show_counter()
      

    def ckeck_game_over(self):
      
      if self._human_player._counter == 0:
        self.show_game_over(self._human_player)
        return True
      elif self._computer_player._counter == 0:
        self.show_game_over(self._computer_player)
        return True
      else:
        return False
      
    def show_game_over(self, winner):
      if winner.is_computer:
        print("\n=====================")
        print(" G A M E    O V E R ❤️‍🔥")
        print("====================")
        print("The computer won the game. Sorry..")
        print("===========================")
      else:
        print("\n=====================")
        print(" G A M E    O V E R ❤️‍🔥")
        print("====================")
        print("You won the game. Congratulations..")
        print("===========================")
        
    def print_game_welcome(self):
      print('\n=========================================')
      print(' 🎲 Welcome to Roll the Dice !!! 🎲')
      print('=========================================')
        
    def print_round_welcome(self):
      
      print("\n----- Start the round -----")
      input(" 🎲 Press any key to roll the dice. 🎲 ") 
    
    def show_value(self,human_value,computer_value):
      
      print(f'\nYour die: {human_value}')
      print(f'Computer die {computer_value}')
      
    def show_counter(self):
      
      print(f'\nYour counter: {self._human_player.counter}')
      print(f'Computer counter: {self._computer_player.counter}\n') 
      
    def update_counters(self, winner, loser):
      winner.decrement_counter()
      loser.increment_counter()


die_human_player = Die()
human_player = Player(die_human_player,False)
die_computer_player = Die()
computer_player = Player(die_computer_player,True) 

Dice_game = DiceGame(human_player,computer_player)
Dice_game.start_game()
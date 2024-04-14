############### Blackjack Project #####################

import random
#from replit import clear
from art import logo

def deal_card():
  """Returns a random card"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(list_cards):
  '''Calculates the score of the cards in the list'''
  if sum(list_cards) == 21 and len(list_cards) == 2: # Checking for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    return 0

  if 11 in list_cards and sum(list_cards) > 21: # Checking for an 11 (ace). If the score is already over 21, we remove the 11 and replace it with a 1.
    list_cards.remove(11)
    list_cards.append(1)
  return sum(list_cards)

def compare(userScore, computerScore):
  if userScore > 21 and computerScore > 21:
    return "You went over. You lose 😤"

  if userScore == computerScore:
    return "Draw 🙃"
  elif computerScore == 0:
    return "Lose, opponent has Blackjack 😱"
  elif userScore == 0:
    return "Win with a Blackjack 😎"
  elif userScore > 21:
    return "You went over. You lose 😭"
  elif computerScore > 21:
    return "Opponent went over. You win 😁"
  elif userScore > computerScore:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():
  print(logo)
  # Deal the user and computer 2 cards each using deal_card(). 
  user_cards = []
  computer_cards = []
  gameOver = False
  
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not gameOver: # this while loop is responsible for dealing with when the user wants to keep drawing cards
    userScore = calculate_score(user_cards) # This the place where I want to call it because it's only after I've dealt the user and the computer some cards can I actually calculate their scores.
    computerScore = calculate_score(computer_cards)
    print(f'Your cards: {user_cards}, current score: {userScore}')
    print(f"Computer's first card: {computer_cards[0]}") # The dealer will reveal their first card
    
    if userScore == 0 or computerScore == 0 or userScore > 21: # If the user has a blackjack (score of 21 with 2 cards)
      gameOver = True
    else:
      userNextCard = input("Would you like to receive another card or pass? Type 'y' or 'n': ").lower() # Asking the user if they want to draw another card
      if userNextCard == 'y':
        user_cards.append(deal_card())
      else:
        gameOver = True
  
  
  # The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
  
  # Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computerScore != 0 and computerScore < 17:
    computer_cards.append(deal_card())
    computerScore = calculate_score(computer_cards)
# Creating a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
  print(f"   Your final hand: {user_cards}, final score: {userScore}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computerScore}")
  print(compare(userScore, computerScore))
# Asking the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
  #clear()
  play_game()

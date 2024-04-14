
#HINT: You can call clear() to clear the output in the conso
from art import logo
print(logo)


bids = {}
biddingFinished = False

def findTheBiigestBid(bid):
  highestBid = 0
  winner = ''
  # {"Max": 100, "Olga": 105}
  for participant in bid:
    if bid[participant] > highestBid:
      highestBid = bid[participant]
      winner = participant
  print(f"The winner is {winner} with a bid of ${highestBid}")
# findTheBiigestBid({"Max": 100, "Olga": 105})

while not biddingFinished:
  name = input("Welcome to the secret auction program.\nWhat is your name?: ")
  offer = int(input("What's your bid?: $"))
  bids[name] = offer
  addingParticipant = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  if addingParticipant == "no":
    biddingFinished = True
    findTheBiigestBid(bids)
  else:
    pass


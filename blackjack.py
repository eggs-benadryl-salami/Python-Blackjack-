
import random

def deposit_funds():
    while True:
        amount = input("How much would you like to deposit?: $")
        if amount.isdigit(): 
            amount = int(amount) 
            if amount > 0:
                break
            else:
                print("The amount must be greater than 0")
        else:
            print("Please enter a number")
    
    return amount


def place_bet():
    while True:
        amount = input("How much would you like to bet?: $")
        if amount.isdigit(): 
            amount = int(amount)
            if amount > 0:
              break
            else:
              print("Please enter a number greater than 0")
        else:
            print("Please enter a number")
    
    return amount


def multiplier():
  while True:
        amount = (input("Enter your multiplier {1/2/2/3/4/5}: "))
        if amount.isdigit(): 
            amount = int(amount)
            if amount > 0:
              break
            else:
              print("Please enter a number greater than 0")
        else:
            print("Please enter a number")
          
  return amount
   

def game():
  global playerp, computerp, winorlose
  playerp = 0
  computerp = 0
  suits_symbols = ['♠', '♦', '♥', '♣']
  ran_suits = random.choice(suits_symbols)
  card_dict = {
    "J": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Q": 11,
    "K": 12,
    "A":13
    }

  deck_dict = {
       
    }

  while True:

    card_symbol, card_value = random.choice(list(card_dict.items()))

    while True:
      card_symbol, card_value = random.choice(list(card_dict.items()))
      if (card_symbol, ran_suits) not in deck_dict.items():
         break 
    
    deck_dict[card_symbol] = ran_suits 
    
    print("┌─────────┐")
    print("│░░░░░░░░░│")
    print("│░░░░░░░░░│")
    print("│░░░░░░░░░│")
    print("│░░░░░░░░░│")
    print("│░░░░░░░░░│")
    print("│░░░░░░░░░│")
    print("│░░░░░░░░░│")
    print("└─────────┘")
    yorn = input("Do you want to draw a card? (yes/no): ")
 
    if yorn == "yes":
      if card_value == 10:
         space = ""
      else:
         space = " "  
    
      if card_symbol == "A":
         while True:
            card_value = input("You got an Ace! Would you like your card to be 1 or 13 points?: ")
            if card_value.isdigit(): 
                card_value = int(card_value)
                if card_value == 1 or card_value == 13:
                    break
                else:
                    print("Please enter either 1 or 13")
            else:
                print("Please enter a number")
    
             
      playerp += int(card_value)
      print("Your card:")
      print("┌─────────┐")
      print("│{}{}       │".format(card_symbol, space))
      print("│         │")
      print("│         │")
      print("│    {}    │".format(ran_suits))
      print("│         │")
      print("│         │")
      print("│       {}{}│".format(card_symbol, space))
      print("└─────────┘")
      print("Your total points: ", playerp)
    
    if playerp > 21:
        print("Bust! You Lose")
        winorlose = "lose"
        break
      
   
    if playerp == 21:
        print("Black Jack! You won!")
        winorlose = "win"
        break

    elif yorn == "no":
        while True:
            computer_card = random.randint(1, 13)
            computerp += computer_card
      
            if computerp >= 17:
                print("Computer total points:", computerp)
                break  
        break 
      
  if computerp > 21:
    print("Computer busts! You Win!")
    winorlose = "win"
  elif computerp > playerp:
    print("You lose!, computer wins")
    winorlose = "lose"
  elif playerp > computerp and playerp < 21:
    print("You Win!")
    winorlose = "win"


def calculate_winnings(balance):
  while True:
    bet = place_bet()
    multiplier_value = multiplier()
    total_bet = bet * multiplier_value 
    if total_bet > balance:
      print("Insufficient balance! Your current balance is:", balance)
    else:
      break
  print("You are betting $", bet, "and setting the multiplier to", multiplier_value, "x. Total bet: $", total_bet)
  game()
  if winorlose == "win":
    print("You won $", total_bet)
    balance += total_bet
  elif winorlose == "lose":
    print("You Lost $", total_bet)
    balance -= total_bet
  return balance 


def main():
  balance = deposit_funds()
  while True:
    print("Current balance: $", balance )
    if input("Press enter to play (q to quit): "):
      break
    balance = calculate_winnings(balance)
  print("You're leaving with $", balance)

main()






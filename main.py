#from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to Secret Auction program")

bidders = {}
end_flag = False
while not end_flag:
   
  name = input("What is your name? : ")
  bid = int(input("What is your bid? : $"))
  
  bidders[name] = bid
  end = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    
  if end == 'no':
    #clear()
    end_flag = True
    max_value = max(bidders.values())
    max_key = max(bidders, key=bidders.get)
    print(f"The winner is {max_key} with a bid of ${max_value}")
    
  elif end == "yes":
    #clear()
    end_flag = False
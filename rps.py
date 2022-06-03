print("elcome to a game of rock, paper, scissors")
options = ['rock', 'paper', 'scissors']
value = random.choice(options)
selection = input("what is your pick? ")
print(f"Computer chose {value}, Player chose: {selection}")
if value == "rock" and selection == "scissors" or value == "scissors" and selection == "rock":
    print("rocks beats scissors")
elif value == "paper" and selection == "rock" or value == "rock" and selection == "paper":
    print("paper beats rock")
elif value == "scissors" and selection == "paper" or value == "paper" and selection == "scissors":
    print("scissors beats paper")
elif value == selection:
    print("the game is a tie")
else:
    print("wrong option, try again later")


import random
import string
HUMAN = True
AI = False
PAIR = 1
TWOPAIR = 2
THREEOFKIND = 3
FIVEHIGHSTRAIGHT = 4 
SIXHIGHSTRAIGHT = 5 
FULLHOUSE = 6 
FOUROFKIND = 7
class Die(object):
	def __init__(self):
		self.value = -1 
		self.needRoll = True 
	def roll(self):
		if self.needRoll:
			self.value = random.randint(1,6)
			self.needRoll = False
class Player(object):
	def __init__(self, humanity, name):
		self.name = name
		self.humanity = humanity
		self.dice = [Die() for i in range(5)]
	def totDiceVal(self):
		total = 0
		for die in self.dice:
			total += die.value
		return total

	def report(self):
		print (self.name + " dice are:")
		diceNum = 1
		for die in self.dice:
			print ("Die " + str(diceNum) + ": [" + str(die.value) + "],\n")
			diceNum += 1
	def makeRolls(self, rollsNeededStr = ''):
		rollsNeeded = []
		for char in rollsNeededStr:
			if char in string.digits and int(char) in range(1,6):
				rollsNeeded.append(self.dice[int(char) - 1])
		for die in rollsNeeded:
			die.needRoll = True
		for die in self.dice:
			die.roll()
	def score(self):
		numPairs = 0
		trip = False
		

		count = 0
		for die1 in self.dice:
			for die2 in self.dice:
				if die1.value == die2.value:
					count += 1
			if count == 4:
				return FOUROFKIND
			if count == 3:
				trip = True
			if count == 2:
				numPairs += 1
			count = 0
		if trip and numPairs == 2:
			return FULLHOUSE
		if trip:
			return THREEOFKIND
		if numPairs == 4:
			return TWOPAIR
		if numPairs == 2:
			return PAIR

		diceVals = []
		for die in self.dice:
			diceVals.append(die.value)
		diceVals.sort()
		if diceVals == range(2,7):
			return SIXHIGHSTRAIGHT
		if diceVals == range(1,6):
			return FIVEHIGHSTRAIGHT

	def scoreReport(self,score):
		
		if score == PAIR:
			print (self.name, "has a Pair\n")
		elif score == TWOPAIR:
			print (self.name, "has Two Pairs\n")
		elif score == THREEOFKIND:
			print (self.name, "has A Three of A Kind\n")
		elif score == FIVEHIGHSTRAIGHT:
			print (self.name, "has A Five High Straight\n")
		elif score == SIXHIGHSTRAIGHT:
			print (self.name, "has A Six High Straight\n")
		elif score == FULLHOUSE:
			print (self.name, "has A Full House\n")
		elif score == FOUROFKIND:
			print (self.name, "has A Four of A Kind\n")
		
	def fullReport(self):
		self.report()
		self.scoreReport(self.score())

	def findBestRoll(self):
		currentDie = 1
		dieValSave = -1
		baseScore = self.score()
		needRolls = ''
		for die in self.dice:
			dieValSave = die.value
			die.value = -1
			if self.score() == baseScore:
				needRolls = needRolls + str(currentDie)
			die.value = dieValSave
			currentDie += 1
		return needRolls

print ("Welcome to Python Dice Poker, how many players would you like? You can have up to 5.")
numPlay = 0
numAI = 0
numHuman = 0
while True:
    try:
        numPlay = int(input())
        if numPlay in range(1,6):
            break
        raise KeyboardInterrupt
    except KeyboardInterrupt:
        print("I just need a number between 1 and 5")
print ("How many of those players would you like to be AI players?")
while True:
	try:
		numAI = int(input())
		if numAI in range(numPlay+1):
			break
		raise ValueError
	except ValueError:
		print ("We can only have as many AIs as we have players.")
players = []
numHuman = numPlay - numAI
for num in range(numHuman):
	print ("What is Player",num+1,"name?")
	tempname = input()
	players.append(Player(HUMAN,tempname))
for num in range(numAI):
	players.append(Player(AI,"AI"+str(num+1)))

for play in players:
	play.makeRolls()
	play.fullReport()
for play in players:
	if play.humanity == HUMAN:
		print (play.name + ". What would you like to reroll? (Type in the die's number to reroll)")
		play.makeRolls(input())
	else:
		play.makeRolls(play.findBestRoll())
for play in players:
	play.fullReport()
bestPlayer = players[0]
index = 0
tie = False
tiedPlayers = []
for play in players[1::]:
	if int(play.score()) > int(bestPlayer.score()):
		bestPlayer = play
		continue
	if int(play.score()) == int(bestPlayer.score()):
		if play.totDiceVal() > bestPlayer.totDiceVal():
			bestPlayer = play
			continue
		elif int(play.totDiceVal) == int(bestPlayer.totDiceVal()):
			tie = True
			tiedPlayers.append(bestPlayer)
			tiedPlayers.append(play)
			continue
if tie:
	print ("There is a tie between; ")
	for play in tiedPlayers:
		print (play.name)
else:
	print( bestPlayer.name, "is the winner!")
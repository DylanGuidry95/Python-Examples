import random

class Card(object):
    def __init__(self, value, color):
        self.value = value
        self.color = color

class Player(object):
    def __init__(self, name):
        self.name = name
        self.handValue = 0
        self.hand = []
    
    def AddCard(self, card):
        self.hand.append(card)
        self.handValue += card.value

class Dealer(object):
    def __init__(self, players):
        self.players = players


    def DealCards(self, cardPerPlayer):
        for i in range(0,cardPerPlayer + 1):
            for player in self.players:
                v = random.randint(0,100)
                if v % 2 == 0:
                    c = random.randint(0,100)
                    if c % 2 == 0:
                        player.AddCard(Card(5, "Light"))
                    else:
                        player.AddCard(Card(5, "Dark"))
                else:
                    c = random.randint(0,100)
                    if c % 2 == 0:
                        player.AddCard(Card(10, "Light"))
                    else:
                        player.AddCard(Card(10, "Dark"))

    def SortPlayer(self):
        tempPlayer = self.players[0]
        for player in self.players:
                if player.handValue > tempPlayer.handValue:
                    tempPlayer = player
        return tempPlayer, tempPlayer.handValue
                

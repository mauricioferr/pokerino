class Card:
    def __init__(self, suit, name, value):
        self.name = name
        self.suit = suit
        self.value = value

class Hand:
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2
        if self.card1.value < self.card2.value:
            self.name = self.card1.name + self.card2.name
            self.completeName = self.card1.name + self.card1.suit + self.card2.name + self.card2.suit
        else:
            self.name = self.card2.name + self.card1.name
            self.completeName = self.card2.name + self.card2.suit + self.card1.name + self.card1.suit
        if (self.card1.value == self.card2.value):
            self.suit = ' '
        else:
            if (self.card1.suit == self.card2.suit):
                self.suit = 's'
            else:
                self.suit = 'o'
        self.name = self.name + self.suit

        
class Deck:
    def __init__(self):

        self.deck = list()
        names = {'A':0,'K':1,'Q':2,'J':3,'T':4,'9':5,'8':6,'7':7,'6':8,'5':9,'4':10,'3':11,'2':12}
        suites = {'s':names,'c':names,'h':names,'d':names}
        for a in suites.keys():
            for b in suites[a].keys():
                self.deck.append(Card(a,b,suites[a][b]))
    def printDeck(self):
        for a in self.deck:
            print(a.name+a.suit)

class HandSet:
    def __init__(self, deck):
        self.deck = deck.deck
        permutated = list()
        self.handset = list()
        #create permutations
        for a in self.deck:     
            permutated.append(a)
            for b in self.deck:
                if b not in permutated:
                    self.handset.append(Hand(a,b))
    def printHandSet(self):
        for a in self.handset:
            print(a.name)

class Chart:
    def __init__(self,handset):
        self.chart = dict()
        self.probability = dict()
        self.action = dict()
        for a in handset.handset:
            if a.name not in self.chart.keys():
                self.chart[a.name]=list()
                self.chart[a.name].append(a)
            else:
                self.chart[a.name].append(a)
        for a in self.chart.keys():
            self.probability[a] = 100*len(self.chart[a])/1326
            self.action[a] = 'Fold'
    def updateActionProbability(self):
        #always call this function when initiallizing a chart
        self.fold = 0
        self.bet = 0
        self.call = 0
        for a in self.action.keys():
            if self.action[a] == 'Fold':
                self.fold = self.fold + self.probability[a]
            if self.action[a] == 'Raise':
                self.bet = self.bet + self.probability[a]
            if self.action[a] == 'Call':
                self.fold = self.fold + self.probability[a]
    
    
"""class Player:
    def __init__(self, stack)
        self.stack = stack
    def draw(self, hand):
        self.hand = hand
    def endTurn (self, position)
        self.position = position
    def updateStack(self, winlose)
        self.stack = self.stack + winlose"""

D = Deck()
#D.printDeck()
H = HandSet(D)
C = Chart(H)
C.updateActionProbability()
#H.printHandSet()

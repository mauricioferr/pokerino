import numpy as np
def slice(seq, k):
    return seq[k:]+seq[:k]
class Card:
    def __init__(self, suit, name, value):
        self.name = name
        self.suit = suit
        self.value = value

class Hand:
    def __init__(self,card1,card2):
        self.card1 = card1
        self.card2 = card2
        if self.card1.value < self.card2.value:
            self.name = self.card1.name + self.card2.name
        else:
            self.name = self.card2.name + self.card1.name
        if (self.card1.suit == self.card2.suit) and (self.card1.value != self.card2.value):
            self.suit = 's'
        else:
            self.suit = 'o'
        self.name = self.name + self.suit

class Deck:
    def __init__(self):

        self.deck = list()
        names = {'A':0,'K':1,'Q':2,'J':3,'T':4,'9':5,'8':6,'7':7,'6':8,'5':9,'4':10,'3':11,'2':12}
        suites = {'S':names,'C':names,'H':names,'D':names}
        for a in suites.keys():
            for b in suites[a].keys():
                self.deck.append(Card(a,b,suites[a][b]))

class Chart:
    def __init__(self):
        self.deck = list()
        names = {'A':0,'K':1,'Q':2,'J':3,'T':4,'9':5,'8':6,'7':7,'6':8,'5':9,'4':10,'3':11,'2':12}
        suites = {1:names, 2:names}
        for a in suites.keys():
            for b in suites[a].keys():
                self.deck.append(Card(a, b, suites[a][b]))
        self.hands = list()
        b = 13
        for a in range(13):
            for c in range(b-13,b):
                self.hands.append(Hand(self.deck[a],self.deck[c]))
            b = b+1
        self.chart = list()
        a = 0
        for b in range(13):
            row = list()
            for c in range(13):
                row.append(self.hands[a])
                a = a+1
            srow = slice(row, -b)
            self.chart.append(srow)

    def printBaseChart(self):
        collum = list()
        for a in range(13):
            row = list()
            for b in range(13):
                row.append(self.chart[a][b].name)
            collum.append(row)
        for a in range(13):
            print(collum[a])



test = Chart()
test.printBaseChart()

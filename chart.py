from tkinter import Entry, Button, Text, Label, Tk, END, RAISED 

class Card:
    def __init__(self, name, value):
        self.name = name
        self.value = value


def handsList():
    names = {'A':0,'K':1,'Q':2,'J':3,'T':4,'9':5,'8':6,'7':7,'6':8,'5':9,'4':10,'3':11,'2':12}
    handDict = dict()
    suitsDict = dict()
    verified = list()
    for a in names.keys():
        A = names[a]
        for b in names.keys():
            B = names[b]
            if b not in verified:
                if a==b:
                    handDict[a+b]=[A,B]
                    suitsDict[a+b] = ' '
                else:
                    if A>B:
                        handDict[b+a+'s']=[A,B]
                        suitsDict[b+a+'s'] = 's'
                        handDict[b+a+'o']=[B,A]
                        suitsDict[b+a+'o']='o'
                    else:
                        handDict[a+b+'s']=[A,B]
                        suitsDict[a+b+'s']='s'
                        handDict[a+b+'o']=[B,A]
                        suitsDict[a+b+'o']='o'
        verified.append(A)
    return handDict,suitsDict


class handButton:
    def __init__(self, root, name, handtype, action, X, Y):
        self.handtype = handtype
        self.action = action
        self.color = Chart.colorDict[self.action]
        self.button = Button(root, text=name, command=lambda: self.changeAction(), height = 1, width = 1, bg = self.color)
        self.button.place(x = X*35, y= Y*30)
    def changeAction(self):
        Chart.probabilities[self.action] -= Chart.handtypes[self.handtype]
        self.action = Chart.actionDict[self.action]
        Chart.probabilities[self.action] += Chart.handtypes[self.handtype]
        self.button["bg"]= Chart.colorDict[self.action]
    
class chartDicts:
    def __init__(self, root):
        self.actionDict = {'Fold':'Raise', 'Raise': 'Limp','Limp':'Call','Call':'All-in','All-in':'Mini-raise/Call All-in','Mini-raise/Call All-in':'Mini-raise/Fold All-in', 'Mini-raise/Fold All-in':'Call All-in', 'Call All-in': 'Fold'}
        self.colorDict = {'Fold':'#4D8A80','Raise':'#D54242','Limp':'#512E2E','Call':'#20DDBE','All-in':'#FF0404','Mini-raise/Call All-in':'#C63806','Mini-raise/Fold All-in':'#C1AB11','Call All-in':'#97947A'}
        self.probabilities = {'Fold': 100, 'Raise': 0,'Limp':0,'Call':0,'All-in':0,'Mini-raise/Call All-in':0,'Mini-raise/Fold All-in':0,'Call All-in':0}
        self.handtypes = {' ':(600/1326), 's':(400/1326), 'o':(1200/1326)}
        self.hands,self.suits = handsList()
        
    def addButtons(self, root):
        for name in self.hands.keys():
            handButton(root, name, self.suits[name], 'Fold', self.hands[name][0], self.hands[name][1])




Root = Tk()
Chart = chartDicts(Root)
Chart.addButtons(Root)
Root.geometry('460x395')
Root.mainloop() 
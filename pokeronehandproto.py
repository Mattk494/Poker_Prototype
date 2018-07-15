import random
import time

class Deck_Hands():

    Deck=[{'2S':2},{'3S':3},{'4S':4},{'5S':5},{'6S':6},{'7S':7},
        {'8S':8},{'9S':9},{'10S':10},{'JS':11},{'QS':12},{'KS':13},{'AS':14},
        {'2H':2},{'3H':3},{'4H':4},{'5H':5},{'6H':6},{'7H':7},
        {'8H':8},{'9H':9},{'10H':10},{'JH':11},{'QH':12},{'KH':13},{'AH':14},
        {'2C':2},{'3C':3},{'4C':4},{'5C':5},{'6C':6},{'7C':7},
        {'8C':8},{'9C':9},{'10C':10},{'JC':11},{'QC':12},{'KC':13},{'AC':14},
        {'2D':2},{'3D':3},{'4D':4},{'5D':5},{'6D':6},{'7D':7},
        {'8D':8},{'9D':9},{'10D':10},{'JD':11},{'QD':12},{'KD':13},{'AD':14}]

    Player1=[]
    Player2=[]
    Player3=[]
    Player4=[]


    Player1_chips=200
    Player2_chips=200
    Player3_chips=200
    Player4_chips=200

    Game=True

    pot=0


class Shuffle():
    def __init__(self):
        self.Deck=Deck_Hands.Deck
    def shuffle_the_deck(self):
        Deck_Hands.Deck=random.sample(self.Deck,len(self.Deck))
        print("Shuffling the Deck...")
        time.sleep(5)
        return Deck_Hands.Deck


class Order():
    hand_number=0

    def increase_handorder(self):
        if Order.hand_number <4:
            Order.hand_number+=1
            return (Order.hand_number)
        elif Order.hand_number >=4:
            Order.hand_number=1
            return (Order.hand_number)


class Deal(Order,Shuffle):
    Player1_Hand=list()
    Player2_Hand=list()
    Player3_Hand=list()
    Player4_Hand=list()
    def __init__(self,Shuffles,Orders):
        self.Deck=Shuffles.shuffle_the_deck()
        self.Orders=Orders.increase_handorder()

    def dealing(self):
        if self.Orders==1:


            for key in self.Deck[0:2]:
                for keys in key:
                    Deal.Player1_Hand.append(keys)

            for key in self.Deck[2:4]:
                for keys in key:
                    Deal.Player2_Hand.append(keys)

            for key in self.Deck[4:6]:
                for keys in key:
                    Deal.Player3_Hand.append(keys)

            for key in self.Deck[6:8]:
                for keys in key:
                    Deal.Player4_Hand.append(keys)


            Deck_Hands.Player1=[self.Deck[0],self.Deck[1]]
            Deck_Hands.Player2=[self.Deck[2],self.Deck[3]]
            Deck_Hands.Player3=[self.Deck[4],self.Deck[5]]
            Deck_Hands.Player4=[self.Deck[6],self.Deck[7]]
            print("Dealing the cards...")
            time.sleep(1)


class Flip():
    def __init__(self):
        self.Deck=Deck_Hands.Deck

    def Place_down(self):
        Table=''
        for key in self.Deck[8:11]:
            for keys in key:
                Table+= keys + " "
        print("Placing the Flop...")
        time.sleep(5)
        print(Table)

    def Place_Next(self):
        Table=''
        for key in self.Deck[8:12]:
            for keys in key:
                    Table+= keys + " "
            print("Placing the Turn..,")
            time.sleep(5)
            print(Table)

    def Place_Last(self):
        Table=''
        for key in self.Deck[8:13]:
            for keys in key:
                Table+= keys + " "
        print("Placing the River...")
        time.sleep(5)
        print(Table)

class preflop():
    Player1_Status=True
    Player2_Status=True
    Player3_Status=True
    Player4_Status=True

    def __init__(self):
        self.Order=Order.hand_number


    def Blind(self):
        Blind=True
        while Blind==True:
            if self.Order==1:
                Deck_Hands.Player2_chips+=-1
                print ("Player 2 has the small blind; Places 1 chip down")
                time.sleep(1)
                Deck_Hands.pot+=1

                Deck_Hands.Player3_chips+=-2
                print("Player 3 has the big blind;Places 2 chips down")
                time.sleep(1)
                Deck_Hands.pot+=2
                Blind=False



        if self.Order==1:
            Player4_input=input(" Player 4, Would You like to Call or Fold?")
            if Player4_input== "Call":
                Deck_Hands.Player4_chips+=-2
                print("Player 4 calls 2 chips")
                time.sleep(1)
                Deck_Hands.pot+=2

            elif Player4_input=='Fold':
                preflop.Player4_Status= False
                print("Player 4 Folded")
                time.sleep(1)


            Player1_input=input(" Player 1, Would You like to Call or Fold?")

            if Player1_input== "Call":
                Deck_Hands.Player1_chips+=-2
                print("Player 1 calls 2 chips")
                time.sleep(1)
                Deck_Hands.pot+=2

            elif Player1_input=='Fold':
                preflop.Player1_Status= False
                print("Player 1 Folded")
                time.sleep(1)

            Player2_input=input("Player 2, would you like to call by placing down one more chip?")
            if Player2_input=='Yes':
                Deck_Hands.Player2_chips+=-1
                print("Player 2 called")
                time.sleep(1)
                Deck_Hands.pot+=1

            elif Player2_input=='No':
                preflop.Player2_Status=False
                print("Player 2 folded")
                time.sleep(1)
                if Player1_input=='Fold' and Player2_input=="No" and Player4_input=="Fold":
                    print("Player 3 wins the hand")
                    time.sleep(1)
                    Deck_Hands.Game=False

        



class Betting():
    last_move=''
    current_bet=''


    def __init__(self):
        self.status1=preflop.Player1_Status
        self.status2=preflop.Player2_Status
        self.status3=preflop.Player3_Status
        self.status4=preflop.Player4_Status

        self.Order=Order.hand_number


    def Betting_time(self):
        Begin=True
        last_person=''

        if self.Order==1:
            while Begin==True and Deck_Hands.Game==True:

                if self.status2==True and (Betting.last_move!='Call4' and Betting.last_move!='Call3' and Betting.last_move!='Call1') and last_person!='Player 2':
                    Betting.last_move=input(" Player 2 Would you like to Bet or Check?")
                    time.sleep(1)
                    if Betting.last_move=='Bet':
                        current_bet=int(input("Enter your bet"))
                        time.sleep(1)
                        Deck_Hands.Player2_chips-= current_bet
                        print("Player 2 bets", current_bet)
                        Deck_Hands.pot+= current_bet
                        last_person='Player 2'
                        Betting.last_move="Call2"
                    elif Betting.last_move=='Check' and self.status3==False:
                            last_person='Player 2'
                            Begin=False
                    elif Betting.last_move=='Check':
                        print ("Player 2 Checks")
                        last_person='Player 2'

                if self.status2==True and (Betting.last_move=='Call4' or Betting.last_move=='Call3' or Betting.last_move=='Call1') and last_person!="Player 2":
                    move=input(" Player 2 Would you like to call the bet of {} Chips or would you like to Fold".format(current_bet))
                    time.sleep(1)
                    if move=="Call" and Deck_Hands.Player2_chips>= current_bet:
                        Deck_Hands.Player2_chips-= current_bet
                        print("Player 2 Calls", current_bet,"Chips")
                        time.sleep(1)
                        Deck_Hands.pot+= current_bet
                        last_person='Player 2'
                    if move=="Call" and Deck_Hands.Player2_chips< current_bet:
                        print("You Do not have enough chips to call. You have to fold!")
                        time.sleep(1)
                        print("Player 2 Folds")
                        time.sleep(1)
                        last_person='Player 2'
                        self.status2=False
                    if move=='Fold':
                        print("Player 2 Folds")
                        time.sleep(1)
                        last_person='Player 2'
                        self.status2=False

                if self.status3==True and (Betting.last_move!='Call4' and Betting.last_move!='Call2' and Betting.last_move!='Call1') and last_person!='Player 3':
                    Betting.last_move=input(" Player 3 Would you like to Bet or Check?")
                    time.sleep(1)
                    if Betting.last_move=='Bet':
                        current_bet=int(input("Enter your bet"))
                        time.sleep(1)
                        Deck_Hands.Player3_chips-= current_bet
                        print("Player 3 bets", current_bet)
                        time.sleep(1)
                        Deck_Hands.pot+= current_bet
                        last_person='Player 3'
                        Betting.last_move="Call3"
                    elif Betting.last_move=='Check' and self.status4==False:
                        last_person='Player 3'
                        Begin=False
                    elif Betting.last_move=='Check':
                        print ("Player 3 Checks")
                        time.sleep(1)
                        last_person='Player 3'

                if self.status3==True and (Betting.last_move=='Call4' or Betting.last_move=='Call2' or Betting.last_move=='Call1') and last_person!='Player 3':
                    move=input(" Player 3 Would you like to call the bet of {} Chips or would you like to Fold".format(current_bet))
                    time.sleep(1)
                    if move=="Call" and Deck_Hands.Player3_Card>= current_bet:
                        Deck_Hands.Player3_chips-= current_bet
                        print("Player 3 Calls", current_bet,"Chips")
                        time.sleep(1)
                        Deck_Hands.pot+= current_bet
                        last_person='Player 3'
                    if move=="Call" and Deck_Hands.Player3_Card < current_bet:
                        print("You Do not have enough chips to call. You have to fold!")
                        time.sleep(1)
                        print("Player 3 Folds")
                        time.sleep(1)
                        last_person='Player 3'
                        self.status3=False
                    if move=='Fold':
                        print('Player 3 Folds')
                        time.sleep(1)
                        last_person='Player 3'
                        self.status3=False

                if self.status4==True and (Betting.last_move!='Call3' and Betting.last_move!='Call2' and Betting.last_move!='Call1') and last_person!='Player 4':
                    Betting.last_move=input("Player 4 Would you like to Bet or Check?")
                    time.sleep(1)
                    if Betting.last_move=='Bet':
                        current_bet=int(input("Enter your bet"))
                        time.sleep(1)
                        Deck_Hands.Player4_chips-= current_bet
                        print("Player 4 bets", current_bet)
                        time.sleep(1)
                        Deck_Hands.pot+= current_bet
                        last_person='Player 4'
                        Betting.last_move="Call4"
                    elif Betting.last_move=='Check' and self.status1==False:
                        last_person='Player 4'
                        Begin=False
                    elif Betting.last_move=='Check':
                        print ("Player 4 Checks")
                        time.sleep(1)
                        last_person='Player 4'

                if self.status4==True and (Betting.last_move=='Call3' or Betting.last_move=='Call2' or Betting.last_move=='Call1') and last_person!='Player 4':
                    move=input(" Player 4 Would you like to call the bet of {} Chips or would you like to Fold".format(current_bet))
                    time.sleep(1)
                    if move=="Call" and Deck_Hands.Player4_chips>= current_bet:
                        Deck_Hands.Player4_chips-= current_bet
                        print("Player 4 Calls", current_bet,"Chips")
                        time.sleep(1)
                        Deck_Hands.pot+= current_bet
                        last_person='Player 4'
                    if move=="Call" and Deck_Hands.Player4_chips< current_bet:
                        print("You Do not have enough chips to call. You have to fold!")
                        time.sleep(1)
                        print("Player 4 Folds")
                        time.sleep(1)
                        last_person='Player 4'
                        self.status4=False
                    if move=='Fold':
                        print("Player 4 Folds")
                        time.sleep(1)
                        last_person='Player 4'
                        self.status4=False

                if self.status1==True and (Betting.last_move!='Call3' and Betting.last_move!='Call2' and Betting.last_move!='Call4') and last_person!='Player 1':
                    Betting.last_move=input("Player 1 Would you like to Bet or Check?")
                    time.sleep(1)
                    if Betting.last_move=='Bet':
                        current_bet=int(input("Enter your bet"))
                        time.sleep(1)
                        Deck_Hands.Player1_chips-= current_bet
                        print("Player 1 bets", current_bet)
                        time.sleep(1)
                        Deck_Hands.pot+= current_bet
                        last_person='Player 1'
                        Betting.last_move="Call1"
                    elif Betting.last_move=='Check':
                        print ("Player 1 Checks")
                        time.sleep(1)
                        last_person='Player 1'
                        Begin=False

                if self.status1==True and (Betting.last_move=='Call3' or Betting.last_move=='Call2' or Betting.last_move=='Call4') and last_person!='Player 1':
                    move=input(" Player 1 Would you like to call the bet of {} Chips or would you like to Fold".format(current_bet))
                    time.sleep(1)
                    if move=="Call" and Deck_Hands.Player1_chips >= current_bet:
                        Deck_Hands.Player1_chips-= current_bet
                        print("Player 1 Calls", current_bet,"Chips")
                        time.sleep(1)
                        Deck_Hands.pot+= current_bet
                        last_person='Player 1'
                    if move=="Call" and Deck_Hands.Player1_chips< current_bet:
                        print("You Do not have enough chips to call. You have to fold!")
                        time.sleep(1)
                        print("Player 1 Folds")
                        time.sleep(1)
                        last_person='Player 1'
                        self.status1=False
                    if move=='Fold':
                        print("Player 1 Folds")
                        time.sleep(1)
                        last_person='Player 1'
                        self.status1=False

                if self.status1==False and self.status2==False and self.status3==False:
                    print("Player 4 wins the hand and won {} chips".format(Deck_Hands.pot))
                    time.sleep(1)
                    Deck_Hands.Game=False

                elif self.status1==False and self.status2==False and self.status4==False:
                    print("Player 3 wins the hand and won {} chips".format(Deck_Hands.pot))
                    time.sleep(1)
                    Deck_Hands.Game=False

                elif self.status1==False and self.status3==False and self.status4==False:
                    print("Player 2 wins the hand and won {} chips".format(Deck_Hands.pot))
                    time.sleep(1)
                    Deck_Hands.Game=False

                elif self.status3==False and self.status2==False and self.status4==False:
                    print("Player 1 wins the hand and won {} chips".format(Deck_Hands.pot))
                    time.sleep(1)
                    Deck_Hands.Game=False









class Players_Hands():

    def __init__(self):
        self.Player1=Deck_Hands.Player1
        self.Player2=Deck_Hands.Player2
        self.Player3=Deck_Hands.Player3
        self.Player4=Deck_Hands.Player4

        self.cards_table=Deck_Hands.Deck[8:13]

    def create_hand(self):

        Player1=list()
        Player1_Cards=list()
        Player1.append(self.Player1)
        Player1.append(self.cards_table)

        for key in Player1:
            for keys in key:
                Player1_Cards.append(Keys)
        print("Player 1's Hand:", Player1_Cards)
        time.sleep(1)

        Player2=list()
        Player2_Cards=list()
        Player2.append(self.Player2)
        Player2.append(self.cards_table)

        for key in Player2:
            for keys in key:
                Player2_Cards.append(Keys)
        print("Player 2's Hand:", Player2_Cards)
        time.sleep(1)

        Player3=list()
        Player3_Cards=list()
        Player3.append(self.Player3)
        Player3.append(self.cards_table)

        for key in Player3:
            for keys in key:
                Player3_Cards.append(Keys)
        print("Player 3's Hand:", Player3_Cards)
        time.sleep(1)

        Player4=list()
        Player4_Cards=list()
        Player1.append(self.Player4)
        Player1.append(self.cards_table)

        for key in Player4:
            for keys in key:
                Player4_Cards.append(Keys)
        print("Player 4's Hand:", Player4_Cards)
        time.sleep(1)

        Strongest=input('Who had the best hand? Player1, Player2, Player3, Player4?')
        time.sleep(1)

        if Strongest=='Player1':
            print('Player 1 Won! and won', Deck_Hands.pot)
        elif Strongest=='Player2':
            print('Player 2 Won! and won', Deck_Hands.pot)
        elif Strongest=='Player3':
            print('Player 3 Won! and won', Deck_Hands.pot)
        elif Strongest=='Player4':
            print('Player 4 Won! and won', Deck_Hands.pot)


Play=input("Would You like to play poker?")
if Play=="Yes":
    y=Shuffle()
    r=Order()
    d=Deal(y,r)
    d.dealing()

    print("Player 1 hand is",Deal.Player1_Hand)
    print("Player 2 hand is",Deal.Player2_Hand)
    print("Player 3 hand is",Deal.Player3_Hand)
    print("Player 4 hand is",Deal.Player4_Hand)


    P= preflop()
    P.Blind()

    if Deck_Hands.Game==True:
        B=Betting()
        B.Betting_time()

    if Deck_Hands.Game==True:
        F=Flip()
        F.Place_down()

    if Deck_Hands.Game==True:
        B=Betting()
        B.Betting_time()

    if Deck_Hands.Game==True:
        F=Flip()
        F.Place_Next()

    if Deck_Hands.Game==True:
        B=Betting()
        B.Betting_time()

    if Deck_Hands.Game==True:
        F=Flip()
        F.Place_Last()

    if Deck_Hands.Game==True:
        B=Betting()
        B.Betting_time()

    if Deck_Hands.Game==True:
        H=Players_Hands()
        H.create_hand()

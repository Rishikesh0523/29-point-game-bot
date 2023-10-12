file = {
    "cards": ['9C', '9S', '8C', '8S'],
    "first-value-cards": ['JS', 'JC', 'JD', 'JH'],
    "second-value-cards": ['9S', '9C', '9D', '9H'],
    "third-value-cards": ['1S', '1C', '1D', '1H'],
    "fourth-value-cards": ['TS', 'TC', 'TD', 'TH'],
    "fifth-value-cards": ['KS', 'KC', 'KD', 'KH'],              #Differentiating value cards
    "sixth-value-cards": ['QS', 'QC', 'QD', 'QH'],
    "seventh-value-cards": ['8S', '8C', '8D', '8H'],
    "eighth-value-cards": ['7S', '7C', '7D', '7H'],
}                                                             
spade=diamond=club=heart=0
spadenonvalue_count=diamondnonvalue_count=clubnonvalue_count=heartnonvalue_count=0
value = [None]*4
value_card = [None]*4
for x in range(len(file["cards"])):
    if file["cards"][x] in file["first-value-cards"]:
        value[x] = 30
        value_card[x] = file["cards"][x]
    elif file["cards"][x] in file["second-value-cards"]:
        value[x] = 20
        value_card[x] = file["cards"][x]
    elif file["cards"][x] in file["third-value-cards"]:             #Separating value cards from non value cards
        value[x] = 15
        value_card[x] = file["cards"][x]
    elif file["cards"][x] in file["fourth-value-cards"]:
        value[x] = 13
        value_card[x] = file["cards"][x]
    else:
        if file["cards"][x][-1]=='S':
            spadenonvalue_count += 9
        if file["cards"][x][-1]=='C':
            clubnonvalue_count += 9                                    #Giving some point to non value card for bidding propose
        if file["cards"][x][-1]=='D':
            diamondnonvalue_count += 9
        if file["cards"][x][-1]=='H':
            heartnonvalue_count += 9
value_card_copy = value_card
total_value = 0
multiplier = 1.3
for x in range(len(value_card_copy)):
    if value_card_copy[x] != None:
        initial_value = value[x]
        count = 0
        for y in range(x+1, len(value_card_copy)):
            if (value_card_copy[x] != None) and (value_card_copy[y] != None):
                if value_card_copy[x][-1] == value_card_copy[y][-1]:
                    initial_value += value[y]
                    value_card_copy[y] = None
                    count += 1
        if count > 0:
            if value_card_copy[x][-1]=='S':
                spade=initial_value * multiplier + spadenonvalue_count + 0.004
            if value_card_copy[x][-1]=='C':
                club=initial_value * multiplier + clubnonvalue_count + 0.003
            if value_card_copy[x][-1]=='D':
                diamond=initial_value * multiplier + diamondnonvalue_count + 0.002           #Finding the total value of first for cards
            if value_card_copy[x][-1]=='H':                                            
                heart=initial_value * multiplier + heartnonvalue_count + 0.001
        else:
            if value_card_copy[x][-1]=='S':
                spade=initial_value
            if value_card_copy[x][-1]=='C':
                club=initial_value
            if value_card_copy[x][-1]=='D':
                diamond=initial_value
            if value_card_copy[x][-1]=='H':
                heart=initial_value
total_value= spade + club + diamond + heart
if total_value<50:
    maximum_bid=0
if total_value>50 and total_value<=65:
    maximum_bid=16
    bid=16
if total_value>65 and total_value<=77:
   maximum_bid=17
   bid=16
if total_value>77 and total_value<=101:                            #Setting bidding point base on total value of cards
    maximum_bid=18
    bid=16
if total_value>101:
    maximum_bid=19
    bid=16
trumph_max=max(spade,club,diamond,heart)
if(trumph_max==spade):
    trumph_card='S'
if(trumph_max==club):
    trumph_card='C'
if(trumph_max==diamond):                                           #Seting the trumph
    trumph_card='D'
if(trumph_max==heart):
    trumph_card='H'
print("Total value-",total_value)
print("Trumph card-",trumph_card)
print("You can bid maximum upto-",maximum_bid)


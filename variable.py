playing_cards={
    "spade": [ 'JS','9S','1S','TS','KS','QS','8S','7S'],
    "club": ['JC', '9C','1C','TC','KC','QC','8C','7C'],
    "diamond": ['JD', '9D','1D','TD','KD','QD','8D','7D'],
    "heart": ['JH', '9H','1H','TH','KH','QH','8H','7H']
} 
no_trumph=False
played_cards=['7C','8C','9C']
trumph=[False,None]
my_cards=['1H','JS','TH','8D','1D','TD','7D']               #Cards in my hand
my_spade=[None]*8
my_club=[None]*8
my_diamond=[None]*8                                            #Cards of particular colors
my_heart=[None]*8
throw_card=None
opponent1=[1,1,1,1]
opponent2=[1,1,1,1]                                          #state of cards
my_team=[1,1,1,1]
index=[None,None,None]
index_third=[None,None]
my_team=[1,1,1,1]
count=[0,0,0,0]                                                  #count of cards in my hand
throw_count1=[0,0,0,0]
throw_count2=[0,0,0,0]
total_count=[8,8,8,8]                                             #count of cards in gameplay
i=0
j=0
handsHistory=['A1',['JS','TD','9D','7C'],'B1']



# for i in range (len(handsHistory)):
#     if handsHistory[0][0]=='You-0':

print(playing_cards)
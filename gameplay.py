from variable import played_cards,my_spade,my_club,my_diamond,my_heart,throw_card,opponent1,opponent2,my_team,my_cards,count,index,index_third,throw_count1,throw_count2,total_count,playing_cards,no_trumph,played_cards,trumph

def playing(body):

  global played_cards,my_spade,my_club,my_diamond,my_heart,throw_card,opponent1,opponent2,my_team,my_cards,count,index,index_third,throw_count1,throw_count2,total_count,playing_cards,no_trumph,played_cards,trumph
  my_cards=body["cards"]
  played_cards=body["played"]


  if body["handsHistory"]!=[]:
    val = len(body["handsHistory"])-1
    for i in range(4):
        if body["handsHistory"][val][1][i][-1] == 'S':
            playing_cards["spade"].remove(body["handsHistory"][val][1][i])
            total_count[0] == len(playing_cards["spade"])
        if body["handsHistory"][val][1][i][-1] == 'C':
            playing_cards["club"].remove(body["handsHistory"][val][1][i])
            total_count[1] == len(playing_cards["club"])
        if body["handsHistory"][val][1][i][-1] == 'D':
            playing_cards["diamond"].remove(body["handsHistory"][val][1][i])
            total_count[2] == len(playing_cards["diamond"])
        if body["handsHistory"][val][1][i][-1] == 'H':
            playing_cards["heart"].remove(body["handsHistory"][val][1][i])
            total_count[3] == len(playing_cards["heart"])
    if body["handsHistory"][val][0] == "You-0":
        if body["handsHistory"][val][1][1][-1] == 'S':
            throw_count1[0] += 1
        elif body["handsHistory"][val][1][1][-1] == 'C':
            throw_count1[1] += 1
        elif body["handsHistory"][val][1][1][-1] == 'D':
            throw_count1[2] += 1
        elif body["handsHistory"][val][1][1][-1] == 'H':
            throw_count1[3] += 1
        if body["handsHistory"][val][1][3][-1] == 'S':
            throw_count2[0] += 1
        elif body["handsHistory"][val][1][3][-1] == 'C':
            throw_count2[1] += 1
        elif body["handsHistory"][val][1][3][-1] == 'D':
            throw_count2[2] += 1
        elif body["handsHistory"][val][1][3][-1] == 'H':
            throw_count2[3] += 1
    elif body["handsHistory"][val][0] == "You-1":
        if body["handsHistory"][val][1][1][-1] == 'S':
            throw_count2[0] += 1
        elif body["handsHistory"][val][1][1][-1] == 'C':
            throw_count2[1] += 1
        elif body["handsHistory"][val][1][1][-1] == 'D':
            throw_count2[2] += 1
        elif body["handsHistory"][val][1][1][-1] == 'H':
            throw_count2[3] += 1
        if body["handsHistory"][val][1][3][-1] == 'S':
            throw_count1[0] += 1
        elif body["handsHistory"][val][1][3][-1] == 'C':
            throw_count1[1] += 1
        elif body["handsHistory"][val][1][3][-1] == 'D':
            throw_count1[2] += 1
        elif body["handsHistory"][val][1][3][-1] == 'H':
            throw_count1[3] += 1
    elif body["handsHistory"][val][0] == "Opponent-0":
        if body["handsHistory"][val][1][0][-1] == 'S':
            throw_count1[0] += 1
        elif body["handsHistory"][val][1][0][-1] == 'C':
            throw_count1[1] += 1
        elif body["handsHistory"][val][1][0][-1] == 'D':
            throw_count1[2] += 1
        elif body["handsHistory"][val][1][0][-1] == 'H':
            throw_count1[3] += 1
        if body["handsHistory"][val][1][2][-1] == 'S':
            throw_count2[0] += 1
        elif body["handsHistory"][val][1][2][-1] == 'C':
            throw_count2[1] += 1
        elif body["handsHistory"][val][1][2][-1] == 'D':
            throw_count2[2] += 1
        elif body["handsHistory"][val][1][2][-1] == 'H':
            throw_count2[3] += 1
    elif body["handsHistory"][val][0] == "Opponent-1":
        if body["handsHistory"][val][1][0][-1] == 'S':
            throw_count2[0] += 1
        elif body["handsHistory"][val][1][0][-1] == 'C':
            throw_count2[1] += 1
        elif body["handsHistory"][val][1][0][-1] == 'D':
            throw_count2[2] += 1
        elif body["handsHistory"][val][1][0][-1] == 'H':
            throw_count2[3] += 1
        if body["handsHistory"][val][1][2][-1] == 'S':
            throw_count1[0] += 1
        elif body["handsHistory"][val][1][2][-1] == 'C':
            throw_count1[1] += 1
        elif body["handsHistory"][val][1][2][-1] == 'D':
            throw_count1[2] += 1
        elif body["handsHistory"][val][1][2][-1] == 'H':
            throw_count1[3] += 1
  

  # Arranging in descending order
  for i in range(len(my_cards)):
    if my_cards[i][-1]=='S':
      my_spade[count[0]]=my_cards[i]
      count[0] += 1
    elif my_cards[i][-1]=='C':
      my_club[count[1]]=my_cards[i]
      count[1]+=1
    elif my_cards[i][-1]=='D':
      my_diamond[count[2]]=my_cards[i]
      count[2]+=1
    elif my_cards[i][-1]=='H':
      my_heart[count[3]]=my_cards[i]
      count[3]+=1
  for i in range(count[0],8):
    my_spade.remove(None)                                            #Arranging the cards and keeping their count
  for i in range(count[1],8):
    my_club.remove(None)
  for i in range(count[2],8):
    my_diamond.remove(None)
  for i in range(count[3],8):
    my_heart.remove(None)
  if count[0]!=0:
    for i in range (count[0]):
      for j in range (i+1,count[0]):
        if playing_cards["spade"].index(my_spade[i])>playing_cards["spade"].index(my_spade[j]):
          temp=my_spade[i]
          my_spade[i]=my_spade[j]
          my_spade[j]=temp
  if count[1]!=0:
    for i in range (count[1]):
      for j in range (i+1,count[1]):
        if playing_cards["club"].index(my_club[i])>playing_cards["club"].index(my_club[j]):
          temp=my_club[i]
          my_club[i]=my_club[j]
          my_club[j]=temp
  if count[2]!=0:
    for i in range (count[2]):
      for j in range (i+1,count[2]):
        if playing_cards["diamond"].index(my_diamond[i])>playing_cards["diamond"].index(my_diamond[j]):
          temp=my_diamond[i]
          my_diamond[i]=my_diamond[j]
          my_diamond[j]=temp
  if count[3]!=0:
    for i in range (count[3]):
      for j in range (i+1,count[3]):
        if playing_cards["heart"].index(my_heart[i])>playing_cards["heart"].index(my_heart[j]):
          temp=my_heart[i]
          my_heart[i]=my_heart[j]
          my_heart[j]=temp
    my_cards= my_spade + my_club + my_diamond + my_heart
    
  def last_card_noncolour1(): 
    non_value_count=[0,0,0,0]
    do=0          
    possibility=[0,0,0,0]    
    check=-1    
    step=0 
    if(step==0):
      for i in range (sum(count)):
        if my_cards[i][0]=='J':
          if my_cards[i][-1]=='S' and (trumph[1]!='S' or trumph[1]==None):
            if (total_count[0]-count[0])<5:
              possibility[0]=1
          if my_cards[i][-1]=='C' and (trumph[1]!='C' or trumph[1]==None):
            if (total_count[1]-count[1])<5:
              possibility[1]=1
          if my_cards[i][-1]=='D' and (trumph[1]!='D' or trumph[1]==None):                      #throws J if that color is almost used and that is not the trumph we set
            if (total_count[2]-count[2])<5:
              possibility[2]=1
          if my_cards[i][-1]=='H' and (trumph[1]!='H' or trumph[1]==None):
            if (total_count[3]-count[3])<5:
              possibility[3]=1
      for i in range(len(possibility)):
        if(possibility[i]==1):
          step=1
          if (count[i]>check):
            check=count[i]
            n=i
      if(step==1):
        if(n==0):
          count[0]=count[0]-1
          my_spade.remove('JS')
          my_cards.remove('JS')
          throw_card='JS'
        if(n==1):
          count[1]=count[1]-1
          my_club.remove('JC')
          my_cards.remove('JC')
          throw_card='JC'
        if(n==2):
          count[2]=count[2]-1
          my_diamond.remove('JD')
          my_cards.remove('JD')
          throw_card='JD'
        if(n==3):
          count[3]=count[3]-1
          my_heart.remove('JH')
          my_cards.remove('JH')
          throw_card='JH'
    if(step==0):
      possibility=[0,0,0,0]    
      check=10     
      for i in range (sum(count)):
        if my_cards[i][0]=='9':
          if my_cards[i][-1]=='S' and (trumph[1]!='S' or trumph[1]==None):
            possibility[0]=1
          if my_cards[i][-1]=='C' and (trumph[1]!='C' or trumph[1]==None):
            possibility[1]=1
          if my_cards[i][-1]=='D' and (trumph[1]!='D' or trumph[1]==None):
            possibility[2]=1
          if my_cards[i][-1]=='H' and (trumph[1]!='H' or trumph[1]==None):
            possibility[3]=1
      for i in range(len(possibility)):                                   #if not J throws 9 and that is not trumph we set
        if(possibility[i]==1):
          step=1
          if (count[i]<=check) and count[i]!=0:
            check=count[i]
            n=i
      if(step==1):
        if(n==0):
          count[0]=count[0]-1
          my_spade.remove('9S')
          my_cards.remove('9S')
          throw_card='9S'
        if(n==1):
          count[1]=count[1]-1
          my_club.remove('9C')
          my_cards.remove('9C')
          throw_card='9C'
        if(n==2):
          count[2]=count[2]-1
          my_diamond.remove('9D')
          my_cards.remove('9D')
          throw_card='9D'
        if(n==3):
          count[3]=count[3]-1
          my_heart.remove('9H')
          my_cards.remove('9H')
          throw_card='9H'
    if(step==0):
      possibility=[0,0,0,0]    
      check=10     
      for i in range (sum(count)):
        if my_cards[i][0]=='1':
          if my_cards[i][-1]=='S' and (trumph[1]!='S' or trumph[1]==None):
            possibility[0]=1
          if my_cards[i][-1]=='C' and (trumph[1]!='C' or trumph[1]==None):
            possibility[1]=1
          if my_cards[i][-1]=='D' and (trumph[1]!='D' or trumph[1]==None):
            possibility[2]=1
          if my_cards[i][-1]=='H' and (trumph[1]!='H' or trumph[1]==None):
            possibility[3]=1
      for i in range(len(possibility)):
        if(possibility[i]==1):
          step=1
          if (count[i]<check) and count[i]!=0:                                                    #if not 9 throws 1 and that is not trumph we set
            check=count[i]
            n=i
      if(step==1):
        if(n==0):
          count[0]=count[0]-1
          my_spade.remove('1S')
          my_cards.remove('1S')
          throw_card='1S'
        if(n==1):
          count[1]=count[1]-1
          my_club.remove('1C')
          my_cards.remove('1C')
          throw_card='1C'
        if(n==2):
          count[2]=count[2]-1
          my_diamond.remove('1D')
          my_cards.remove('1D')
          throw_card='1D'
        if(n==3):
          count[3]=count[3]-1
          my_heart.remove('1H')
          my_cards.remove('1H')
          throw_card='1H'
    if(step==0):
      possibility=[0,0,0,0]    
      check=10     
      for i in range (sum(count)):
        if my_cards[i][0]=='T':
          if my_cards[i][-1]=='S' and (trumph[1]!='S' or trumph[1]==None):
            possibility[0]=1
          if my_cards[i][-1]=='C' and (trumph[1]!='C' or trumph[1]==None):
            possibility[1]=1
          if my_cards[i][-1]=='D' and (trumph[1]!='D' or trumph[1]==None):
            possibility[2]=1
          if my_cards[i][-1]=='H' and (trumph[1]!='H' or trumph[1]==None):
            possibility[3]=1
      for i in range(len(possibility)):
        if(possibility[i]==1):
          step=1
          if (count[i]<check) and count[i]!=0:
            check=count[i]
            n=i
      if(step==1):
        if(n==0):
          count[0]=count[0]-1
          my_spade.remove('TS')
          my_cards.remove('TS')
          throw_card='TS'
        if(n==1):                                                                 #if not 1 throws T and that is not trumph we set
          count[1]=count[1]-1
          my_club.remove('TC')
          my_cards.remove('TC')
          throw_card='TC'
        if(n==2):
          count[2]=count[2]-1
          my_diamond.remove('TD')
          my_cards.remove('TD')
          throw_card='TD'
        if(n==3):
          count[3]=count[3]-1
          my_heart.remove('TH')
          my_cards.remove('TH')
          throw_card='TH'
    if (step==0):
      for i in range(len(my_cards)):
          if my_cards[i][-1]=='S' and (my_cards[i][0]!='J' and my_cards[i][0]!='9' and my_cards[i][0]!='1' and my_cards[i][0]!='T'):
            non_value_count[0]+=1
          if my_cards[i][-1]=='C' and (my_cards[i][0]!='J' and my_cards[i][0]!='9' and my_cards[i][0]!='1' and my_cards[i][0]!='T'):
            non_value_count[1]+=1
          if my_cards[i][-1]=='D' and (my_cards[i][0]!='J' and my_cards[i][0]!='9' and my_cards[i][0]!='1' and my_cards[i][0]!='T'):
            non_value_count[2]+=1
          if my_cards[i][-1]=='H' and (my_cards[i][0]!='J' and my_cards[i][0]!='9' and my_cards[i][0]!='1' and my_cards[i][0]!='T'):
            non_value_count[3]+=1
      if non_value_count[0]!=0 and my_spade[0][0]=='J':
        non_value_count[0]+=1
      if non_value_count[1]!=0 and my_club[0][0]=='J':
        non_value_count[1]+=1
      if non_value_count[2]!=0 and my_diamond[0][0]=='J':
        non_value_count[2]+=1 
      if non_value_count[3]!=0 and my_heart[0][0]=='J':
        non_value_count[3]+=1
    if (step==0):
      min_non_value = sorted([x for x in non_value_count if x != 0])
      if min_non_value!=[]:
        if ((len(min_non_value))==1):
          min_non_value.append(None)
        if (non_value_count[0]==min_non_value[0]) and ((min_non_value[0]!=min_non_value[1]) or (min_non_value[0]==1)) and (trumph[1]!='S' or trumph[1]==None):
          throw_card=my_spade[count[0]-1]
          my_spade.pop(count[0]-1)
          count[0]=count[0]-1
          my_cards.remove(throw_card)
        elif (non_value_count[1]==min_non_value[0]) and ((min_non_value[0]!=min_non_value[1]) or (min_non_value[0]==1)) and (trumph[1]!='C' or trumph[1]==None):
          throw_card=my_club[count[1]-1]
          my_club.pop(count[1]-1)
          count[1]=count[1]-1
          my_cards.remove(throw_card)
        elif (non_value_count[2]==min_non_value[0]) and ((min_non_value[0]!=min_non_value[1]) or (min_non_value[0]==1)) and (trumph[1]!='D' or trumph[1]==None):
          throw_card=my_diamond[count[2]-1]
          my_diamond.pop(count[2]-1)
          count[2]=count[2]-1
          my_cards.remove(throw_card)

        elif (non_value_count[3]==min_non_value[0]) and ((min_non_value[0]!=min_non_value[1]) or (min_non_value[0]==1)) and (trumph[1]!='H' or trumph[1]==None):
          throw_card=my_heart[count[3]-1]
          my_heart.pop(count[3]-1)
          count[3]=count[3]-1
          my_cards.remove(throw_card)
        else:
          do=69
      else:
        do=69
    if(do==69):
      if(step==0):
        possibility=[0,0,0,0]    
        check=10     
        for i in range (sum(count)):
          if my_cards[i][0]=='7':
            if my_cards[i][-1]=='S' and (trumph[1]!='S' or trumph[1]==None):
              possibility[0]=1
            if my_cards[i][-1]=='C' and (trumph[1]!='C' or trumph[1]==None):
              possibility[1]=1
            if my_cards[i][-1]=='D' and (trumph[1]!='D' or trumph[1]==None):
              possibility[2]=1
            if my_cards[i][-1]=='H' and (trumph[1]!='H' or trumph[1]==None):
              possibility[3]=1
        for i in range(len(possibility)):
          if(possibility[i]==1):
            step=1
            if (count[i]<check) and count[i]!=0:
              check=count[i]
              n=i
        if(step==1):
          if(n==0):
            count[0]=count[0]-1
            my_cards.remove('7S')
            my_spade.remove('7S')
            throw_card='7S'
          if(n==1):                                                                 #if not T throws 7 and that is not trumph we set
            count[1]=count[1]-1
            my_club.remove('7C')
            my_cards.remove('7C')
            throw_card='7C'
          if(n==2):
            count[2]=count[2]-1
            my_diamond.remove('7D')
            my_cards.remove('7D')
            throw_card='7D'
          if(n==3):
            count[3]=count[3]-1
            my_heart.remove('7H')
            my_cards.remove('7H')
            throw_card='7H'
      if(step==0):
        possibility=[0,0,0,0]    
        check=10     
        for i in range (sum(count)):
          if my_cards[i][0]=='8':
            if my_cards[i][-1]=='S' and (trumph[1]!='S' or trumph[1]==None):
              possibility[0]=1
            if my_cards[i][-1]=='C' and (trumph[1]!='C' or trumph[1]==None):
              possibility[1]=1
            if my_cards[i][-1]=='D' and (trumph[1]!='D' or trumph[1]==None):
              possibility[2]=1
            if my_cards[i][-1]=='H' and (trumph[1]!='H' or trumph[1]==None):
              possibility[3]=1
        for i in range(len(possibility)):
          if(possibility[i]==1):
            step=1
            if (count[i]<check) and count[i]!=0:
              check=count[i]
              n=i
        if(step==1):
          if(n==0):
            count[0]=count[0]-1
            my_spade.remove('8S')
            my_cards.remove('8S')
            throw_card='8S'
          if(n==1):                                                                 #if not 7 throws 8 and that is not trumph we set
            count[1]=count[1]-1
            my_club.remove('8C')
            my_cards.remove('8C')
            throw_card='8C'
          if(n==2):
            count[2]=count[2]-1
            my_diamond.remove('8D')
            my_cards.remove('8D')
            throw_card='8D'
          if(n==3):
            count[3]=count[3]-1
            my_heart.remove('8H')
            my_cards.remove('8H')
            throw_card='8H'
      if(step==0):
        possibility=[0,0,0,0]    
        check=10     
        for i in range (sum(count)):
          if my_cards[i][0]=='Q':
            if my_cards[i][-1]=='S' and (trumph[1]!='S' or trumph[1]==None):
              possibility[0]=1
            if my_cards[i][-1]=='C' and (trumph[1]!='C' or trumph[1]==None):
              possibility[1]=1
            if my_cards[i][-1]=='D' and (trumph[1]!='D' or trumph[1]==None):
              possibility[2]=1
            if my_cards[i][-1]=='H' and (trumph[1]!='H' or trumph[1]==None):
              possibility[3]=1
        for i in range(len(possibility)):
          if(possibility[i]==1):
            step=1
            if (count[i]<check) and count[i]!=0:
              check=count[i]
              n=i
        if(step==1):
          if(n==0):
            count[0]=count[0]-1
            my_spade.remove('QS')
            my_cards.remove('QS')
            throw_card='QS'
          if(n==1):                                                                 #if not 8 throws Q and that is not trumph we set
            count[1]=count[1]-1
            my_club.remove('QC')
            my_cards.remove('QC')
            throw_card='QC'
          if(n==2):
            count[2]=count[2]-1
            my_diamond.remove('QD')
            my_cards.remove('QD')
            throw_card='QD'
          if(n==3):
            count[3]=count[3]-1
            my_heart.remove('QH')
            my_cards.remove('QH')
            throw_card='QH'
      if(step==0):
        possibility=[0,0,0,0]    
        check=10     
        for i in range (sum(count)):
          if my_cards[i][0]=='K':
            if my_cards[i][-1]=='S' and (trumph[1]!='S' or trumph[1]==None):
              possibility[0]=1
            if my_cards[i][-1]=='C' and (trumph[1]!='C' or trumph[1]==None):
              possibility[1]=1
            if my_cards[i][-1]=='D' and (trumph[1]!='D' or trumph[1]==None):
              possibility[2]=1
            if my_cards[i][-1]=='H' and (trumph[1]!='H' or trumph[1]==None):
              possibility[3]=1
        for i in range(len(possibility)):
          if(possibility[i]==1):
            step=1
            if (count[i]<check) and count[i]!=0:
              check=count[i]
              n=i
        if(step==1):
          if(n==0):
            count[0]=count[0]-1
            my_spade.remove('KS')
            my_cards.remove('KS')
            throw_card='KS'
          if(n==1):                                                                 #if not Q throws K and that is not trumph we set
            count[1]=count[1]-1
            my_club.remove('KC')
            my_cards.remove('KC')
            throw_card='KC'
          if(n==2):
            count[2]=count[2]-1
            my_diamond.remove('KD')
            my_cards.remove('KD')
            throw_card='KD'
          if(n==3):
            count[3]=count[3]-1
            my_heart.remove('KH')
            my_cards.remove('KH')
            throw_card='KH'
      if (step==0):
        throw_card=my_cards[sum(count)-1]
        if my_cards[sum(count)-1][-1]=='S':
          count[0]=count[0]-1
          my_spade.remove(throw_card)
        if my_cards[sum(count)-1][-1]=='C':
          count[1]=count[1]-1
          my_club.remove(throw_card)
        if my_cards[sum(count)-1][-1]=='D':
          count[2]=count[2]-1
          my_diamond.remove(throw_card)
        if my_cards[sum(count)-1][-1]=='H':
          count[3]=count[3]-1
          my_heart.remove(throw_card)
        my_cards.remove(throw_card)
    return(throw_card)

  def last_card_noncolour3():
    step=0
    non_value_count=[0,0,0,0]
    for i in range(len(my_cards)):
      if my_cards[i][-1]=='S' and (my_cards[i][0]!='J' and my_cards[i][0]!='9' and my_cards[i][0]!='1' and my_cards[i][0]!='T'):
        non_value_count[0]+=1
      if my_cards[i][-1]=='C' and (my_cards[i][0]!='J' and my_cards[i][0]!='9' and my_cards[i][0]!='1' and my_cards[i][0]!='T'):
        non_value_count[1]+=1
      if my_cards[i][-1]=='D' and (my_cards[i][0]!='J' and my_cards[i][0]!='9' and my_cards[i][0]!='1' and my_cards[i][0]!='T'):
        non_value_count[2]+=1
      if my_cards[i][-1]=='H' and (my_cards[i][0]!='J' and my_cards[i][0]!='9' and my_cards[i][0]!='1' and my_cards[i][0]!='T'):
        non_value_count[3]+=1
    if (non_value_count[0]!=0):
      for i in range (len(my_spade)):
        if my_spade[i][0]=='J' or my_spade[i][0]=='9' or my_spade[i][0]=='1' or my_spade[i][0]=='T':
          non_value_count[0]+=1
    if (non_value_count[1]!=0):
      for i in range (len(my_club)):
        if my_club[i][0]=='J' or my_club[i][0]=='9' or my_club[i][0]=='1' or my_club[i][0]=='T':
          non_value_count[1]+=1
    if (non_value_count[2]!=0):
      for i in range (len(my_diamond)):
        if my_diamond[i][0]=='J' or my_diamond[i][0]=='9' or my_diamond[i][0]=='1' or my_diamond[i][0]=='T':
          non_value_count[2]+=1
    if (non_value_count[3]!=0):
      for i in range (len(my_heart)):
        if my_heart[i][0]=='J' or my_heart[i][0]=='9' or my_heart[i][0]=='1' or my_heart[i][0]=='T':
          non_value_count[3]+=1
    min_non_value = sorted([x for x in non_value_count if x != 0])
    if min_non_value!=[]:
      if ((len(min_non_value))==1):
        min_non_value.append(None)
      if ((non_value_count[0]==min_non_value[0]) and ((min_non_value[0]!=min_non_value[1]) or (min_non_value[0]==1) or ((len(min_non_value))==1))):
        throw_card=my_spade[count[0]-1]
        my_spade.pop(count[0]-1)
        count[0]=count[0]-1
        my_cards.remove(throw_card)
        step=1
      elif ((non_value_count[1]==min_non_value[0]) and ((min_non_value[0]!=min_non_value[1]) or (min_non_value[0]==1) or ((len(min_non_value))==1))):
        throw_card=my_club[count[1]-1]
        my_club.pop(count[1]-1)
        count[1]=count[1]-1
        my_cards.remove(throw_card)
        step=1
      elif ((non_value_count[2]==min_non_value[0]) and ((min_non_value[0]!=min_non_value[1]) or (min_non_value[0]==1) or ((len(min_non_value))==1))):
        throw_card=my_diamond[count[2]-1]
        my_diamond.pop(count[2]-1)
        count[2]=count[2]-1
        my_cards.remove(throw_card)
        step=1

      elif ((non_value_count[3]==min_non_value[0]) and ((min_non_value[0]!=min_non_value[1]) or (min_non_value[0]==1) or ((len(min_non_value))==1))):
        throw_card=my_heart[count[3]-1]
        my_heart.pop(count[3]-1)
        count[3]=count[3]-1
        my_cards.remove(throw_card)
        step=1
      else:
        step=0
    if(step==0):
      possibility=[0,0,0,0]    
      check=10     
      for i in range (sum(count)):
        if my_cards[i][0]=='7':
          if my_cards[i][-1]=='S' and (trumph[1]!='S' or trumph[1]==None):
            possibility[0]=1
          if my_cards[i][-1]=='C' and (trumph[1]!='C' or trumph[1]==None):
            possibility[1]=1
          if my_cards[i][-1]=='D' and (trumph[1]!='D' or trumph[1]==None):
            possibility[2]=1
          if my_cards[i][-1]=='H' and (trumph[1]!='H' or trumph[1]==None):
            possibility[3]=1
      for i in range(len(possibility)):
        if(possibility[i]==1):
          step=1
          if (count[i]<check) and count[i]!=0:
            check=count[i]
            n=i
      if(step==1):
        if(n==0):
          count[0]=count[0]-1
          my_cards.remove('7S')
          my_spade.remove('7S')
          throw_card='7S'
        if(n==1):                                                                 #if not T throws 7 and that is not trumph we set
          count[1]=count[1]-1
          my_club.remove('7C')
          my_cards.remove('7C')
          throw_card='7C'
        if(n==2):
          count[2]=count[2]-1
          my_diamond.remove('7D')
          my_cards.remove('7D')
          throw_card='7D'
        if(n==3):
          count[3]=count[3]-1
          my_heart.remove('7H')
          my_cards.remove('7H')
          throw_card='7H'
    if(step==0):
      possibility=[0,0,0,0]    
      check=10     
      for i in range (sum(count)):
        if my_cards[i][0]=='8':
          if my_cards[i][-1]=='S' and (trumph[1]!='S' or trumph[1]==None):
            possibility[0]=1
          if my_cards[i][-1]=='C' and (trumph[1]!='C' or trumph[1]==None):
            possibility[1]=1
          if my_cards[i][-1]=='D' and (trumph[1]!='D' or trumph[1]==None):
            possibility[2]=1
          if my_cards[i][-1]=='H' and (trumph[1]!='H' or trumph[1]==None):
            possibility[3]=1
      for i in range(len(possibility)):
        if(possibility[i]==1):
          step=1
          if (count[i]<check) and count[i]!=0:
            check=count[i]
            n=i
      if(step==1):
        if(n==0):
          count[0]=count[0]-1
          my_spade.remove('8S')
          my_cards.remove('8S')
          throw_card='8S'
        if(n==1):                                                                 #if not 7 throws 8 and that is not trumph we set
          count[1]=count[1]-1
          my_club.remove('8C')
          my_cards.remove('8C')
          throw_card='8C'
        if(n==2):
          count[2]=count[2]-1
          my_diamond.remove('8D')
          my_cards.remove('8D')
          throw_card='8D'
        if(n==3):
          count[3]=count[3]-1
          my_heart.remove('8H')
          my_cards.remove('8H')
          throw_card='8H'
    if(step==0):
      possibility=[0,0,0,0]    
      check=10     
      for i in range (sum(count)):
        if my_cards[i][0]=='Q':
          if my_cards[i][-1]=='S' and (trumph[1]!='S' or trumph[1]==None):
            possibility[0]=1
          if my_cards[i][-1]=='C' and (trumph[1]!='C' or trumph[1]==None):
            possibility[1]=1
          if my_cards[i][-1]=='D' and (trumph[1]!='D' or trumph[1]==None):
            possibility[2]=1
          if my_cards[i][-1]=='H' and (trumph[1]!='H' or trumph[1]==None):
            possibility[3]=1
      for i in range(len(possibility)):
        if(possibility[i]==1):
          step=1
          if (count[i]<check) and count[i]!=0:
            check=count[i]
            n=i
      if(step==1):
        if(n==0):
          count[0]=count[0]-1
          my_spade.remove('QS')
          my_cards.remove('QS')
          throw_card='QS'
        if(n==1):                                                                 #if not 8 throws Q and that is not trumph we set
          count[1]=count[1]-1
          my_club.remove('QC')
          my_cards.remove('QC')
          throw_card='QC'
        if(n==2):
          count[2]=count[2]-1
          my_diamond.remove('QD')
          my_cards.remove('QD')
          throw_card='QD'
        if(n==3):
          count[3]=count[3]-1
          my_heart.remove('QH')
          my_cards.remove('QH')
          throw_card='QH'
    if(step==0):
      possibility=[0,0,0,0]    
      check=10     
      for i in range (sum(count)):
        if my_cards[i][0]=='K':
          if my_cards[i][-1]=='S' and (trumph[1]!='S' or trumph[1]==None):
            possibility[0]=1
          if my_cards[i][-1]=='C' and (trumph[1]!='C' or trumph[1]==None):
            possibility[1]=1
          if my_cards[i][-1]=='D' and (trumph[1]!='D' or trumph[1]==None):
            possibility[2]=1
          if my_cards[i][-1]=='H' and (trumph[1]!='H' or trumph[1]==None):
            possibility[3]=1
      for i in range(len(possibility)):
        if(possibility[i]==1):
          step=1
          if (count[i]<check) and count[i]!=0:
            check=count[i]
            n=i
      if(step==1):
        if(n==0):
          count[0]=count[0]-1
          my_spade.remove('KS')
          my_cards.remove('KS')
          throw_card='KS'
        if(n==1):                                                                 #if not Q throws K and that is not trumph we set
          count[1]=count[1]-1
          my_club.remove('KC')
          my_cards.remove('KC')
          throw_card='KC'
        if(n==2):
          count[2]=count[2]-1
          my_diamond.remove('KD')
          my_cards.remove('KD')
          throw_card='KD'
        if(n==3):
          count[3]=count[3]-1
          my_heart.remove('KH')
          my_cards.remove('KH')
          throw_card='KH'
    if(step==0):
      possibility=[0,0,0,0]    
      check=10     
      for i in range (sum(count)):
        if my_cards[i][0]=='T':
          if my_cards[i][-1]=='S' and (trumph[1]!='S' or trumph[1]==None):
            possibility[0]=1
          if my_cards[i][-1]=='C' and (trumph[1]!='C' or trumph[1]==None):
            possibility[1]=1
          if my_cards[i][-1]=='D' and (trumph[1]!='D' or trumph[1]==None):
            possibility[2]=1
          if my_cards[i][-1]=='H' and (trumph[1]!='H' or trumph[1]==None):
            possibility[3]=1
      for i in range(len(possibility)):
        if(possibility[i]==1):
          step=1
          if (count[i]<check) and count[i]!=0:
            check=count[i]
            n=i
      if(step==1):
        if(n==0):
          count[0]=count[0]-1
          my_spade.remove('TS')
          my_cards.remove('TS')
          throw_card='TS'
        if(n==1):                                                                 #if not 1 throws T and that is not trumph we set
          count[1]=count[1]-1
          my_club.remove('TC')
          my_cards.remove('TC')
          throw_card='TC'
        if(n==2):
          count[2]=count[2]-1
          my_diamond.remove('TD')
          my_cards.remove('TD')
          throw_card='TD'
        if(n==3):
          count[3]=count[3]-1
          my_heart.remove('TH')
          my_cards.remove('TH')
          throw_card='TH'
    if(step==0):
      possibility=[0,0,0,0]    
      check=10     
      for i in range (sum(count)):
        if my_cards[i][0]=='1':
          if my_cards[i][-1]=='S' and (trumph[1]!='S' or trumph[1]==None):
            possibility[0]=1
          if my_cards[i][-1]=='C' and (trumph[1]!='C' or trumph[1]==None):
            possibility[1]=1
          if my_cards[i][-1]=='D' and (trumph[1]!='D' or trumph[1]==None):
            possibility[2]=1
          if my_cards[i][-1]=='H' and (trumph[1]!='H' or trumph[1]==None):
            possibility[3]=1
      for i in range(len(possibility)):
        if(possibility[i]==1):
          step=1
          if (count[i]<check) and count[i]!=0:                                                    #if not 9 throws 1 and that is not trumph we set
            check=count[i]
            n=i
      if(step==1):
        if(n==0):
          count[0]=count[0]-1
          my_spade.remove('1S')
          my_cards.remove('1S')
          throw_card='1S'
        if(n==1):
          count[1]=count[1]-1
          my_club.remove('1C')
          my_cards.remove('1C')
          throw_card='1C'
        if(n==2):
          count[2]=count[2]-1
          my_diamond.remove('1D')
          my_cards.remove('1D')
          throw_card='1D'
        if(n==3):
          count[3]=count[3]-1
          my_heart.remove('1H')
          my_cards.remove('1H')
          throw_card='1H'
    if(step==0):
      possibility=[0,0,0,0]    
      check=10     
      for i in range (sum(count)):
        if my_cards[i][0]=='9':
          if my_cards[i][-1]=='S' and (trumph[1]!='S' or trumph[1]==None):
            possibility[0]=1
          if my_cards[i][-1]=='C' and (trumph[1]!='C' or trumph[1]==None):
            possibility[1]=1
          if my_cards[i][-1]=='D' and (trumph[1]!='D' or trumph[1]==None):
            possibility[2]=1
          if my_cards[i][-1]=='H' and (trumph[1]!='H' or trumph[1]==None):
            possibility[3]=1
      for i in range(len(possibility)):                                   #if not J throws 9 and that is not trumph we set
        if(possibility[i]==1):
          step=1
          if (count[i]<=check) and count[i]!=0:
            check=count[i]
            n=i
      if(step==1):
        if(n==0):
          count[0]=count[0]-1
          my_spade.remove('9S')
          my_cards.remove('9S')
          throw_card='9S'
        if(n==1):
          count[1]=count[1]-1
          my_club.remove('9C')
          my_cards.remove('9C')
          throw_card='9C'
        if(n==2):
          count[2]=count[2]-1
          my_diamond.remove('9D')
          my_cards.remove('9D')
          throw_card='9D'
        if(n==3):
          count[3]=count[3]-1
          my_heart.remove('9H')
          my_cards.remove('9H')
          throw_card='9H'
    if(step==0):
      possibility=[0,0,0,0]    
      check=10     
      for i in range (sum(count)):
        if my_cards[i][0]=='J':
          if my_cards[i][-1]=='S' and (trumph[1]!='S' or trumph[1]==None):
            possibility[0]=1
          if my_cards[i][-1]=='C' and (trumph[1]!='C' or trumph[1]==None):
            possibility[1]=1
          if my_cards[i][-1]=='D' and (trumph[1]!='D' or trumph[1]==None):
            possibility[2]=1
          if my_cards[i][-1]=='H' and (trumph[1]!='H' or trumph[1]==None):
            possibility[3]=1
      for i in range(len(possibility)):                                   #if not J throws 9 and that is not trumph we set
        if(possibility[i]==1):
          step=1
          if (count[i]<=check) and count[i]!=0:
            check=count[i]
            n=i
      if(step==1):
        if(n==0):
          count[0]=count[0]-1
          my_spade.remove('JS')
          my_cards.remove('JS')
          throw_card='JS'
        if(n==1):
          count[1]=count[1]-1
          my_club.remove('JC')
          my_cards.remove('JC')
          throw_card='JC'
        if(n==2):
          count[2]=count[2]-1
          my_diamond.remove('JD')
          my_cards.remove('JD')
          throw_card='JD'
        if(n==3):
          count[3]=count[3]-1
          my_heart.remove('JH')
          my_cards.remove('JH')
          throw_card='JH'
    if (step==0):
      throw_card=my_cards[sum(count)-1]
      if my_cards[sum(count)-1][-1]=='S':
        count[0]=count[0]-1
        my_spade.remove(throw_card)
      if my_cards[sum(count)-1][-1]=='C':
        count[1]=count[1]-1
        my_club.remove(throw_card)
      if my_cards[sum(count)-1][-1]=='D':
        count[2]=count[2]-1
        my_diamond.remove(throw_card)
      if my_cards[sum(count)-1][-1]=='H':
        count[3]=count[3]-1
        my_heart.remove(throw_card)
      my_cards.remove(throw_card)
    return(throw_card)
    
  def last_card_noncolour2(round_winner):
    if (round_winner>=0):
      if (trumph[0]==False):
        trumph[0]=True
        return {"revealTrump": True}
      if no_trumph==False:
        trumph[1]=body["trumpSuit"]  #put here what trumph_suit is
      if trumph[1]=='S':
        if count[0]!=0:
          throw_card=my_spade[count[0]-1]
          my_spade.pop(count[0]-1)
          count[0]=count[0]-1
          my_cards.remove(throw_card)
        elif count[0]==0:
          throw_card=last_card_noncolour3()
      if trumph[1]=='C':
        if count[1]!=0:
          throw_card=my_club[count[1]-1]
          my_club.pop(count[1]-1)
          count[1]=count[1]-1
          my_cards.remove(throw_card)
        elif count[1]==0:
          throw_card=last_card_noncolour3()
      if trumph[1]=='D':
        if count[2]!=0:
          throw_card=my_diamond[count[2]-1]
          my_diamond.pop(count[2]-1)
          count[2]=count[2]-1
          my_cards.remove(throw_card)
        elif count[2]==0:
          throw_card=last_card_noncolour3()
      if trumph[1]=='H':
        if count[3]!=0:
          throw_card=my_heart[count[3]-1]
          my_heart.pop(count[3]-1)
          count[3]=count[3]-1
          my_cards.remove(throw_card)
        elif count[3]==0:
          throw_card=last_card_noncolour3()
      
    elif(round_winner<0):
      if trumph[1]=='S':
        if count[0]!=0:
          for i in range(count[0]-1,-1,-1):
            if (my_spade[i][0]=='J'):
              check_index=-8
            elif (my_spade[i][0]=='9'):
              check_index=-7
            elif (my_spade[i][0]=='A'):
              check_index=-6
            elif (my_spade[i][0]=='T'):
              check_index=-5
            elif (my_spade[i][0]=='K'):
              check_index=-4
            elif (my_spade[i][0]=='Q'):
              check_index=-3
            elif (my_spade[i][0]=='8'):
              check_index=-2
            elif (my_spade[i][0]=='7'):
              check_index=-1
            if (check_index<round_winner):
              throw_card=my_spade[i]
              my_spade.pop(i)
              count[0]=count[0]-1
              my_cards.remove(throw_card)
              break
            else:
              throw_card=last_card_noncolour3()
        elif count[0]==0:
          throw_card=last_card_noncolour3()
      
      if trumph[1]=='C':
        if count[1]!=0:
          for i in range(count[1]-1,-1,-1):
            if (my_club[i][0]=='J'):
              check_index=-8
            elif (my_club[i][0]=='9'):
              check_index=-7
            elif (my_club[i][0]=='A'):
              check_index=-6
            elif (my_club[i][0]=='T'):
              check_index=-5
            elif (my_club[i][0]=='K'):
              check_index=-4
            elif (my_club[i][0]=='Q'):
              check_index=-3
            elif (my_club[i][0]=='8'):
              check_index=-2
            elif (my_club[i][0]=='7'):
              check_index=-1
            if (check_index<round_winner):
              throw_card=my_club[i]
              my_club.pop(i)
              count[1]=count[1]-1
              my_cards.remove(throw_card)
              break
            else:
              throw_card=last_card_noncolour3()
        elif count[1]==0:
          throw_card=last_card_noncolour3()

      if trumph[1]=='D':
        if count[2]!=0:
          for i in range(count[2]-1,-1,-1):
            if (my_diamond[i][0]=='J'):
              check_index=-8
            elif (my_diamond[i][0]=='9'):
              check_index=-7
            elif (my_diamond[i][0]=='A'):
              check_index=-6
            elif (my_diamond[i][0]=='T'):
              check_index=-5
            elif (my_diamond[i][0]=='K'):
              check_index=-4
            elif (my_diamond[i][0]=='Q'):
              check_index=-3
            elif (my_diamond[i][0]=='8'):
              check_index=-2
            elif (my_diamond[i][0]=='7'):
              check_index=-1
            if (check_index<round_winner):
              throw_card=my_diamond[i]
              my_diamond.pop(i)
              count[2]=count[2]-1
              my_cards.remove(throw_card)
              break
            else:
              throw_card=last_card_noncolour3()
        elif count[2]==0:
          throw_card=last_card_noncolour3()

      if trumph[1]=='H':
        if count[3]!=0:
          for i in range(count[3]-1,-1,-1):
            if (my_heart[i][0]=='J'):
              check_index=-8
            elif (my_heart[i][0]=='9'):
              check_index=-7
            elif (my_heart[i][0]=='A'):
              check_index=-6
            elif (my_heart[i][0]=='T'):
              check_index=-5
            elif (my_heart[i][0]=='K'):
              check_index=-4
            elif (my_heart[i][0]=='Q'):
              check_index=-3
            elif (my_heart[i][0]=='8'):
              check_index=-2
            elif (my_heart[i][0]=='7'):
              check_index=-1
            if (check_index<round_winner):
              throw_card=my_heart[i]
              my_heart.pop(i)
              count[3]=count[3]-1
              my_cards.remove(throw_card)
              break
            else:
              throw_card=last_card_noncolour3()
        elif count[3]==0:
          throw_card=last_card_noncolour3()
    return(throw_card)
      
  def third_card_noncolour2(round_winner,test):
    if (round_winner>=0):
      #Show trumph req
      trumph[0]=True
      trumph[1]='S'  #put here what trumph_suit is
      if trumph[1]=='S':
        if (opponent1[0]!=0):
          if count[0]!=0:
            throw_card=my_spade[0]
            my_spade.pop(0)
            count[0]=count[0]-1
            my_cards.remove(throw_card)
          elif count[0]==0:
            throw_card=last_card_noncolour3()
        else:
          if count[0]!=0:
            throw_card=my_spade[count[0]-1]
            my_spade.pop(count[0]-1)
            count[0]=count[0]-1
            my_cards.remove(throw_card)
          elif count[0]==0:
            throw_card=last_card_noncolour3()
      if trumph[1]=='C':
        if (opponent1[1]!=0):
          if count[1]!=0:
            throw_card=my_club[0]
            my_club.pop(0)
            count[1]=count[1]-1
            my_cards.remove(throw_card)
          elif count[1]==0:
            throw_card=last_card_noncolour3()
        else:
          if count[1]!=0:
            throw_card=my_club[count[1]-1]
            my_club.pop(count[1]-1)
            count[1]=count[1]-1
            my_cards.remove(throw_card)
          elif count[1]==0:
            throw_card=last_card_noncolour3()
      if trumph[1]=='D':
        if (opponent1[2]!=0):
          if count[2]!=0:
            throw_card=my_diamond[0]
            my_diamond.pop(0)
            count[2]=count[2]-1
            my_cards.remove(throw_card)
          elif count[2]==0:
            throw_card=last_card_noncolour3()
        else:
          if count[2]!=0:
            throw_card=my_diamond[count[2]-1]
            my_diamond.pop(count[2]-1)
            count[2]=count[2]-1
            my_cards.remove(throw_card)
          elif count[2]==0:
            throw_card=last_card_noncolour3()
      if trumph[1]=='H':
        if (opponent1[3]!=0):
          if count[3]!=0:
            throw_card=my_heart[0]
            my_heart.pop(0)
            count[3]=count[3]-1
            my_cards.remove(throw_card)
          elif count[3]==0:
            throw_card=last_card_noncolour3()
        else:
          if count[3]!=0:
            throw_card=my_heart[count[3]-1]
            my_heart.pop(count[3]-1)
            count[3]=count[3]-1
            my_cards.remove(throw_card)
          elif count[3]==0:
            throw_card=last_card_noncolour3()

    elif(round_winner<0):
      if trumph[1]=='S':
        if count[0]!=0:
          for i in range(count[0]-1,-1,-1):
            if (my_spade[i][0]=='J'):
              check_index=-8
            elif (my_spade[i][0]=='9'):
              check_index=-7
            elif (my_spade[i][0]=='A'):
              check_index=-6
            elif (my_spade[i][0]=='T'):
              check_index=-5
            elif (my_spade[i][0]=='K'):
              check_index=-4
            elif (my_spade[i][0]=='Q'):
              check_index=-3
            elif (my_spade[i][0]=='8'):
              check_index=-2
            elif (my_spade[i][0]=='7'):
              check_index=-1
            if (check_index<round_winner):
              if opponent1[0]==0:
                throw_card=my_spade[i]
                my_spade.pop(i)
                count[0]=count[0]-1
                my_cards.remove(throw_card)
                break
              else:
                if playing_cards["spade"].index(my_spade[0])==0:
                  throw_card=my_spade[0]
                  my_spade.pop(0)
                  count[0]=count[0]-1
                  my_cards.remove(throw_card)
                else:
                  throw_card=my_spade[i]
                  my_spade.pop(i)
                  count[0]=count[0]-1
                  my_cards.remove(throw_card)
            else:
              throw_card=last_card_noncolour3()
        elif count[0]==0:
          throw_card=last_card_noncolour3()
      
      if trumph[1]=='C':
        if count[1]!=0:
          for i in range(count[1]-1,-1,-1):
            if (my_club[i][0]=='J'):
              check_index=-8
            elif (my_club[i][0]=='9'):
              check_index=-7
            elif (my_club[i][0]=='A'):
              check_index=-6
            elif (my_club[i][0]=='T'):
              check_index=-5
            elif (my_club[i][0]=='K'):
              check_index=-4
            elif (my_club[i][0]=='Q'):
              check_index=-3
            elif (my_club[i][0]=='8'):
              check_index=-2
            elif (my_club[i][0]=='7'):
              check_index=-1
            if (check_index<round_winner):
              if opponent1[1]==0:
                throw_card=my_club[i]
                my_club.pop(i)
                count[1]=count[1]-1
                my_cards.remove(throw_card)
                break
              else:
                if playing_cards["club"].index(my_club[0])==0:
                  throw_card=my_club[0]
                  my_club.pop(0)
                  count[1]=count[1]-1
                  my_cards.remove(throw_card)
                else:
                  throw_card=my_club[i]
                  my_club.pop(i)
                  count[1]=count[1]-1
                  my_cards.remove(throw_card)
            else:
              throw_card=last_card_noncolour3()
        elif count[1]==0:
          throw_card=last_card_noncolour3()

      if trumph[1]=='D':
        if count[2]!=0:
          for i in range(count[2]-1,-1,-1):
            if (my_diamond[i][0]=='J'):
              check_index=-8
            elif (my_diamond[i][0]=='9'):
              check_index=-7
            elif (my_diamond[i][0]=='A'):
              check_index=-6
            elif (my_diamond[i][0]=='T'):
              check_index=-5
            elif (my_diamond[i][0]=='K'):
              check_index=-4
            elif (my_diamond[i][0]=='Q'):
              check_index=-3
            elif (my_diamond[i][0]=='8'):
              check_index=-2
            elif (my_diamond[i][0]=='7'):
              check_index=-1
            if (check_index<round_winner):
              if opponent1[2]==0:
                throw_card=my_diamond[i]
                my_diamond.pop(i)
                count[2]=count[2]-1
                my_cards.remove(throw_card)
                break
              else:
                if playing_cards["diamond"].index(my_diamond[0])==0:
                  throw_card=my_diamond[0]
                  my_diamond.pop(0)
                  count[2]=count[2]-1
                  my_cards.remove(throw_card)
                else:
                  throw_card=my_diamond[i]
                  my_diamond.pop(i)
                  count[2]=count[2]-1
                  my_cards.remove(throw_card)
            else:
              throw_card=last_card_noncolour3()
        elif count[2]==0:
          throw_card=last_card_noncolour3()

      if trumph[1]=='H':
        if count[3]!=0:
          for i in range(count[3]-1,-1,-1):
            if (my_heart[i][0]=='J'):
              check_index=-8
            elif (my_heart[i][0]=='9'):
              check_index=-7
            elif (my_heart[i][0]=='A'):
              check_index=-6
            elif (my_heart[i][0]=='T'):
              check_index=-5
            elif (my_heart[i][0]=='K'):
              check_index=-4
            elif (my_heart[i][0]=='Q'):
              check_index=-3
            elif (my_heart[i][0]=='8'):
              check_index=-2
            elif (my_heart[i][0]=='7'):
              check_index=-1
            if (check_index<round_winner):
              if opponent1[3]==0:
                throw_card=my_heart[i]
                my_heart.pop(i)
                count[3]=count[3]-1
                my_cards.remove(throw_card)
                break
              else:
                if playing_cards["heart"].index(my_heart[0])==0:
                  throw_card=my_heart[0]
                  my_heart.pop(0)
                  count[3]=count[3]-1
                  my_cards.remove(throw_card)
                else:
                  throw_card=my_heart[i]
                  my_heart.pop(i)
                  count[3]=count[3]-1
                  my_cards.remove(throw_card)
            else:
              throw_card=last_card_noncolour3()
        elif count[3]==0:
          throw_card=last_card_noncolour3()
    return(throw_card)

  def last_turn():
    #played_cards=cards played by other players,trumph_state=on or off,trumph[1]=which color,playing_cards=all the cards,count=no of colors i have,total_count =no of total colors in game
    if (len(my_cards)==1):
      return {"card": my_cards[0]}
    else:
      if trumph[0]==False:#or all trumph cards are finished
        if played_cards[0][-1]=='S':
          index[0]=playing_cards["spade"].index(played_cards[0])
          if played_cards[1][-1]=='S':
            index[1]=playing_cards["spade"].index(played_cards[1])                #Looking who has highest cards
          else:
            my_team[0]=0
            index[1]=97
          if played_cards[2][-1]=='S':
            index[2]=playing_cards["spade"].index(played_cards[2])  
          else:
            opponent2[0]=0
            index[2]=98
          round_winner=min(index[0],index[1],index[2])
          if round_winner==index[1]:
            if count[0]!=0:                                                                #if I have spade throw highest spade if my team wins
              count[0]=count[0]-1
              throw_card=my_spade[0]
              my_spade.pop(0)
              my_cards.remove(throw_card)
              return {"card": throw_card}
            elif count[0]==0:
              return {"card": last_card_noncolour1()}
          else:
            if count[0]!=0:                                                                #if I have spade throw lowest spade if my team lose
              if playing_cards["spade"].index(my_spade[0])<round_winner:
                count[0]=count[0]-1
                throw_card=my_spade[0]
                my_spade.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              else:
                throw_card=my_spade[count[0]-1]
                my_spade.pop(count[0]-1)
                count[0]=count[0]-1
                my_cards.remove(throw_card)
                return {"card": throw_card}
            elif count[0]==0:
              return {"card": last_card_noncolour2(round_winner)}

        elif played_cards[0][-1]=='C':
          index[0]=playing_cards["club"].index(played_cards[0])
          if played_cards[1][-1]=='C':
            index[1]=playing_cards["club"].index(played_cards[1])                #Looking who has highest cards
          else:
            my_team[1]=0
            index[1]=97
          if played_cards[2][-1]=='C':
            index[2]=playing_cards["club"].index(played_cards[2])  
          else:
            opponent2[1]=0
            index[2]=98
          round_winner=min(index[0],index[1],index[2])
          if round_winner==index[1]:
            if count[1]!=0:                                                                #if I have club throw highest club if my team wins
              count[1]=count[1]-1
              throw_card=my_club[0]
              my_club.pop(0)
              my_cards.remove(throw_card)
              return {"card": throw_card}
            elif count[1]==0:
              return {"card": last_card_noncolour1()}
          else:
            if count[1]!=0:                                                                #if I have club throw lowest club if my team lose
              if playing_cards["club"].index(my_club[0])<round_winner:
                count[1]=count[1]-1
                throw_card=my_club[0]
                my_club.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              else:
                throw_card=my_club[count[1]-1]
                my_club.pop(count[1]-1)
                count[1]=count[1]-1
                my_cards.remove(throw_card)
                return {"card": throw_card}
            elif count[1]==0:
              return {"card": last_card_noncolour2(round_winner)}

        elif played_cards[0][-1]=='D':
          index[0]=playing_cards["diamond"].index(played_cards[0])
          if played_cards[1][-1]=='D':
            index[1]=playing_cards["diamond"].index(played_cards[1])                #Looking who has highest cards
          else:
            my_team[2]=0
            index[1]=97
          if played_cards[2][-1]=='D':
            index[2]=playing_cards["diamond"].index(played_cards[2])  
          else:
            opponent2[2]=0
            index[2]=98
          round_winner=min(index[0],index[1],index[2])
          if round_winner==index[1]:
            if count[2]!=0:                                                                #if I have diamond throw highest diamond if my team wins
              count[2]=count[2]-1
              throw_card=my_diamond[0]
              my_diamond.pop(0)
              my_cards.remove(throw_card)
              return {"card": throw_card}
            elif count[2]==0:
              return {"card": last_card_noncolour1()}
          else:
            if count[2]!=0:                                                                #if I have diamond throw lowest diamond if my team lose
              if playing_cards["diamond"].index(my_diamond[0])<round_winner:
                count[2]=count[2]-1
                throw_card=my_diamond[0]
                my_diamond.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              else:
                throw_card=my_diamond[count[2]-1]
                my_diamond.pop(count[2]-1)
                count[2]=count[2]-1
                my_cards.remove(throw_card)
                return {"card": throw_card}
            elif count[2]==0:
              return {"card": last_card_noncolour2(round_winner)}
        
        elif played_cards[0][-1]=='H':
          index[0]=playing_cards["heart"].index(played_cards[0])
          if played_cards[1][-1]=='H':
            index[1]=playing_cards["heart"].index(played_cards[1])                #Looking who has highest cards
          else:
            my_team[3]=0
            index[1]=97
          if played_cards[2][-1]=='H':
            index[2]=playing_cards["heart"].index(played_cards[2])  
          else:
            opponent2[3]=0
            index[2]=98
          round_winner=min(index[0],index[1],index[2])
          if round_winner==index[1]:
            if count[3]!=0:                                                                #if I have heart throw highest heart if my team wins
              count[3]=count[3]-1
              throw_card=my_heart[0]
              my_heart.pop(0)
              my_cards.remove(throw_card)
              return {"card": throw_card}
            elif count[3]==0:
              return {"card": last_card_noncolour1()}
          else:
            if count[3]!=0:                                                                #if I have heart throw lowest heart if my team lose
              if playing_cards["heart"].index(my_heart[0])<round_winner:
                count[3]=count[3]-1
                throw_card=my_heart[0]
                my_heart.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              else:
                throw_card=my_heart[count[3]-1]
                my_heart.pop(count[3]-1)
                count[3]=count[3]-1
                my_cards.remove(throw_card)
                return {"card": throw_card}
            elif count[3]==0:
              return {"card": last_card_noncolour2(round_winner)}
      elif trumph[0]==True:
        if played_cards[0][-1]=='S':
          index[0]=playing_cards["spade"].index(played_cards[0])
          if played_cards[1][-1]=='S':
            index[1]=playing_cards["spade"].index(played_cards[1])                #Looking who has highest cards
          elif played_cards[1][-1]==trumph[1]:
            my_team[0]=0
            if played_cards[1][0]=='J':
              index[1]=-8
            if played_cards[1][0]=='9':
              index[1]=-7
            if played_cards[1][0]=='1':
              index[1]=-6
            if played_cards[1][0]=='T':
              index[1]=-5
            if played_cards[1][0]=='K':
              index[1]=-4
            if played_cards[1][0]=='Q':
              index[1]=-3
            if played_cards[1][0]=='8':
              index[1]=-2
            if played_cards[1][0]=='7':
              index[1]=-1
          else:
            my_team[0]=0
            index[1]=97
          if played_cards[2][-1]=='S':
            index[2]=playing_cards["spade"].index(played_cards[2])                #Looking who has highest cards
          elif played_cards[2][-1]==trumph[1]:
            opponent2[0]=0
            if played_cards[2][0]=='J':
              index[2]=-8
            if played_cards[2][0]=='9':
              index[2]=-7
            if played_cards[2][0]=='1':
              index[2]=-6
            if played_cards[2][0]=='T':
              index[2]=-5
            if played_cards[2][0]=='K':
              index[2]=-4
            if played_cards[2][0]=='Q':
              index[2]=-3
            if played_cards[2][0]=='8':
              index[2]=-2
            if played_cards[2][0]=='7':
              index[2]=-1
          else:
            opponent2[0]=0
            index[2]=98
          round_winner=min(index[0],index[1],index[2])
          if round_winner==index[1]:
            if count[0]!=0:                                                                #if I have spade throw highest spade if my team wins
              count[0]=count[0]-1
              throw_card=my_spade[0]
              my_spade.pop(0)
              my_cards.remove(throw_card)
              return {"card": throw_card}
            elif count[0]==0:
              return {"card": last_card_noncolour1()}
          else:
            if count[0]!=0:                                                                #if I have spade throw lowest spade if my team lose
              if playing_cards["spade"].index(my_spade[0])<round_winner:
                count[0]=count[0]-1
                throw_card=my_spade[0]
                my_spade.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              else:
                throw_card=my_spade[count[0]-1]
                my_spade.pop(count[0]-1)
                count[0]=count[0]-1
                my_cards.remove(throw_card)
                return {"card": throw_card}
            elif count[0]==0:
              return {"card": last_card_noncolour2(round_winner)}



        if played_cards[0][-1]=='C':
          index[0]=playing_cards["club"].index(played_cards[0])
          if played_cards[1][-1]=='C':
            index[1]=playing_cards["club"].index(played_cards[1])                #Looking who has highest cards
          elif played_cards[1][-1]==trumph[1]:
            my_team[1]=0
            if played_cards[1][0]=='J':
              index[1]=-8
            if played_cards[1][0]=='9':
              index[1]=-7
            if played_cards[1][0]=='1':
              index[1]=-6
            if played_cards[1][0]=='T':
              index[1]=-5
            if played_cards[1][0]=='K':
              index[1]=-4
            if played_cards[1][0]=='Q':
              index[1]=-3
            if played_cards[1][0]=='8':
              index[1]=-2
            if played_cards[1][0]=='7':
              index[1]=-1
          else:
            my_team[1]=0
            index[1]=97
          if played_cards[2][-1]=='C':
            index[2]=playing_cards["club"].index(played_cards[2])                #Looking who has highest cards
          elif played_cards[2][-1]==trumph[1]:
            opponent2[1]=0
            if played_cards[2][0]=='J':
              index[2]=-8
            if played_cards[2][0]=='9':
              index[2]=-7
            if played_cards[2][0]=='1':
              index[2]=-6
            if played_cards[2][0]=='T':
              index[2]=-5
            if played_cards[2][0]=='K':
              index[2]=-4
            if played_cards[2][0]=='Q':
              index[2]=-3
            if played_cards[2][0]=='8':
              index[2]=-2
            if played_cards[2][0]=='7':
              index[2]=-1
          else:
            opponent2[1]=0
            index[2]=98
          round_winner=min(index[0],index[1],index[2])
          if round_winner==index[1]:
            if count[1]!=0:                                                                #if I have club throw highest club if my team wins
              count[1]=count[1]-1
              throw_card=my_club[0]
              my_club.pop(0)
              my_cards.remove(throw_card)
              return {"card": throw_card}
            elif count[1]==0:
              return {"card": last_card_noncolour1()}
          else:
            if count[1]!=0:                                                                #if I have club throw lowest club if my team lose
              if playing_cards["club"].index(my_club[0])<round_winner:
                count[1]=count[1]-1
                throw_card=my_club[0]
                my_club.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              else:
                throw_card=my_club[count[1]-1]
                my_club.pop(count[1]-1)
                count[1]=count[1]-1
                my_cards.remove(throw_card)
                return {"card": throw_card}
            elif count[1]==0:
              return {"card": last_card_noncolour2(round_winner)}



        if played_cards[0][-1]=='D':
          index[0]=playing_cards["diamond"].index(played_cards[0])
          if played_cards[1][-1]=='D':
            index[1]=playing_cards["diamond"].index(played_cards[1])                #Looking who has highest cards
          elif played_cards[1][-1]==trumph[1]:
            my_team[2]=0
            if played_cards[1][0]=='J':
              index[1]=-8
            if played_cards[1][0]=='9':
              index[1]=-7
            if played_cards[1][0]=='1':
              index[1]=-6
            if played_cards[1][0]=='T':
              index[1]=-5
            if played_cards[1][0]=='K':
              index[1]=-4
            if played_cards[1][0]=='Q':
              index[1]=-3
            if played_cards[1][0]=='8':
              index[1]=-2
            if played_cards[1][0]=='7':
              index[1]=-1
          else:
            my_team[2]=0
            index[1]=97
          if played_cards[2][-1]=='D':
            index[2]=playing_cards["diamond"].index(played_cards[2])                #Looking who has highest cards
          elif played_cards[2][-1]==trumph[1]:
            opponent2[2]=0
            if played_cards[2][0]=='J':
              index[2]=-8
            if played_cards[2][0]=='9':
              index[2]=-7
            if played_cards[2][0]=='1':
              index[2]=-6
            if played_cards[2][0]=='T':
              index[2]=-5
            if played_cards[2][0]=='K':
              index[2]=-4
            if played_cards[2][0]=='Q':
              index[2]=-3
            if played_cards[2][0]=='8':
              index[2]=-2
            if played_cards[2][0]=='7':
              index[2]=-1
          else:
            opponent2[2]=0
            index[2]=98
          round_winner=min(index[0],index[1],index[2])
          if round_winner==index[1]:
            if count[2]!=0:                                                                #if I have diamond throw highest diamond if my team wins
              count[2]=count[2]-1
              throw_card=my_diamond[0]
              my_diamond.pop(0)
              my_cards.remove(throw_card)
              return {"card": throw_card}
            elif count[2]==0:
              return {"card": last_card_noncolour1()}
          else:
            if count[2]!=0:                                                                #if I have diamond throw lowest diamond if my team lose
              if playing_cards["diamond"].index(my_diamond[0])<round_winner:
                count[2]=count[2]-1
                throw_card=my_diamond[0]
                my_diamond.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              else:
                throw_card=my_diamond[count[2]-1]
                my_diamond.pop(count[2]-1)
                count[2]=count[2]-1
                my_cards.remove(throw_card)
                return {"card": throw_card}
            elif count[2]==0:
              return {"card": last_card_noncolour2(round_winner)}


        if played_cards[0][-1]=='H':
          index[0]=playing_cards["heart"].index(played_cards[0])
          if played_cards[1][-1]=='H':
            index[1]=playing_cards["heart"].index(played_cards[1])                #Looking who has highest cards
          elif played_cards[1][-1]==trumph[1]:
            my_team[3]=0
            if played_cards[1][0]=='J':
              index[1]=-8
            if played_cards[1][0]=='9':
              index[1]=-7
            if played_cards[1][0]=='1':
              index[1]=-6
            if played_cards[1][0]=='T':
              index[1]=-5
            if played_cards[1][0]=='K':
              index[1]=-4
            if played_cards[1][0]=='Q':
              index[1]=-3
            if played_cards[1][0]=='8':
              index[1]=-2
            if played_cards[1][0]=='7':
              index[1]=-1
          else:
            my_team[3]=0
            index[1]=97
          if played_cards[2][-1]=='H':
            index[2]=playing_cards["heart"].index(played_cards[2])                #Looking who has highest cards
          elif played_cards[2][-1]==trumph[1]:
            opponent2[3]=0
            if played_cards[2][0]=='J':
              index[2]=-8
            if played_cards[2][0]=='9':
              index[2]=-7
            if played_cards[2][0]=='1':
              index[2]=-6
            if played_cards[2][0]=='T':
              index[2]=-5
            if played_cards[2][0]=='K':
              index[2]=-4
            if played_cards[2][0]=='Q':
              index[2]=-3
            if played_cards[2][0]=='8':
              index[2]=-2
            if played_cards[2][0]=='7':
              index[2]=-1
          else:
            opponent2[3]=0
            index[2]=98
          round_winner=min(index[0],index[1],index[2])
          if round_winner==index[1]:
            if count[3]!=0:                                                                #if I have heart throw highest heart if my team wins
              count[3]=count[3]-1
              throw_card=my_heart[0]
              my_heart.pop(0)
              my_cards.remove(throw_card)
              return {"card": throw_card}
            elif count[3]==0:
              return {"card": last_card_noncolour1()}
          else:
            if count[3]!=0:                                                                #if I have heart throw lowest heart if my team lose
              if playing_cards["heart"].index(my_heart[0])<round_winner:
                count[3]=count[3]-1
                throw_card=my_heart[0]
                my_heart.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              else:
                throw_card=my_heart[count[3]-1]
                my_heart.pop(count[3]-1)
                count[3]=count[3]-1
                my_cards.remove(throw_card)
                return {"card": throw_card}
            elif count[3]==0:
              return {"card": last_card_noncolour2(round_winner)}
  
  def third_turn():
    if (len(my_cards)==1):
      return {"card": my_cards[0]}
    else:
      if trumph[0]==False:#or all trumph cards are finished
        if played_cards[0][-1]=='S':
          index_third[0]=playing_cards["spade"].index(played_cards[0])
          if played_cards[1][-1]=='S':
            index_third[1]=playing_cards["spade"].index(played_cards[1])                #Looking who has highest cards
          else:
            opponent2[0]=0
            index_third[1]=97
          round_winner=min(index_third[0],index_third[1])
          if round_winner==index_third[0]:
            if count[0]!=0:                                                                #if I have spade throw highest spade if my team wins
              if (((round_winner==0) or playing_cards["spade"].index(my_spade[0])==0 or (no_trumph==True and ((opponent1[0]==0)or total_count[0]==0))) and ((throw_count1[0]==0) or (no_trumph==True and ((opponent1[0]==0)or total_count[0]==0)))):
                count[0]=count[0]-1
                throw_card=my_spade[0]
                my_spade.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              elif (((round_winner==0) or playing_cards["spade"].index(my_spade[0])==0 or (no_trumph==True and ((opponent1[0]==0)or total_count[0]==0))) and ((throw_count1[0]>0) and (no_trumph==True and ((opponent1[0]==0)or total_count[0]==0)))):
                count[0]=count[0]-1
                throw_card=my_spade[0]
                my_spade.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              elif (((round_winner==0) or playing_cards["spade"].index(my_spade[0])==0 or (no_trumph==True and opponent1[0]==0)) and ((throw_count1[0]>0) and ((no_trumph==True and ((opponent1[0]==0)or total_count[0]==0)) or ((total_count[0]-count[0]-1>=3) and (my_team[0]==0 or opponent2[0]==0))))):
                count[0]=count[0]-1
                throw_card=my_spade[0]
                my_spade.pop(0)(no_trumph==True and ((opponent1[0]==0)or total_count[0]==0))
                my_cards.remove(throw_card)
                return {"card": throw_card}
              else:
                throw_card=my_spade[count[0]-1]
                my_spade.pop(count[0]-1)
                count[0]=count[0]-1
                my_cards.remove(throw_card)
                return {"card": throw_card}

            elif count[0]==0:

              if (((round_winner==0) or (no_trumph==True and ((opponent1[0]==0)or total_count[0]==0))) and ((throw_count1[0]==0) or (no_trumph==True and ((opponent1[0]==0)or total_count[0]==0)))):
                return {"card": last_card_noncolour1()}
              elif (((round_winner==0) or (no_trumph==True and ((opponent1[0]==0)or total_count[0]==0))) and ((throw_count1[0]>0) and (no_trumph==True and ((opponent1[0]==0)or total_count[0]==0)))):
                return {"card": last_card_noncolour1()}
              elif (((round_winner==0) or (no_trumph==True and ((opponent1[0]==0)or total_count[0]==0))) and ((throw_count1[0]>0) and ((no_trumph==True and ((opponent1[0]==0)or total_count[0]==0)) or ((total_count[0]-count[0]-1>=3) and (my_team[0]==0 or opponent2[0]==0))))):
                return {"card": last_card_noncolour1()}
              else:

                return {"card": third_card_noncolour2(round_winner,0)}
          else:
            if count[0]!=0:                                                                #if I have spade throw lowest spade if my team lose
              if playing_cards["spade"].index(my_spade[0])<round_winner:
                if ((throw_count1[0]==0) or (no_trumph==True and ((opponent1[0]==0)or total_count[0]==0))):
                  count[0]=count[0]-1
                  throw_card=my_spade[0]
                  my_spade.pop(0)
                  my_cards.remove(throw_card)
                  return {"card": throw_card}
                elif ((throw_count1[0]>0) and (no_trumph==True and ((opponent1[0]==0)or total_count[0]==0))):
                  count[0]=count[0]-1
                  throw_card=my_spade[0]
                  my_spade.pop(0)
                  my_cards.remove(throw_card)
                  return {"card": throw_card}
                elif ((throw_count1[0]>0) and ((no_trumph==True and ((opponent1[0]==0)or total_count[0]==0)) or ((total_count[0]-count[0]-1>=3) and (my_team[0]==0 or opponent2[0]==0)))):
                  count[0]=count[0]-1
                  throw_card=my_spade[0]
                  my_spade.pop(0)
                  my_cards.remove(throw_card)
                  return {"card": throw_card}
                else:
                  throw_card=my_spade[count[0]-1]
                  my_spade.pop(count[0]-1)
                  count[0]=count[0]-1
                  my_cards.remove(throw_card)
                  return {"card": throw_card}
              else:
                throw_card=my_spade[count[0]-1]
                my_spade.pop(count[0]-1)
                count[0]=count[0]-1
                my_cards.remove(throw_card)
                return {"card": throw_card}
            elif count[0]==0:
              return {"card": third_card_noncolour2(round_winner,0)}

        if played_cards[0][-1]=='C':
          index_third[0]=playing_cards["club"].index(played_cards[0])
          if played_cards[1][-1]=='C':
            index_third[1]=playing_cards["club"].index(played_cards[1])                #Looking who has highest cards
          else:
            opponent2[1]=0
            index_third[1]=97
          round_winner=min(index_third[0],index_third[1])
          if round_winner==index_third[0]:
            if count[1]!=0:                                                                #if I have club throw highest club if my team wins
              if (((round_winner==0) or playing_cards["club"].index(my_club[0])==0 or (no_trumph==True and ((opponent1[1]==0)or total_count[1]==0))) and ((throw_count1[1]==0) or (no_trumph==True and ((opponent1[1]==0)or total_count[1]==0)))):
                count[1]=count[1]-1
                throw_card=my_club[0]
                my_club.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              elif (((round_winner==0) or playing_cards["club"].index(my_club[0])==0 or (no_trumph==True and ((opponent1[1]==0)or total_count[1]==0))) and ((throw_count1[1]>0) and (no_trumph==True and ((opponent1[1]==0)or total_count[1]==0)))):
                count[1]=count[1]-1
                throw_card=my_club[0]
                my_club.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              elif (((round_winner==0) or playing_cards["club"].index(my_club[0])==0 or (no_trumph==True and ((opponent1[1]==0)or total_count[1]==0))) and ((throw_count1[1]>0) and ((no_trumph==True and ((opponent1[1]==0)or total_count[1]==0)) or ((total_count[1]-count[1]-1>=3) and (my_team[1]==0 or opponent2[1]==0))))):
                count[1]=count[1]-1
                throw_card=my_club[0]
                my_club.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              else:
                throw_card=my_club[count[1]-1]
                my_club.pop(count[1]-1)
                count[1]=count[1]-1
                my_cards.remove(throw_card)
                return {"card": throw_card}

            elif count[1]==0:

              if (((round_winner==0) or (no_trumph==True and ((opponent1[1]==0)or total_count[1]==0))) and ((throw_count1[1]==0) or (no_trumph==True and ((opponent1[1]==0)or total_count[1]==0)))):
                return {"card": last_card_noncolour1()}
              elif (((round_winner==0) or (no_trumph==True and ((opponent1[1]==0)or total_count[1]==0))) and ((throw_count1[1]>0) and (no_trumph==True and ((opponent1[1]==0)or total_count[1]==0)))):
                return {"card": last_card_noncolour1()}
              elif (((round_winner==0) or (no_trumph==True and ((opponent1[1]==0)or total_count[1]==0))) and ((throw_count1[1]>0) and ((no_trumph==True and ((opponent1[1]==0)or total_count[1]==0)) or ((total_count[1]-count[1]-1>=3) and (my_team[1]==0 or opponent2[1]==0))))):
                return {"card": last_card_noncolour1()}
              else:
                return {"card": third_card_noncolour2(round_winner,0)}
          else:
            if count[1]!=0:                                                                #if I have club throw lowest club if my team lose
              if playing_cards["club"].index(my_club[0])<round_winner:
                if ((throw_count1[1]==0) or (no_trumph==True and ((opponent1[1]==0)or total_count[1]==0))):
                  count[1]=count[1]-1
                  throw_card=my_club[0]
                  my_club.pop(0)
                  my_cards.remove(throw_card)
                  return {"card": throw_card}
                elif ((throw_count1[1]>0) and (no_trumph==True and ((opponent1[1]==0)or total_count[1]==0))):
                  count[1]=count[1]-1
                  throw_card=my_club[0]
                  my_club.pop(0)
                  my_cards.remove(throw_card)
                  return {"card": throw_card}
                elif ((throw_count1[1]>0) and ((no_trumph==True and ((opponent1[1]==0)or total_count[1]==0)) or ((total_count[1]-count[1]-1>=3) and (my_team[1]==0 or opponent2[1]==0)))):
                  count[1]=count[1]-1
                  throw_card=my_club[0]
                  my_club.pop(0)
                  my_cards.remove(throw_card)
                  return {"card": throw_card}
                else:
                  throw_card=my_club[count[1]-1]
                  my_club.pop(count[1]-1)
                  count[1]=count[1]-1
                  my_cards.remove(throw_card)
                  return {"card": throw_card}
              else:
                throw_card=my_club[count[1]-1]
                my_club.pop(count[1]-1)
                count[1]=count[1]-1
                my_cards.remove(throw_card)
                return {"card": throw_card}
            elif count[1]==0:
              return {"card": third_card_noncolour2(round_winner,0)}

        if played_cards[0][-1]=='D':
          index_third[0]=playing_cards["diamond"].index(played_cards[0])
          if played_cards[1][-1]=='D':
            index_third[1]=playing_cards["diamond"].index(played_cards[1])                #Looking who has highest cards
          else:
            opponent2[2]=0
            index_third[1]=97
          round_winner=min(index_third[0],index_third[1])
          if round_winner==index_third[0]:
            if count[2]!=0:                                                                #if I have diamond throw highest diamond if my team wins
              if (((round_winner==0) or playing_cards["diamond"].index(my_diamond[0])==0 or (no_trumph==True and ((opponent1[2]==0)or total_count[2]==0))) and ((throw_count1[2]==0) or (no_trumph==True and ((opponent1[2]==0)or total_count[2]==0)))):
                count[2]=count[2]-1
                throw_card=my_diamond[0]
                my_diamond.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              elif (((round_winner==0) or playing_cards["diamond"].index(my_diamond[0])==0 or (no_trumph==True and ((opponent1[2]==0)or total_count[2]==0))) and ((throw_count1[2]>0) and (no_trumph==True and ((opponent1[2]==0)or total_count[2]==0)))):
                count[2]=count[2]-1
                throw_card=my_diamond[0]
                my_diamond.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              elif (((round_winner==0) or playing_cards["diamond"].index(my_diamond[0])==0 or (no_trumph==True and ((opponent1[2]==0)or total_count[2]==0))) and ((throw_count1[2]>0) and ((no_trumph==True and ((opponent1[2]==0)or total_count[2]==0)) or ((total_count[2]-count[2]-1>=3) and (my_team[2]==0 or opponent2[2]==0))))):
                count[2]=count[2]-1
                throw_card=my_diamond[0]
                my_diamond.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              else:
                throw_card=my_diamond[count[2]-1]
                my_diamond.pop(count[2]-1)
                count[2]=count[2]-1
                my_cards.remove(throw_card)
                return {"card": throw_card}

            elif count[2]==0:

              if (((round_winner==0) or (no_trumph==True and ((opponent1[2]==0)or total_count[2]==0))) and ((throw_count1[2]==0) or (no_trumph==True and ((opponent1[2]==0)or total_count[2]==0)))):
                return {"card": last_card_noncolour1()}
              elif (((round_winner==0) or (no_trumph==True and ((opponent1[2]==0)or total_count[2]==0))) and ((throw_count1[2]>0) and (no_trumph==True and ((opponent1[2]==0)or total_count[2]==0)))):
                return {"card": last_card_noncolour1()}
              elif (((round_winner==0) or (no_trumph==True and ((opponent1[2]==0)or total_count[2]==0))) and ((throw_count1[2]>0) and ((no_trumph==True and ((opponent1[2]==0)or total_count[2]==0)) or ((total_count[2]-count[2]-1>=3) and (my_team[2]==0 or opponent2[2]==0))))):
                return {"card": last_card_noncolour1()}
              else:
                return {"card": third_card_noncolour2(round_winner,0)}
          else:
            if count[2]!=0:                                                                #if I have diamond throw lowest diamond if my team lose
              if playing_cards["diamond"].index(my_diamond[0])<round_winner:
                if ((throw_count1[2]==0) or ((opponent1[2]==0 or total_count[2]==0) and trumph[2]==False)):
                  count[2]=count[2]-1
                  throw_card=my_diamond[0]
                  my_diamond.pop(0)
                  my_cards.remove(throw_card)
                  return {"card": throw_card}
                elif ((throw_count1[2]>0) and (no_trumph==True and ((opponent1[2]==0)or total_count[2]==0))):
                  count[2]=count[2]-1
                  throw_card=my_diamond[0]
                  my_diamond.pop(0)
                  my_cards.remove(throw_card)
                  return {"card": throw_card}
                elif ((throw_count1[2]>0) and ((no_trumph==True and ((opponent1[2]==0)or total_count[2]==0)) or ((total_count[2]-count[2]-1>=3) and (my_team[2]==0 or opponent2[2]==0)))):
                  count[2]=count[2]-1
                  throw_card=my_diamond[0]
                  my_diamond.pop(0)
                  my_cards.remove(throw_card)
                  return {"card": throw_card}
                else:
                  throw_card=my_diamond[count[2]-1]
                  my_diamond.pop(count[2]-1)
                  count[2]=count[2]-1
                  my_cards.remove(throw_card)
                  return {"card": throw_card}
              else:
                throw_card=my_diamond[count[2]-1]
                my_diamond.pop(count[2]-1)
                count[2]=count[2]-1
                my_cards.remove(throw_card)
                return {"card": throw_card}
            elif count[2]==0:
              return {"card": third_card_noncolour2(round_winner,0)}

        if played_cards[0][-1]=='H':
          index_third[0]=playing_cards["heart"].index(played_cards[0])
          if played_cards[1][-1]=='H':
            index_third[1]=playing_cards["heart"].index(played_cards[1])                #Looking who has highest cards
          else:
            opponent2[3]=0
            index_third[1]=97
          round_winner=min(index_third[0],index_third[1])
          if round_winner==index_third[0]:
            if count[3]!=0:                                                                #if I have heart throw highest heart if my team wins
              if (((round_winner==0) or playing_cards["heart"].index(my_heart[0])==0 or (no_trumph==True and ((opponent1[3]==0)or total_count[3]==0))) and ((throw_count1[3]==0) or (no_trumph==True and ((opponent1[3]==0)or total_count[3]==0)))):
                count[3]=count[3]-1
                throw_card=my_heart[0]
                my_heart.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              elif (((round_winner==0) or playing_cards["heart"].index(my_heart[0])==0 or (no_trumph==True and ((opponent1[3]==0)or total_count[3]==0))) and ((throw_count1[3]>0) and (no_trumph==True and ((opponent1[3]==0)or total_count[3]==0)))):
                count[3]=count[3]-1
                throw_card=my_heart[0]
                my_heart.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              elif (((round_winner==0) or playing_cards["heart"].index(my_heart[0])==0 or (no_trumph==True and ((opponent1[3]==0)or total_count[3]==0))) and ((throw_count1[3]>0) and ((no_trumph==True and ((opponent1[3]==0)or total_count[3]==0)) or ((total_count[3]-count[3]-1>=3) and (my_team[3]==0 or opponent2[3]==0))))):
                count[3]=count[3]-1
                throw_card=my_heart[0]
                my_heart.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              else:
                throw_card=my_heart[count[3]-1]
                my_heart.pop(count[3]-1)
                count[3]=count[3]-1
                my_cards.remove(throw_card)
                return {"card": throw_card}

            elif count[3]==0:

              if (((round_winner==0) or (no_trumph==True and ((opponent1[3]==0)or total_count[3]==0))) and ((throw_count1[3]==0) or (no_trumph==True and ((opponent1[3]==0)or total_count[3]==0)))):
                return {"card": last_card_noncolour1()}
              elif (((round_winner==0) or (no_trumph==True and ((opponent1[3]==0)or total_count[3]==0))) and ((throw_count1[3]>0) and (no_trumph==True and ((opponent1[3]==0)or total_count[3]==0)))):
                return {"card": last_card_noncolour1()}
              elif (((round_winner==0) or (no_trumph==True and ((opponent1[3]==0)or total_count[3]==0))) and ((throw_count1[3]>0) and ((no_trumph==True and ((opponent1[3]==0)or total_count[3]==0)) or ((total_count[3]-count[3]-1>=3) and (my_team[3]==0 or opponent2[3]==0))))):
                return {"card": last_card_noncolour1()}
              else:
                return {"card": third_card_noncolour2(round_winner,0)}
          else:
            if count[3]!=0:                                                                #if I have heart throw lowest heart if my team lose
              if playing_cards["heart"].index(my_heart[0])<round_winner:
                if ((throw_count1[3]==0) or ((opponent1[3]==0 or total_count[3]==0) and trumph[3]==False)):
                  count[3]=count[3]-1
                  throw_card=my_heart[0]
                  my_heart.pop(0)
                  my_cards.remove(throw_card)
                  return {"card": throw_card}
                elif ((throw_count1[3]>0) and (no_trumph==True and ((opponent1[3]==0)or total_count[3]==0))):
                  count[3]=count[3]-1
                  throw_card=my_heart[0]
                  my_heart.pop(0)
                  my_cards.remove(throw_card)
                  return {"card": throw_card}
                elif ((throw_count1[3]>0) and ((no_trumph==True and ((opponent1[3]==0)or total_count[3]==0)) or ((total_count[3]-count[3]-1>=3) and (my_team[3]==0 or opponent2[3]==0)))):
                  count[3]=count[3]-1
                  throw_card=my_heart[0]
                  my_heart.pop(0)
                  my_cards.remove(throw_card)
                  return {"card": throw_card}
                else:
                  throw_card=my_heart[count[3]-1]
                  my_heart.pop(count[3]-1)
                  count[3]=count[3]-1
                  my_cards.remove(throw_card)
                  return {"card": throw_card}
              else:
                throw_card=my_heart[count[3]-1]
                my_heart.pop(count[3]-1)
                count[3]=count[3]-1
                my_cards.remove(throw_card)
                return {"card": throw_card}
            elif count[3]==0:
              return {"card": third_card_noncolour2(round_winner,0)}

      elif trumph[0]==True:
        if played_cards[0][-1]=='S' and trumph[1]=='S':
          index_third[0]=playing_cards["spade"].index(played_cards[0])
          if played_cards[1][-1]=='S':
            index_third[1]=playing_cards["spade"].index(played_cards[1])
          else:
            opponent2[0]=0
            index_third[1]=98
          round_winner=min(index_third[0],index_third[1])
          if round_winner==index_third[0]:
            if count[0]!=0:
              if (round_winner==0):
                if count[0]==1:
                  count[0]=count[0]-1
                  throw_card=my_spade[0]
                  my_spade.pop(0)
                  my_cards.remove(throw_card)
                  return {"card": throw_card}
                elif count[0]==2:
                  if playing_cards["spade"].index(my_spade[0])==1:
                    count[0]=count[0]-1
                    throw_card=my_spade[1]
                    my_spade.pop(1)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                  else:
                    count[0]=count[0]-1
                    throw_card=my_spade[0]
                    my_spade.pop(0)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                elif count[0]==3:
                  if playing_cards["spade"].index(my_spade[0])==1:
                    if playing_cards["spade"].index(my_spade[1])==2:
                      count[0]=count[0]-1
                      throw_card=my_spade[2]
                      my_spade.pop(2)
                      my_cards.remove(throw_card)
                      return {"card": throw_card}
                    else:
                      count[0]=count[0]-1
                      throw_card=my_spade[1]
                      my_spade.pop(1)
                      my_cards.remove(throw_card)
                      return {"card": throw_card}
                  else:
                    count[0]=count[0]-1
                    throw_card=my_spade[0]
                    my_spade.pop(0)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                else:
                  if playing_cards["spade"].index(my_spade[0])==1:
                    count[0]=count[0]-1
                    throw_card=my_spade[1]
                    my_spade.pop(1)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                  else:
                    count[0]=count[0]-1
                    throw_card=my_spade[0]
                    my_spade.pop(0)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
              else:
                if playing_cards["spade"].index(my_spade[0])==0:
                  count[0]=count[0]-1
                  throw_card=my_spade[0]
                  my_spade.pop(0)
                  my_cards.remove(throw_card)
                  return {"card": throw_card}
                else:
                  throw_card=my_spade[count[0]-1]
                  my_spade.pop(count[0]-1)
                  count[0]=count[0]-1
                  my_cards.remove(throw_card)
                  return {"card": throw_card}  
            elif count[0]==0:   
              if (round_winner==0):
                return {"card": last_card_noncolour1()}  
              else:
                return {"card": last_card_noncolour3()}

          elif round_winner==index_third[1]:
            if count[0]!=0:
              if playing_cards["spade"].index(my_spade[0])==0:
                count[0]=count[0]-1
                throw_card=my_spade[0]
                my_spade.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              else:
                throw_card=my_spade[count[0]-1]
                my_spade.pop(count[0]-1)
                count[0]=count[0]-1
                my_cards.remove(throw_card)
                return {"card": throw_card}
            else:
              return {"card": last_card_noncolour3()}

        elif played_cards[0][-1]=='S' and trumph[1]!='S':
          index_third[0]=playing_cards["spade"].index(played_cards[0])
          if played_cards[1][-1]=='S':
            index_third[1]=playing_cards["spade"].index(played_cards[1])                #Looking who has highest cards
          elif played_cards[1][-1]==trumph[1]:
            opponent2[0]=0
            if played_cards[1][0]=='J':
              index_third[1]=-8
            if played_cards[1][0]=='9':
              index_third[1]=-7
            if played_cards[1][0]=='1':
              index_third[1]=-6
            if played_cards[1][0]=='T':
              index_third[1]=-5
            if played_cards[1][0]=='K':
              index_third[1]=-4
            if played_cards[1][0]=='Q':
              index_third[1]=-3
            if played_cards[1][0]=='8':
              index_third[1]=-2
            if played_cards[1][0]=='7':
              index_third[1]=-1
          else:
            opponent2[0]=0
            index_third[1]=97
          round_winner=min(index_third[0],index_third[1])
          if round_winner==index_third[0]:
            if count[0]!=0:                                                                #if I have spade throw highest spade if my team wins
              if (((round_winner==0) or playing_cards["spade"].index(my_spade[0])==0 or (no_trumph==True and ((opponent1[0]==0)or total_count[0]==0))) and ((throw_count1[0]==0) or (no_trumph==True and ((opponent1[0]==0)or total_count[0]==0)))):
                count[0]=count[0]-1
                throw_card=my_spade[0]
                my_spade.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              elif (((round_winner==0) or playing_cards["spade"].index(my_spade[0])==0 or (no_trumph==True and ((opponent1[0]==0)or total_count[0]==0))) and ((throw_count1[0]>0) and (no_trumph==True and ((opponent1[0]==0)or total_count[0]==0)))):
                count[0]=count[0]-1
                throw_card=my_spade[0]
                my_spade.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              elif (((round_winner==0) or playing_cards["spade"].index(my_spade[0])==0 or (no_trumph==True and ((opponent1[0]==0)or total_count[0]==0))) and ((throw_count1[0]>0) and ((no_trumph==True and ((opponent1[0]==0)or total_count[0]==0)) or ((total_count[0]-count[0]-1>=3) and (my_team[0]==0 or opponent2[0]==0))))):
                count[0]=count[0]-1
                throw_card=my_spade[0]
                my_spade.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              else:
                throw_card=my_spade[count[0]-1]
                my_spade.pop(count[0]-1)
                count[0]=count[0]-1
                my_cards.remove(throw_card)
                return {"card": throw_card}

            elif count[0]==0:

              if (((round_winner==0) or (no_trumph==True and ((opponent1[0]==0)or total_count[0]==0))) and ((throw_count1[0]==0) or (no_trumph==True and ((opponent1[0]==0)or total_count[0]==0)))):
                return {"card": last_card_noncolour1()}
              elif (((round_winner==0) or (no_trumph==True and ((opponent1[0]==0)or total_count[0]==0))) and ((throw_count1[0]>0) and (no_trumph==True and ((opponent1[0]==0)or total_count[0]==0)))):
                return {"card": last_card_noncolour1()}
              elif (((round_winner==0) or (no_trumph==True and ((opponent1[0]==0)or total_count[0]==0))) and ((throw_count1[0]>0) and ((no_trumph==True and ((opponent1[0]==0)or total_count[0]==0)) or ((total_count[0]-count[0]-1>=3) and (my_team[0]==0 or opponent2[0]==0))))):
                return {"card": last_card_noncolour1()}
              else:
                return {"card": third_card_noncolour2(round_winner,0)}
          elif round_winner==index_third[1]:
            if round_winner>=0:
              if count[0]!=0:                                                                #if I have spade throw lowest spade if my team lose
                if playing_cards["spade"].index(my_spade[0])<round_winner:
                  if ((throw_count1[0]==0) or (no_trumph==True and ((opponent1[0]==0)or total_count[0]==0))):
                    count[0]=count[0]-1
                    throw_card=my_spade[0]
                    my_spade.pop(0)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                  elif ((throw_count1[0]>0) and (no_trumph==True and ((opponent1[0]==0)or total_count[0]==0))):
                    count[0]=count[0]-1
                    throw_card=my_spade[0]
                    my_spade.pop(0)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                  elif ((throw_count1[0]>0) and ((no_trumph==True and ((opponent1[0]==0)or total_count[0]==0)) or ((total_count[0]-count[0]-1>=3) and (my_team[0]==0 or opponent2[0]==0)))):
                    count[0]=count[0]-1
                    throw_card=my_spade[0]
                    my_spade.pop(0)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                  else:
                    throw_card=my_spade[count[0]-1]
                    my_spade.pop(count[0]-1)
                    count[0]=count[0]-1
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                else:
                  throw_card=my_spade[count[0]-1]
                  my_spade.pop(count[0]-1)
                  count[0]=count[0]-1
                  my_cards.remove(throw_card)
                  return {"card": throw_card}
              elif count[0]==0:
                return {"card": third_card_noncolour2(round_winner,0)}
            elif round_winner<0:
              if count[0]!=0:
                throw_card=my_spade[count[0]-1]
                my_spade.pop(count[0]-1)
                count[0]=count[0]-1
                my_cards.remove(throw_card)
                return {"card": throw_card}
              elif count[0]==0:
                return {"card": third_card_noncolour2(round_winner,0)}

        elif played_cards[0][-1]=='C' and trumph[1]=='C':
          index_third[0]=playing_cards["club"].index(played_cards[0])
          if played_cards[1][-1]=='C':
            index_third[1]=playing_cards["club"].index(played_cards[1])
          else:
            opponent2[1]=0
            index_third[1]=98
          round_winner=min(index_third[0],index_third[1])
          if round_winner==index_third[0]:
            if count[1]!=0:
              if (round_winner==0):
                if count[1]==1:
                  count[1]=count[1]-1
                  throw_card=my_club[0]
                  my_club.pop(0)
                  my_cards.remove(throw_card)
                  return {"card": throw_card}
                elif count[1]==2:
                  if playing_cards["club"].index(my_club[0])==1:
                    count[1]=count[1]-1
                    throw_card=my_club[1]
                    my_club.pop(1)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                  else:
                    count[1]=count[1]-1
                    throw_card=my_club[0]
                    my_club.pop(0)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                elif count[1]==3:
                  if playing_cards["club"].index(my_club[0])==1:
                    if playing_cards["club"].index(my_club[1])==2:
                      count[1]=count[1]-1
                      throw_card=my_club[2]
                      my_club.pop(2)
                      my_cards.remove(throw_card)
                      return {"card": throw_card}
                    else:
                      count[1]=count[1]-1
                      throw_card=my_club[1]
                      my_club.pop(1)
                      my_cards.remove(throw_card)
                      return {"card": throw_card}
                  else:
                    count[1]=count[1]-1
                    throw_card=my_club[0]
                    my_club.pop(0)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                else:
                  if playing_cards["club"].index(my_club[0])==1:
                    count[1]=count[1]-1
                    throw_card=my_club[1]
                    my_club.pop(1)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                  else:
                    count[1]=count[1]-1
                    throw_card=my_club[0]
                    my_club.pop(0)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
              else:
                if playing_cards["club"].index(my_club[0])==0:
                  count[1]=count[1]-1
                  throw_card=my_club[0]
                  my_club.pop(0)
                  my_cards.remove(throw_card)
                  return {"card": throw_card}
                else:
                  throw_card=my_club[count[1]-1]
                  my_club.pop(count[1]-1)
                  count[1]=count[1]-1
                  my_cards.remove(throw_card)
                  return {"card": throw_card}  
            elif count[1]==0:   
              if (round_winner==0):
                return {"card": last_card_noncolour1()}  
              else:
                return {"card": last_card_noncolour3()}

          elif round_winner==index_third[1]:
            if count[1]!=0:
              if playing_cards["club"].index(my_club[0])==0:
                count[1]=count[1]-1
                throw_card=my_club[0]
                my_club.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              else:
                throw_card=my_club[count[1]-1]
                my_club.pop(count[1]-1)
                count[1]=count[1]-1
                my_cards.remove(throw_card)
                return {"card": throw_card}
            else:
              return {"card": last_card_noncolour3()}

        elif played_cards[0][-1]=='C' and trumph[1]!='C':
          index_third[0]=playing_cards["club"].index(played_cards[0])
          if played_cards[1][-1]=='C':
            index_third[1]=playing_cards["club"].index(played_cards[1])                #Looking who has highest cards
          elif played_cards[1][-1]==trumph[1]:
            opponent2[1]=0
            if played_cards[1][0]=='J':
              index_third[1]=-8
            if played_cards[1][0]=='9':
              index_third[1]=-7
            if played_cards[1][0]=='1':
              index_third[1]=-6
            if played_cards[1][0]=='T':
              index_third[1]=-5
            if played_cards[1][0]=='K':
              index_third[1]=-4
            if played_cards[1][0]=='Q':
              index_third[1]=-3
            if played_cards[1][0]=='8':
              index_third[1]=-2
            if played_cards[1][0]=='7':
              index_third[1]=-1
          else:
            opponent2[1]=0
            index_third[1]=97
          round_winner=min(index_third[0],index_third[1])
          if round_winner==index_third[0]:
            if count[1]!=0:                                                                #if I have club throw highest club if my team wins
              if (((round_winner==0) or playing_cards["club"].index(my_club[0])==0 or (no_trumph==True and ((opponent1[1]==0)or total_count[1]==0))) and ((throw_count1[1]==0) or (no_trumph==True and ((opponent1[1]==0)or total_count[1]==0)))):
                count[1]=count[1]-1
                throw_card=my_club[0]
                my_club.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              elif (((round_winner==0) or playing_cards["club"].index(my_club[0])==0 or (no_trumph==True and ((opponent1[1]==0)or total_count[1]==0))) and ((throw_count1[1]>0) and (no_trumph==True and ((opponent1[1]==0)or total_count[1]==0)))):
                count[1]=count[1]-1
                throw_card=my_club[0]
                my_club.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              elif (((round_winner==0) or playing_cards["club"].index(my_club[0])==0 or (no_trumph==True and ((opponent1[1]==0)or total_count[1]==0))) and ((throw_count1[1]>0) and ((no_trumph==True and ((opponent1[1]==0)or total_count[1]==0)) or ((total_count[1]-count[1]-1>=3) and (my_team[1]==0 or opponent2[1]==0))))):
                count[1]=count[1]-1
                throw_card=my_club[0]
                my_club.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              else:
                throw_card=my_club[count[1]-1]
                my_club.pop(count[1]-1)
                count[1]=count[1]-1
                my_cards.remove(throw_card)
                return {"card": throw_card}

            elif count[1]==0:

              if (((round_winner==0) or (no_trumph==True and ((opponent1[1]==0)or total_count[1]==0))) and ((throw_count1[1]==0) or (no_trumph==True and ((opponent1[1]==0)or total_count[1]==0)))):
                return {"card": last_card_noncolour1()}
              elif (((round_winner==0) or (no_trumph==True and ((opponent1[1]==0)or total_count[1]==0))) and ((throw_count1[1]>0) and (no_trumph==True and ((opponent1[1]==0)or total_count[1]==0)))):
                return {"card": last_card_noncolour1()}
              elif (((round_winner==0) or (no_trumph==True and ((opponent1[1]==0)or total_count[1]==0))) and ((throw_count1[1]>0) and ((no_trumph==True and ((opponent1[1]==0)or total_count[1]==0)) or ((total_count[1]-count[1]-1>=3) and (my_team[1]==0 or opponent2[1]==0))))):
                return {"card": last_card_noncolour1()}
              else:
                return {"card": third_card_noncolour2(round_winner,0)}
          elif round_winner==index_third[1]:
            if round_winner>=0:
              if count[1]!=0:                                                                #if I have club throw lowest club if my team lose
                if playing_cards["club"].index(my_club[0])<round_winner:
                  if ((throw_count1[1]==0) or (no_trumph==True and ((opponent1[1]==0)or total_count[1]==0))):
                    count[1]=count[1]-1
                    throw_card=my_club[0]
                    my_club.pop(0)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                  elif ((throw_count1[1]>0) and (no_trumph==True and ((opponent1[1]==0)or total_count[1]==0))):
                    count[1]=count[1]-1
                    throw_card=my_club[0]
                    my_club.pop(0)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                  elif ((throw_count1[1]>0) and ((no_trumph==True and ((opponent1[1]==0)or total_count[1]==0)) or ((total_count[1]-count[1]-1>=3) and (my_team[1]==0 or opponent2[1]==0)))):
                    count[1]=count[1]-1
                    throw_card=my_club[0]
                    my_club.pop(0)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                  else:
                    throw_card=my_club[count[1]-1]
                    my_club.pop(count[1]-1)
                    count[1]=count[1]-1
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                else:
                  throw_card=my_club[count[1]-1]
                  my_club.pop(count[1]-1)
                  count[1]=count[1]-1
                  my_cards.remove(throw_card)
                  return {"card": throw_card}
              elif count[1]==0:
                return {"card": third_card_noncolour2(round_winner,0)}
            elif round_winner<0:
              if count[1]!=0:
                throw_card=my_club[count[1]-1]
                my_club.pop(count[1]-1)
                count[1]=count[1]-1
                my_cards.remove(throw_card)
                return {"card": throw_card}
              elif count[1]==0:
                return {"card": third_card_noncolour2(round_winner,0)}

        elif played_cards[0][-1]=='D' and trumph[1]=='D':
          index_third[0]=playing_cards["diamond"].index(played_cards[0])
          if played_cards[1][-1]=='D':
            index_third[1]=playing_cards["diamond"].index(played_cards[1])
          else:
            opponent2[2]=0
            index_third[1]=98
          round_winner=min(index_third[0],index_third[1])
          if round_winner==index_third[0]:
            if count[2]!=0:
              if (round_winner==0):
                if count[2]==1:
                  count[2]=count[2]-1
                  throw_card=my_diamond[0]
                  my_diamond.pop(0)
                  my_cards.remove(throw_card)
                  return {"card": throw_card}
                elif count[2]==2:
                  if playing_cards["diamond"].index(my_diamond[0])==1:
                    count[2]=count[2]-1
                    throw_card=my_diamond[1]
                    my_diamond.pop(1)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                  else:
                    count[2]=count[2]-1
                    throw_card=my_diamond[0]
                    my_diamond.pop(0)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                elif count[2]==3:
                  if playing_cards["diamond"].index(my_diamond[0])==1:
                    if playing_cards["diamond"].index(my_diamond[1])==2:
                      count[2]=count[2]-1
                      throw_card=my_diamond[2]
                      my_diamond.pop(2)
                      my_cards.remove(throw_card)
                      return {"card": throw_card}
                    else:
                      count[2]=count[2]-1
                      throw_card=my_diamond[1]
                      my_diamond.pop(1)
                      my_cards.remove(throw_card)
                      return {"card": throw_card}
                  else:
                    count[2]=count[2]-1
                    throw_card=my_diamond[0]
                    my_diamond.pop(0)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                else:
                  if playing_cards["diamond"].index(my_diamond[0])==1:
                    count[2]=count[2]-1
                    throw_card=my_diamond[1]
                    my_diamond.pop(1)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                  else:
                    count[2]=count[2]-1
                    throw_card=my_diamond[0]
                    my_diamond.pop(0)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
              else:
                if playing_cards["diamond"].index(my_diamond[0])==0:
                  count[2]=count[2]-1
                  throw_card=my_diamond[0]
                  my_diamond.pop(0)
                  my_cards.remove(throw_card)
                  return {"card": throw_card}
                else:
                  throw_card=my_diamond[count[2]-1]
                  my_diamond.pop(count[2]-1)
                  count[2]=count[2]-1
                  my_cards.remove(throw_card)
                  return {"card": throw_card}  
            elif count[2]==0:   
              if (round_winner==0):
                return {"card": last_card_noncolour1()}  
              else:
                return {"card": last_card_noncolour3()}

          elif round_winner==index_third[1]:
            if count[2]!=0:
              if playing_cards["diamond"].index(my_diamond[0])==0:
                count[2]=count[2]-1
                throw_card=my_diamond[0]
                my_diamond.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              else:
                throw_card=my_diamond[count[2]-1]
                my_diamond.pop(count[2]-1)
                count[2]=count[2]-1
                my_cards.remove(throw_card)
                return {"card": throw_card}
            else:
              return {"card": last_card_noncolour3()}

        elif played_cards[0][-1]=='D' and trumph[1]!='D':
          index_third[0]=playing_cards["diamond"].index(played_cards[0])
          if played_cards[1][-1]=='D':
            index_third[1]=playing_cards["diamond"].index(played_cards[1])                #Looking who has highest cards
          elif played_cards[1][-1]==trumph[1]:
            opponent2[2]=0
            if played_cards[1][0]=='J':
              index_third[1]=-8
            if played_cards[1][0]=='9':
              index_third[1]=-7
            if played_cards[1][0]=='1':
              index_third[1]=-6
            if played_cards[1][0]=='T':
              index_third[1]=-5
            if played_cards[1][0]=='K':
              index_third[1]=-4
            if played_cards[1][0]=='Q':
              index_third[1]=-3
            if played_cards[1][0]=='8':
              index_third[1]=-2
            if played_cards[1][0]=='7':
              index_third[1]=-1
          else:
            opponent2[2]=0
            index_third[1]=97
          round_winner=min(index_third[0],index_third[1])
          if round_winner==index_third[0]:
            if count[2]!=0:                                                                #if I have diamond throw highest diamond if my team wins
              if (((round_winner==0) or playing_cards["diamond"].index(my_diamond[0])==0 or (no_trumph==True and ((opponent1[2]==0)or total_count[2]==0))) and ((throw_count1[2]==0) or (no_trumph==True and ((opponent1[2]==0)or total_count[2]==0)))):
                count[2]=count[2]-1
                throw_card=my_diamond[0]
                my_diamond.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              elif (((round_winner==0) or playing_cards["diamond"].index(my_diamond[0])==0 or (no_trumph==True and ((opponent1[2]==0)or total_count[2]==0))) and ((throw_count1[2]>0) and (no_trumph==True and ((opponent1[2]==0)or total_count[2]==0)))):
                count[2]=count[2]-1
                throw_card=my_diamond[0]
                my_diamond.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              elif (((round_winner==0) or playing_cards["diamond"].index(my_diamond[0])==0 or (no_trumph==True and ((opponent1[2]==0)or total_count[2]==0))) and ((throw_count1[2]>0) and ((no_trumph==True and ((opponent1[2]==0)or total_count[2]==0)) or ((total_count[2]-count[2]-1>=3) and (my_team[2]==0 or opponent2[2]==0))))):
                count[2]=count[2]-1
                throw_card=my_diamond[0]
                my_diamond.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              else:
                throw_card=my_diamond[count[2]-1]
                my_diamond.pop(count[2]-1)
                count[2]=count[2]-1
                my_cards.remove(throw_card)
                return {"card": throw_card}

            elif count[2]==0:

              if (((round_winner==0) or (no_trumph==True and ((opponent1[2]==0)or total_count[2]==0))) and ((throw_count1[2]==0) or (no_trumph==True and ((opponent1[2]==0)or total_count[2]==0)))):
                return {"card": last_card_noncolour1()}
              elif (((round_winner==0) or (no_trumph==True and ((opponent1[2]==0)or total_count[2]==0))) and ((throw_count1[2]>0) and (no_trumph==True and ((opponent1[2]==0)or total_count[2]==0)))):
                return {"card": last_card_noncolour1()}
              elif (((round_winner==0) or (no_trumph==True and ((opponent1[2]==0)or total_count[2]==0))) and ((throw_count1[2]>0) and ((no_trumph==True and ((opponent1[2]==0)or total_count[2]==0)) or ((total_count[2]-count[2]-1>=3) and (my_team[2]==0 or opponent2[2]==0))))):
                return {"card": last_card_noncolour1()}
              else:
                return {"card": third_card_noncolour2(round_winner,0)}
          elif round_winner==index_third[1]:
            if round_winner>=0:
              if count[2]!=0:                                                                #if I have diamond throw lowest diamond if my team lose
                if playing_cards["diamond"].index(my_diamond[0])<round_winner:
                  if ((throw_count1[2]==0) or (no_trumph==True and ((opponent1[2]==0)or total_count[2]==0))):
                    count[2]=count[2]-1
                    throw_card=my_diamond[0]
                    my_diamond.pop(0)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                  elif ((throw_count1[2]>0) and (no_trumph==True and ((opponent1[2]==0)or total_count[2]==0))):
                    count[2]=count[2]-1
                    throw_card=my_diamond[0]
                    my_diamond.pop(0)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                  elif ((throw_count1[2]>0) and ((no_trumph==True and ((opponent1[2]==0)or total_count[2]==0)) or ((total_count[2]-count[2]-1>=3) and (my_team[2]==0 or opponent2[2]==0)))):
                    count[2]=count[2]-1
                    throw_card=my_diamond[0]
                    my_diamond.pop(0)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                  else:
                    throw_card=my_diamond[count[2]-1]
                    my_diamond.pop(count[2]-1)
                    count[2]=count[2]-1
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                else:
                  throw_card=my_diamond[count[2]-1]
                  my_diamond.pop(count[2]-1)
                  count[2]=count[2]-1
                  my_cards.remove(throw_card)
                  return {"card": throw_card}
              elif count[2]==0:
                return {"card": third_card_noncolour2(round_winner,0)}
            elif round_winner<0:
              if count[2]!=0:
                throw_card=my_diamond[count[2]-1]
                my_diamond.pop(count[2]-1)
                count[2]=count[2]-1
                my_cards.remove(throw_card)
                return {"card": throw_card}
              elif count[2]==0:
                return {"card": third_card_noncolour2(round_winner,0)}

        elif played_cards[0][-1]=='H' and trumph[1]=='H':
          index_third[0]=playing_cards["heart"].index(played_cards[0])
          if played_cards[1][-1]=='H':
            index_third[1]=playing_cards["heart"].index(played_cards[1])
          else:
            opponent2[3]=0
            index_third[1]=98
          round_winner=min(index_third[0],index_third[1])
          if round_winner==index_third[0]:
            if count[3]!=0:
              if (round_winner==0):
                if count[3]==1:
                  count[3]=count[3]-1
                  throw_card=my_heart[0]
                  my_heart.pop(0)
                  my_cards.remove(throw_card)
                  return {"card": throw_card}
                elif count[3]==2:
                  if playing_cards["heart"].index(my_heart[0])==1:
                    count[3]=count[3]-1
                    throw_card=my_heart[1]
                    my_heart.pop(1)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                  else:
                    count[3]=count[3]-1
                    throw_card=my_heart[0]
                    my_heart.pop(0)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                elif count[3]==3:
                  if playing_cards["heart"].index(my_heart[0])==1:
                    if playing_cards["heart"].index(my_heart[1])==2:
                      count[3]=count[3]-1
                      throw_card=my_heart[2]
                      my_heart.pop(2)
                      my_cards.remove(throw_card)
                      return {"card": throw_card}
                    else:
                      count[3]=count[3]-1
                      throw_card=my_heart[1]
                      my_heart.pop(1)
                      my_cards.remove(throw_card)
                      return {"card": throw_card}
                  else:
                    count[3]=count[3]-1
                    throw_card=my_heart[0]
                    my_heart.pop(0)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                else:
                  if playing_cards["heart"].index(my_heart[0])==1:
                    count[3]=count[3]-1
                    throw_card=my_heart[1]
                    my_heart.pop(1)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                  else:
                    count[3]=count[3]-1
                    throw_card=my_heart[0]
                    my_heart.pop(0)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
              else:
                if playing_cards["heart"].index(my_heart[0])==0:
                  count[3]=count[3]-1
                  throw_card=my_heart[0]
                  my_heart.pop(0)
                  my_cards.remove(throw_card)
                  return {"card": throw_card}
                else:
                  throw_card=my_heart[count[3]-1]
                  my_heart.pop(count[3]-1)
                  count[3]=count[3]-1
                  my_cards.remove(throw_card)
                  return {"card": throw_card}  
            elif count[3]==0:   
              if (round_winner==0):
                return {"card": last_card_noncolour1()}  
              else:
                return {"card": last_card_noncolour3()}

          elif round_winner==index_third[1]:
            if count[3]!=0:
              if playing_cards["heart"].index(my_heart[0])==0:
                count[3]=count[3]-1
                throw_card=my_heart[0]
                my_heart.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              else:
                throw_card=my_heart[count[3]-1]
                my_heart.pop(count[3]-1)
                count[3]=count[3]-1
                my_cards.remove(throw_card)
                return {"card": throw_card}
            else:
              return {"card": last_card_noncolour3()}

        elif played_cards[0][-1]=='H' and trumph[1]!='H':
          index_third[0]=playing_cards["heart"].index(played_cards[0])
          if played_cards[1][-1]=='H':
            index_third[1]=playing_cards["heart"].index(played_cards[1])                #Looking who has highest cards
          elif played_cards[1][-1]==trumph[1]:
            opponent2[3]=0
            if played_cards[1][0]=='J':
              index_third[1]=-8
            if played_cards[1][0]=='9':
              index_third[1]=-7
            if played_cards[1][0]=='1':
              index_third[1]=-6
            if played_cards[1][0]=='T':
              index_third[1]=-5
            if played_cards[1][0]=='K':
              index_third[1]=-4
            if played_cards[1][0]=='Q':
              index_third[1]=-3
            if played_cards[1][0]=='8':
              index_third[1]=-2
            if played_cards[1][0]=='7':
              index_third[1]=-1
          else:
            opponent2[3]=0
            index_third[1]=97
          round_winner=min(index_third[0],index_third[1])
          if round_winner==index_third[0]:
            if count[3]!=0:                                                                #if I have heart throw highest heart if my team wins
              if (((round_winner==0) or playing_cards["heart"].index(my_heart[0])==0 or (no_trumph==True and ((opponent1[3]==0)or total_count[3]==0))) and ((throw_count1[3]==0) or (no_trumph==True and ((opponent1[3]==0)or total_count[3]==0)))):
                count[3]=count[3]-1
                throw_card=my_heart[0]
                my_heart.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              elif (((round_winner==0) or playing_cards["heart"].index(my_heart[0])==0 or (no_trumph==True and ((opponent1[3]==0)or total_count[3]==0))) and ((throw_count1[3]>0) and (no_trumph==True and ((opponent1[3]==0)or total_count[3]==0)))):
                count[3]=count[3]-1
                throw_card=my_heart[0]
                my_heart.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              elif (((round_winner==0) or playing_cards["heart"].index(my_heart[0])==0 or (no_trumph==True and ((opponent1[3]==0)or total_count[3]==0))) and ((throw_count1[3]>0) and ((no_trumph==True and ((opponent1[3]==0)or total_count[3]==0)) or ((total_count[3]-count[3]-1>=3) and (my_team[3]==0 or opponent2[3]==0))))):
                count[3]=count[3]-1
                throw_card=my_heart[0]
                my_heart.pop(0)
                my_cards.remove(throw_card)
                return {"card": throw_card}
              else:
                throw_card=my_heart[count[3]-1]
                my_heart.pop(count[3]-1)
                count[3]=count[3]-1
                my_cards.remove(throw_card)
                return {"card": throw_card}

            elif count[3]==0:

              if (((round_winner==0) or (no_trumph==True and ((opponent1[3]==0)or total_count[3]==0))) and ((throw_count1[3]==0) or (no_trumph==True and ((opponent1[3]==0)or total_count[3]==0)))):
                return {"card": last_card_noncolour1()}
              elif (((round_winner==0) or (no_trumph==True and ((opponent1[3]==0)or total_count[3]==0))) and ((throw_count1[3]>0) and (no_trumph==True and ((opponent1[3]==0)or total_count[3]==0)))):
                return {"card": last_card_noncolour1()}
              elif (((round_winner==0) or (no_trumph==True and ((opponent1[3]==0)or total_count[3]==0))) and ((throw_count1[3]>0) and ((no_trumph==True and ((opponent1[3]==0)or total_count[3]==0)) or ((total_count[3]-count[3]-1>=3) and (my_team[3]==0 or opponent2[3]==0))))):
                return {"card": last_card_noncolour1()}
              else:
                return {"card": third_card_noncolour2(round_winner,0)}
          elif round_winner==index_third[1]:
            if round_winner>=0:
              if count[3]!=0:                                                                #if I have heart throw lowest heart if my team lose
                if playing_cards["heart"].index(my_heart[0])<round_winner:
                  if ((throw_count1[3]==0) or (no_trumph==True and ((opponent1[3]==0)or total_count[3]==0))):
                    count[3]=count[3]-1
                    throw_card=my_heart[0]
                    my_heart.pop(0)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                  elif ((throw_count1[3]>0) and (no_trumph==True and ((opponent1[3]==0)or total_count[3]==0))):
                    count[3]=count[3]-1
                    throw_card=my_heart[0]
                    my_heart.pop(0)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                  elif ((throw_count1[3]>0) and ((no_trumph==True and ((opponent1[3]==0)or total_count[3]==0)) or ((total_count[3]-count[3]-1>=3) and (my_team[3]==0 or opponent2[3]==0)))):
                    count[3]=count[3]-1
                    throw_card=my_heart[0]
                    my_heart.pop(0)
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                  else:
                    throw_card=my_heart[count[3]-1]
                    my_heart.pop(count[3]-1)
                    count[3]=count[3]-1
                    my_cards.remove(throw_card)
                    return {"card": throw_card}
                else:
                  throw_card=my_heart[count[3]-1]
                  my_heart.pop(count[3]-1)
                  count[3]=count[3]-1
                  my_cards.remove(throw_card)
                  return {"card": throw_card}
              elif count[3]==0:
                return {"card": third_card_noncolour2(round_winner,0)}
            elif round_winner<0:
              if count[3]!=0:
                throw_card=my_heart[count[3]-1]
                my_heart.pop(count[3]-1)
                count[3]=count[3]-1
                my_cards.remove(throw_card)
                return {"card": throw_card}
              elif count[3]==0:
                return {"card": third_card_noncolour2(round_winner,0)}

  def first_turn():
    if (len(my_cards)==1):
      return {"card": my_cards[0]}
    else:
      step=0
      if (trumph[1]!=None):
        if (trumph[1]=='S'):
          if count[0]!=0:
            if playing_cards["spade"].index(my_spade[0])==0:
              step=1
              count[0]=count[0]-1
              throw_card=my_spade[0]
              my_spade.pop(0)
              my_cards.remove(throw_card)
              return {"card": throw_card}
        if (trumph[1]=='C'):
          if count[1]!=0:
            if playing_cards["club"].index(my_club[0])==0:
              step=1
              count[1]=count[1]-1
              throw_card=my_club[0]
              my_club.pop(0)
              my_cards.remove(throw_card)
              return {"card": throw_card}
        if (trumph[1]=='D'):
          if count[2]!=0:
            if playing_cards["diamond"].index(my_diamond[0])==0:
              step=1
              count[2]=count[2]-1
              throw_card=my_diamond[0]
              my_diamond.pop(0)
              my_cards.remove(throw_card)
              return {"card": throw_card}
        if (trumph[1]=='H'):
          if count[3]!=0:
            if playing_cards["heart"].index(my_heart[0])==0:
              step=1
              count[3]=count[3]-1
              throw_card=my_heart[0]
              my_heart.pop(0)
              my_cards.remove(throw_card)
              return {"card": throw_card}
      if (step==0):
        possibility=[0,0,0,0]    
        check=10    
        if(step==0):
          for i in range (sum(count)):
            if my_cards[i][0]=='J':
              if my_cards[i][-1]=='S' and total_count[0]==8:            
                possibility[0]=1
              if my_cards[i][-1]=='C' and total_count[1]==8:             
                possibility[1]=1
              if my_cards[i][-1]=='D' and total_count[2]==8:                      #throws J if that color is almost used and that is not the trumph we set             
                possibility[2]=1
              if my_cards[i][-1]=='H' and total_count[3]==8:        
                possibility[3]=1
          for i in range(len(possibility)):
            if(possibility[i]==1):
              step=1
              if (count[i]<check):
                check=count[i]
                n=i
          if(step==1):
            if(n==0):
              count[0]=count[0]-1
              my_spade.remove('JS')
              my_cards.remove('JS')
              throw_card='JS'
              return {"card": throw_card}
            if(n==1):
              count[1]=count[1]-1
              my_club.remove('JC')
              my_cards.remove('JC')
              throw_card='JC'
              return {"card": throw_card}
            if(n==2):
              count[2]=count[2]-1
              my_diamond.remove('JD')
              my_cards.remove('JD')
              throw_card='JD'
              return {"card": throw_card}
            if(n==3):
              count[3]=count[3]-1
              my_heart.remove('JH')
              my_cards.remove('JH')
              throw_card='JH'
              return {"card": throw_card}
      if (step==0):
        possibility=[0,0,0,0]    
        check=10 
        if count[0]!=0:
          if playing_cards["spade"].index(my_spade[0])==0 and no_trumph==True:
            possibility[0]=1
        if count[1]!=0:
          if playing_cards["club"].index(my_club[0])==0 and no_trumph==True:
            possibility[1]=1
        if count[2]!=0:
          if playing_cards["diamond"].index(my_diamond[0])==0 and no_trumph==True:
            possibility[2]=1
        if count[3]!=0:
          if playing_cards["heart"].index(my_heart[0])==0 and no_trumph==True:
            possibility[3]=1
        for i in range(len(possibility)):
          if(possibility[i]==1):
            step=1
            if (count[i]<check):
              check=count[i]
              n=i
        if(step==1):
          if(n==0):
            count[0]=count[0]-1
            throw_card=my_spade[0]
            my_spade.pop(0)
            my_cards.remove(throw_card)
            return {"card": throw_card}
          if(n==1):
            count[1]=count[1]-1
            throw_card=my_club[0]
            my_club.pop(0)
            my_cards.remove(throw_card)
            return {"card": throw_card}
          if(n==2):
            count[2]=count[2]-1
            throw_card=my_diamond[0]
            my_diamond.pop(0)
            my_cards.remove(throw_card)
            return {"card": throw_card}
          if(n==3):
            count[3]=count[3]-1
            throw_card=my_heart[0]
            my_heart.pop(0)
            my_cards.remove(throw_card)
            return {"card": throw_card}
      if (step==0):
        return {"card": last_card_noncolour3()}

  def second_turn():
    if (len(my_cards)==1):
      return {"card": my_cards[0]}
    else:
      if trumph[0]==False or trumph[1]==True:#or all trumph cards are finished
        if played_cards[0][-1]=='S':
          if count[0]!=0:
            if playing_cards["spade"].index(played_cards[0])==0:
              throw_card=my_spade[count[0]-1]
              my_spade.pop(count[0]-1)
              count[0]=count[0]-1
              my_cards.remove(throw_card)
              return {"card": throw_card}
            elif playing_cards["spade"].index(my_spade[0])==0 and total_count[0]==0:
              count[0]=count[0]-1
              throw_card=my_spade[0]
              my_spade.pop(0)
              my_cards.remove(throw_card)
              return {"card": throw_card}
            elif playing_cards["spade"].index(my_spade[0])==0 and total_count[0]==0:
              count[0]=count[0]-1
              throw_card=my_spade[0]
              my_spade.pop(0)
              my_cards.remove(throw_card)
              return {"card": throw_card} 
            elif playing_cards["spade"].index(my_spade[0])==0 and (no_trumph==True and ((opponent1[0]==0)or total_count[0]==0)):
              count[0]=count[0]-1
              throw_card=my_spade[0]
              my_spade.pop(0)
              my_cards.remove(throw_card)
              return {"card": throw_card}
            else:
              throw_card=my_spade[count[0]-1]
              my_spade.pop(count[0]-1)
              count[0]=count[0]-1
              my_cards.remove(throw_card)
              return {"card": throw_card}
          elif count[0]==0:
            return {"card": last_card_noncolour2(0)}

        if played_cards[0][-1]=='C':
          if count[1]!=0:
            if playing_cards["club"].index(played_cards[0])==0:
              throw_card=my_club[count[1]-1]
              my_club.pop(count[1]-1)
              count[1]=count[1]-1
              my_cards.remove(throw_card)
              return {"card": throw_card}
            elif playing_cards["club"].index(my_club[0])==0 and total_count[1]==0:
              count[1]=count[1]-1
              throw_card=my_club[0]
              my_club.pop(0)
              my_cards.remove(throw_card)
              return {"card": throw_card}
            elif playing_cards["club"].index(my_club[0])==0 and total_count[1]==0:
              count[1]=count[1]-1
              throw_card=my_club[0]
              my_club.pop(0)
              my_cards.remove(throw_card)
              return {"card": throw_card} 
            elif playing_cards["club"].index(my_club[0])==0 and (no_trumph==True and ((opponent1[1]==0)or total_count[1]==0)):
              count[1]=count[1]-1
              throw_card=my_club[0]
              my_club.pop(0)
              my_cards.remove(throw_card)
              return {"card": throw_card}
            else:
              throw_card=my_club[count[1]-1]
              my_club.pop(count[1]-1)
              count[1]=count[1]-1
              my_cards.remove(throw_card)
              return {"card": throw_card}
          elif count[1]==0:
            return {"card": last_card_noncolour2(0)}

        if played_cards[0][-1]=='D':
          if count[2]!=0:
            if playing_cards["diamond"].index(played_cards[0])==0:
              throw_card=my_diamond[count[2]-1]
              my_diamond.pop(count[2]-1)
              count[2]=count[2]-1
              my_cards.remove(throw_card)
              return {"card": throw_card}
            elif playing_cards["diamond"].index(my_diamond[0])==0 and total_count[2]==0:
              count[2]=count[2]-1
              throw_card=my_diamond[0]
              my_diamond.pop(0)
              my_cards.remove(throw_card)
              return {"card": throw_card}
            elif playing_cards["diamond"].index(my_diamond[0])==0 and total_count[2]==0:
              count[2]=count[2]-1
              throw_card=my_diamond[0]
              my_diamond.pop(0)
              my_cards.remove(throw_card)
              return {"card": throw_card} 
            elif playing_cards["diamond"].index(my_diamond[0])==0 and (no_trumph==True and ((opponent1[2]==0)or total_count[2]==0)):
              count[2]=count[2]-1
              throw_card=my_diamond[0]
              my_diamond.pop(0)
              my_cards.remove(throw_card)
              return {"card": throw_card}
            else:
              throw_card=my_diamond[count[2]-1]
              my_diamond.pop(count[2]-1)
              count[2]=count[2]-1
              my_cards.remove(throw_card)
              return {"card": throw_card}
          elif count[2]==0:
            return {"card": last_card_noncolour2(0)}

        if played_cards[0][-1]=='H':
          if count[3]!=0:
            if playing_cards["heart"].index(played_cards[0])==0:
              throw_card=my_heart[count[3]-1]
              my_heart.pop(count[3]-1)
              count[3]=count[3]-1
              my_cards.remove(throw_card)
              return {"card": throw_card}
            elif playing_cards["heart"].index(my_heart[0])==0 and total_count[3]==0:
              count[3]=count[3]-1
              throw_card=my_heart[0]
              my_heart.pop(0)
              my_cards.remove(throw_card)
              return {"card": throw_card}
            elif playing_cards["heart"].index(my_heart[0])==0 and total_count[3]==0:
              count[3]=count[3]-1
              throw_card=my_heart[0]
              my_heart.pop(0)
              my_cards.remove(throw_card)
              return {"card": throw_card} 
            elif playing_cards["heart"].index(my_heart[0])==0 and (no_trumph==True and ((opponent1[2]==0)or total_count[3]==0)):
              count[3]=count[3]-1
              throw_card=my_heart[0]
              my_heart.pop(0)
              my_cards.remove(throw_card)
              return {"card": throw_card}
            else:
              throw_card=my_heart[count[3]-1]
              my_heart.pop(count[3]-1)
              count[3]=count[3]-1
              my_cards.remove(throw_card)
              return {"card": throw_card}
          elif count[3]==0:
            return {"card": last_card_noncolour2(0)}

      elif trumph[0]==True:
        pass

  if played_cards ==[]:
    
    first_turn()
  elif (len(played_cards)==1):
    second_turn()
  elif (len(played_cards)==2):
    third_turn()
  elif (len(played_cards)==3):
    last_turn()


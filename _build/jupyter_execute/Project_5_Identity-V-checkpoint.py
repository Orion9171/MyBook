#!/usr/bin/env python
# coding: utf-8

# In[1]:


#第五人格

count=0
while count<3:
    phone=input('enter your phone number:')
    if(phone=='0909198701'):
        print('歡迎來到莊園')
        break
    else:
        count+=1
        print('invalid-identification')
 
#當你翻開日記時啟動角色介紹
class character:
    def __init__(c,name,power,weapon):
        c.name=name
        c.power=power
        c.weapon=weapon
    def print_info(c,title):
        print(title)
        print('Name:',c.name)
        print('Power:',c.power)
        print('Weapon:',c.weapon)
player1=character('Emma',power=45,weapon='toolbox')
player1.print_info('--Emma--')
player2=character('Pearson',power=52,weapon='flashlight')
player2.print_info('--Pearson--')
player3=character('Freddy',power=10,weapon='map')
player3.print_info('--lawyer_Freddy--')
player4=character('Lucky boy',power=10,weapon=None) #finding red boxes to get weapon
player4.print_info('--Lucky boy--')

class villain:
    def __init__(v,name,power,weapon):
        v.name=name
        v.power=power
        v.weapon=weapon
    def print_info(v,title):
        print(title)
        print('Name:',v.name)
        print('Power:',v.power)
        print('Weapon:',v.weapon)
ghost1=villain('廠長',power=60,weapon='鯊魚棒')
ghost1.print_info('--廠長--')
ghost2=villain('小丑',power=75,weapon='火箭筒')
ghost2.print_info('--小丑--')
ghost3=villain('開膛手傑克',power=85,weapon='霧刃和大手')
ghost3.print_info('--開膛手傑克--')

count=0
while count<2:
    hits=input('do players get hits?')
    if(hits=='n'):
        print('*專心破譯*')
        continue
    else:
        hits=='y'
        count+=1
        print('*受傷%d次,我需要幫助!*'%count)
print('2次受傷上椅子')

while True:        
    log_out=input('enter q to quit game') #登出離開
    if(log_out=='q'):
        break
    
while True:
    attack=int(input('death number:'))
    if(attack==4 or 3):
        print('you win!')
        #第五人格

count=0
while count<3:
    phone=input('enter your phone number:')
    if(phone=='0909198701'):
        print('歡迎來到莊園')
        break
    else:
        count+=1
        print('invalid-identification')
 
#當你翻開日記時啟動角色介紹
class character:
    def __init__(c,name,power,weapon):
        c.name=name
        c.power=power
        c.weapon=weapon
    def print_info(c,title):
        print(title)
        print('Name:',c.name)
        print('Power:',c.power)
        print('Weapon:',c.weapon)
player1=character('Emma',power=45,weapon='toolbox')
player1.print_info('--Emma--')
player2=character('Pearson',power=52,weapon='flashlight')
player2.print_info('--Pearson--')
player3=character('Freddy',power=10,weapon='map')
player3.print_info('--lawyer_Freddy--')
player4=character('Lucky boy',power=10,weapon=None) #finding red boxes to get weapon
player4.print_info('--Lucky boy--')

class villain:
    def __init__(v,name,power,weapon):
        v.name=name
        v.power=power
        v.weapon=weapon
    def print_info(v,title):
        print(title)
        print('Name:',v.name)
        print('Power:',v.power)
        print('Weapon:',v.weapon)
ghost1=villain('廠長',power=60,weapon='鯊魚棒')
ghost1.print_info('--廠長--')
ghost2=villain('小丑',power=75,weapon='火箭筒')
ghost2.print_info('--小丑--')
ghost3=villain('開膛手傑克',power=85,weapon='霧刃和大手')
ghost3.print_info('--開膛手傑克--')

count=0
while count<2:
    hits=input('do players get hits?')
    if(hits=='n'):
        print('*專心破譯*')
        break
    else:
        hits=='y'
        count+=1
        print('*受傷%d次,我需要幫助!*'%count)
print('2次受傷上椅子')

while True:        
    log_out=input('enter q to quit game') #登出離開
    if(log_out=='q'):
        break
    
while True:
    attack=int(input('death number:'))
    if(attack==4 or 3):
        print('you win!')
        continue
        if(attack==2):
            print('equal')
    else:
        attack<2
        print('you lose!')
        
    log_out=input('enter q to quit game') #登出離開
    if(log_out=='q'):
        print('登出')
        break
    else:
        continue


# In[ ]:





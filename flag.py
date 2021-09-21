#Tihsrah's war codes
'''
It is the time of war when military soldiers use to send their messages through codes. 
Tihsrah a great scientist made a message encryptor that enciphers the message into a ten-word combination.
He knows how to crack the coded message into human text.
So he secretly sold his device to the enemy nations so that whatever message they were to impart among them could be deciphered easily.
Well, the enemy nations started sending messages on the battlefield and our radars have caught 5 words in the coded message.

MAAB LEBC _____ KODE OUEF _____  _____ IIHI...

Now being Tihsrah's henchman you must bring all the coded words to him so that he could decipher the whole message before it's too late.
Get to work soldier!
GET ALL THE COMBINATIONS CORRECTLY!
HURRY!
'''
'''
hint: This world is full of patterns!
'''

#solution code

count=1
vowl=['A','E','I','O','U']
tempvowl=0
ky=[]
for i in range(65,91):
    ky.append(chr(i))
temp1="M"
temp1cnt=1
temp2=""
temp3=""
result=""
diff=0
off=12
for i in range(10):
    count=i
    if diff==0:
        temp1=ky[off]
        diff=diff+1
    elif (diff%2!=0):
        off=off-diff
        temp1=ky[off]
        diff=diff+1
    elif (diff%2==0):
        off=off+diff
        temp1=ky[off]
        diff=diff+1
    if(tempvowl==5):
        tempvowl=0
    temp2=vowl[tempvowl]
    tempvowl=tempvowl+1   
    temp3=str(ky[count])+str(ky[count+1])
    result=str(temp1)+str(temp2)+str(temp3)
    print(result,end=" ")

'''output: MAAB LEBC NICD KODE OUEF JAFG PEGH IIHI QOIJ HUJK '''
            
            
   

    
    

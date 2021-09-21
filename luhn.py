num1='543210'
num2='1234'
lit=[]
lit_div=[]
valid=[]
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for m in range(10):
                    for n in range(10):
                        h=str(i)+str(j)+str(k)+str(l)+str(m)+str(n)
                        lit.append(int(num1+h+num2))

for i in lit:
    if(int(i)%123457==0):
        lit_div.append(str(i))

def checkLuhn(cardNo):
     
    nDigits = len(cardNo)
    nSum = 0
    isSecond = False
     
    for i in range(nDigits - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')
     
        if (isSecond == True):
            d = d * 2
        nSum += d // 10
        nSum += d % 10
  
        isSecond = not isSecond
     
    if (nSum % 10 == 0):
        return True
    else:
        return False
  
for i in lit_div:
    if (checkLuhn(i)):
        valid.append(i)

for i in valid:
    print(i)
     
    

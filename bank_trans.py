net_amount=0
transaction=[]
while True:
    str1=input("Enter the transaction:")
    transaction=str1.split(" ")
    typ=transaction[0]
#    amount=int(transaction[1])
    if (typ=="D") or (typ=="d"):
        net_amount+=int(transaction[1])
    elif (typ=="W") or (typ=="w"):
        net_amount-=int(transaction[1])
    else:
      break
        	
print("Net Amount:",net_amount)

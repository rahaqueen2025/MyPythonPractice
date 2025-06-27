class Wallet:
    def __init__(self,initial_balance):
        self.balance=initial_balance

    def get_balance(self):
        print(f"you have {self.balance}$ is in your wallet")

    def __str__(self):
        return f"this wallet contains {self.balance}$"    
    
    def __add__(self, other):
        return self.balance + other.balance
    
    def __sub__(self,other):
        return self.balance - other.balance
    
    def __mul__(self,other):
        return self.balance *other.balance
    
    def __eq__(self,other):
        return self.balance==other.balance
    
    def __lt__(self,other):
        return self.balance<other.balance
    
    def __gt__(self,other):
        return self.balance>other.balance
    
    def __ne__(self,other):
        return self.balance != other.balance
    
    def __len__(self):
        return self.balance
        
wallet_1=Wallet(500)
wallet_2=Wallet(100)
        

#wallet_1.get_balance()
#print(wallet_1.balance)
#print(wallet_1)
#print(wallet_1 + wallet_2) 
#print (wallet_1 - wallet_2) 
#print(wallet_1*wallet_2)  
#print(wallet_1==wallet_2)
#print(wallet_1<wallet_2)
#print(wallet_1>wallet_2)
#print(wallet_1 != wallet_2)
#print(len(wallet_1))

#attr="balance"
#print(hasattr(wallet_1,"balance"))
#print(hasattr(wallet_1,"user"))

#attr="balance"
#print(getattr(wallet_1,attr))

#ttr="balance"
#print(setattr(wallet_1,attr,100))
#print(wallet_1)
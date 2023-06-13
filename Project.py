#Implementation Code

class Date:
    def __init__(self,d,m,y):
        self.day=d
        self.month=m
        self.year=y
    def disdate(self):
        return (self.day,self.month,self.year)
#composition
class Person:
    def __init__(self,n,c,i,dday,dmonth,dyear):
        self.name=n
        self.number=c
        self.id=i
        self.joindate= Date(dday,dmonth,dyear)

    def setname(self,n):
        self.name=n
    def setnumber(self,c):
        self.number=c
    def setid(self,i):
        self.id=i
    def getname(self):
        return self.name
    def getnumber(self):
        return self.number
    def getid(self):
        return self.id

    def displayinfo(self):
        print("Name:",self.name)
        print("ID:",self.id)
        print("Cell Number:",self.number)
        print("Date of joining",self.joindate.disdate())
#inheritance
class customer(Person):
    def __init__(self,n,c,i,dday,dmonth,dyear,fee):
        super().__init__(n,c,i,dday,dmonth,dyear)
        self.fee=fee
    def setfee(self,fee):
        self.fee=fee
    def getfee(self):
        return self.fee
    def display(self):
        super().displayinfo(),print("Fee:",self.fee)
#Inheritance
class Trainer(Person):

    def __init__(self,n,c,i,dday,dmonth,dyear,salary):
        super().__init__(n,c,i,dday,dmonth,dyear)
        self.salary=salary

    def setsalary(self,salary):
        self.salary=salary
    def getsalary(self):
        return self.salary

    def display(self):
        super().displayinfo(),print("Salary:",self.salary)
class Equipment:

    def __init__(self,n,noe):
        self.name=n
        self.damaged=de

    def setname(self,n):
        self.name=n
    
    def setdamaged(self,d):
        self.damaged=d

    def getname(self):
        return self.name

    def getdamaged(self):
        return self.damaged

    def display(self):
        print("Equipment Name:",self.name)
        print("Damaged Condition?",self.damaged)
class Membership:

    def __init__(self,mt,perks,time,cost):
        self.type=mt
        self.perks=perks
        self.time=time
        self.cost=cost

    def settype(self,mt):
        self.type=mt
    def setperks(self,perks):
        self.perks=perks
    def settime(self,time):
        self.time=time
    def setcost(self,cost):
        self.cost=cost
    def gettype(self):
        return self.type
    def getperks(self):
        return self.perks
    def gettime(self):
        return self.time
    def getcost(self):
        return self.cost
    
    def display(self):
        print("Membership Type:",self.type)
        print("Perks:",self.perks)
        print("Time limit:",self.time)
        print("Cost:",self.cost)

class Payment:
    def __init__(self,pid,cid,pamount,duedate):
        self.paymentid=pid
        self.customerid=cid
        self.amount=pamount
        self.date=duedate

    def setpayid(self,pid):
        self.paymentid=pid
    def setcustid(self,cid):
        self.customerid=cid
    def setamount(self,pamount):
        self.amount=pamount
    def setdate(self,duedate):
        self.date=duedate
    def getpayid(self):
        return self.paymentid
    def getcustid(self):
        return self.customerid
    def getamount(self):
        return self.amount
    def getduedate(self):
        return self.date
    def display(self):
        print("Payment ID:",self.paymentid)
        print("Customer ID;",self.customerid)
        print("Amount:",self.amount)
        print("Due Date:",self.date)
    #Functions
class GymManager:
    def __init__(self,c=[],t=[],e=[],p=[],m=[]):
        self.customers=c
        self.trainer=t
        self.equipments=e
        self.payements=p
        self.membership=m

    def addcustomer(self,c):
        clist=[]
        self.customer=c
        clist.append(c)
        return clist
    def showmembership(self,m):
        mlist=[]
        self.membership=m
        mlist.append(m)
        return mlist
    def paymentreciept(self,p):
        plist=[]
        self.payment=p
        plist.append(p)
        return plist

    def equipment(self,x):
        e=[]
        for i in range(x):
            self.equipment=input("Enter Equipment Name:")
            e.append(self.equipment)
        return e

    def addtrainer(self,t):
        tlist=[]
        self.trainer=t
        tlist.append(t)
        return tlist

def menu():
    print("Gym Management System")
    print("Press 1 To Add Customers")
    print("Press 2 To Add Trainers")
    print("Press 3 To Update Specific Equipments Condition")
    print("Press 4 To Show Added Customers")
    print("Press 5 To Show Added Trainers")
    print("Press 6 To Show Available Membership")
    print("Press 7 To Add and Show Equipments")
    print("Press 8 To Make A Payment Reciept For A Customer")
    print("Press 9 To Open Menu Again")

menu()
gymobj=GymManager()

while(True):
    
    a=int(input("Enter Option Number: "))
    if a==1:
        z=int(input("How many customers you want to add:"))
        clist=[] # List for polymorphism
        for i in range (z):
            n=input("Input Name:")
            c=int(input("Input Cell Number:"))
            i=int(input("Input ID:"))
            dday=int(input("Input Day of joining:"))
            dmonth=int(input("Input Month Of Joining:"))
            dyear=int(input("Input Year"))
            fee=int(input("Input Fees"))
            Cobj=customer(n,c,i,dday,dmonth,dyear,fee)
            clist.append(Cobj)
            
       
        
        

    elif a==2:
        b=int(input("How many trainers you want to add:"))
        tlist=[]
        for x in range (b):
            n=input("Input Trainer Name:")
            c=int(input("Input Cell Number:"))
            i=int(input("Input ID:"))
            dday=int(input("Input Day of joining:"))
            dmonth=int(input("Input Month Of Joining:"))
            dyear=int(input("Input Year:"))
            salary=int(input("Input Salary per month:"))
            Tobj=Trainer(n,c,i,dday,dmonth,dyear,salary)
            tlist.append(Tobj)
            


    elif a==3:

        n=input("Input name of equipment:")
        de=input("Is it damaged ? Yes/No :")
        equipobj=Equipment(n,de)
        equipobj.display()
        
        
        
    


    elif a==4:
        #polymorphism
        for i in range(z):
            clist[i].display()

    
    
    elif a==5:
        #polymorphism
        for x in range(b):
            tlist[x].display()

    elif a==6:

        mt="Gold"
        perks="Personal Training"
        time="1 Month"
        cost="$5000 per month"
        mobj=Membership(mt,perks,time,cost)
        for i in(gymobj.showmembership(mobj)):
            i.display()
    elif a==7:
        x=int(input("Number of equipment you want to add:"))
        print("Equipments:",gymobj.equipment(x))

    elif a==8:

        pid=int(input("Input Paymentid (integer):"))
        cid=int(input("Input Customerid *integer):"))
        pamount=int(input("Amount due?:"))
        duedate=input("due date:")#eg: 3 june 
        pobj=Payment(pid,cid,pamount,duedate)

        for i in (gymobj.paymentreciept(pobj)):
            i.display()
        
    


    elif a==9:
        menu()
        


menu()
        
        
        
    
        



    

    
        

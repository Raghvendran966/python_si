sp=int(input("enter the selling price of item"))
cp =int(input("enter the cost price of item"))
if(sp>cp):
        p =sp-cp
        print("your profit is",p)
else:
        l= cp-sp
        print("your loss is ",l)

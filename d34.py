Key = [ 'Mango', 'Banana', 'Apple']
Value = [40, 50,100]
res= { 'Key' : ['Mango', 'Banana', 'Apple'],
       'Value': [40, 50,100]}
res=[{'Key':i, 'Value':j} for i in res['Key']
    for j in res['Value']]
print("All key value paired List:"+str(res))
                 

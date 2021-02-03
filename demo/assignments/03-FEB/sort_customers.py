
input = ['Mike,4848484844','Joe,1919193233','Jack,3838333333',
         'Andy,191919933','Roberts,3838383333', 'Andy,9494949444',
         'Andy,9494949444', 'Joe,39391919121','Jack,39392911334']

customers = {}

for entry in input:
    name,mobile = entry.split(",")
    if name in customers:
        customers[name].add(mobile)   # Add new number to existing set
    else:
        # Create a new entry with name as key and mobile number as entry in set
        customers[name] = {mobile}


for name, mobiles in sorted(customers.items()):
     print(f"{name:15} {','.join(mobiles)}")


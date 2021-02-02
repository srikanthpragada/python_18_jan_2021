
input = ['Mike,4848484844','Joe,1919193233','Jack,3838333333',
         'Andy,191919933','Roberts,3838383333', 'Andy,9494949444']

customers = {}

for entry in input:
    name,mobile = entry.split(",")
    customers[name] = mobile

for name, mobile in sorted(customers.items()):
     print(f"{name:15} {mobile}")

# for name in sorted(customers):
#      print(f"{name:15} {customers[name]}")
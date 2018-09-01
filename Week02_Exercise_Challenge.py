"""
09/02/2018
Jiang Nixuan

Exercises and Challenges
Design and calculate a media business model

"""

#Major cost
content_cost = 70000
labor_cost = 30000
server_cost = 50000

# Calculate function
def calculate(visitor):
    subscriber = int(visitor) / 10
    subscription_fee = subscriber * 15
    ad_revenue = 0.8 * float(visitor)

    net_income = subscription_fee + ad_revenue - content_cost - labor_cost - server_cost

    return net_income

# User type number here  (logic is the same as def above)
visitor = input('Please input the number of monthly visitors: ')

subscriber = int(visitor)/10
subscription_fee = subscriber*15
ad_revenue = 0.8*float(visitor)

net_income = subscription_fee + ad_revenue - content_cost - labor_cost - server_cost

print(net_income)



# when visitor equals 40000, 60000 and 80000, respectively.
print('\n')
print("If the number of visitors is 40000 \n")
print(calculate(40000))

print('\n')
print("If the number of visitors is 60000 \n")
print(calculate(60000))

print('\n')
print("If the number of visitors is 80000 \n")
print(calculate(80000))

"""
09/02/2018
Jiang Nixuan

Exercises and Challenges
Design and calculate a media business model (optional)

"""

# Major cost
# HKBU students decide to invest 50000 in IT infrastructure (ex. server)
content_cost = 70000
labor_cost = 30000
IT_infrastructure_cost = 50000


def calculate(visitor):
    subscriber = int(visitor) / 10
    subscription_fee = subscriber * 15
    ad_revenue = 0.8 * float(visitor)

    # If the number of visitors is equal to or smaller than 50000
    if(visitor < 50000):
        net_income = subscription_fee + ad_revenue - content_cost - labor_cost - IT_infrastructure_cost
    # If the number of visitors is lager than 50000
    else:
        net_income = subscription_fee + ad_revenue - content_cost - labor_cost - IT_infrastructure_cost + (visitor-50000)*0.001

    return net_income


visitor = float(input('Please type number of visitors: '))

print(calculate(visitor))
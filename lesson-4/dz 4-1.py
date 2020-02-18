from sys import argv

script_name, production, rate, premium = argv

production = int(production)
hour_rate = int(rate)
premium = int(premium)

salary = production * hour_rate + premium
print(salary)

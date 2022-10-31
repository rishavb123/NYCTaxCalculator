from constants import *
from calculator import calc_tax

base_income = 250000
bonus_income = 212500

total_tax = bonus_income * bonus_tax / 100 + calc_tax(base_income, federal_brackets) + calc_tax(base_income, state_brackets) + calc_tax(base_income, city_brackets)

print("Pre-Tax Income:", base_income + bonus_income)
print("Total Tax:", total_tax)
print("Post-Tax Income:", base_income + bonus_income - total_tax)

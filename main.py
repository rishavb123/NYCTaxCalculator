import sys

from constants import *
from calculator import calc_tax

base_income = 250000 if len(sys.argv) < 2 else int(sys.argv[1])
bonus_income = 212500 if len(sys.argv) < 3 else int(sys.argv[2])

total_tax = bonus_income * bonus_tax / 100 + calc_tax(base_income, federal_brackets) + calc_tax(base_income, state_brackets) + calc_tax(base_income, city_brackets)

print("Pre-Tax Income:", base_income + bonus_income)
print("Total Tax:", total_tax)
print("Post-Tax Income:", base_income + bonus_income - total_tax)
print("Average Tax Rate:", total_tax / (base_income + bonus_income))

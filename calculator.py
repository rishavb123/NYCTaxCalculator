def calc_tax(income, brackets):
    cur_val = income
    last_cap = 0
    tax = 0
    for (tax_rate, cap) in brackets:
        taxable_val = min(cur_val, cap - last_cap)
        tax += taxable_val * tax_rate / 100
        cur_val -= taxable_val
        last_cap = cap
        if cur_val <= 0: break
    return tax

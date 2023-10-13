# PA106/G/9556/20
# Mutwiri Brian Muthomi
gross_pay = float(input("Enter your gross pay: "))


tax_rates = {
    10000: 0.0,  
    20000: 0.10,  
    30000: 0.15,  
    40000: 0.25,  
}


tax_amount = 0
for bracket, rate in tax_rates.items():
    if gross_pay > bracket:
        taxable_income = min(gross_pay - bracket, gross_pay - max(tax_rates.keys()))
        tax_amount += taxable_income * rate

net_pay = gross_pay - tax_amount


print(f"Gross Pay: ${gross_pay:.2f}")
print(f"Tax Amount: ${tax_amount:.2f}")
print(f"Net Pay: ${net_pay:.2f}")

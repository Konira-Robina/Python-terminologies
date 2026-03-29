# write down steps (each step) with a statement(code examples) on how u can create someone"s net pay after tax.
# Step 1: Display a Welcome message
print("Welcome")
# The user enters their salary before tax.

# Step 2: The user inputs gross pay
print("Net Pay Calculation")
# We convert gross pay to float, because the value entered initially was a string.
# float is used because salary can include decimals.
gross_pay = float(input("Enter your gross pay: "))

# Step 3: Get tax rate
# tax rate is 10% of the total pay.
# In programming, percentages are written as decimals therefore;
tax_rate = 0.10

# Step 4: Calculating the tax amount
# Here, we calculate how much tax should be deducted.
# Multiply gross pay by tax_rate.
tax = gross_pay * tax_rate

# Step 5: Calculating net_pay
# Net_pay is what remains after tax is removed
# substract tax from gross pay
net_pay = gross_pay - tax
 
 # Step 6: Display results
print("Gross Pay:", gross_pay)
print("Tax Deducted:", tax)
print("Net Pay:", net_pay)
#Problem Set 1 (27-05-2023)
#Name: Sai Kelkar
#Time: 11.30 am

annual_salary = int(input("Enter your annual salary: ")) 
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ")) 

total_cost = int(input("Enter the cost of your dream home: ")) 
portion_down_payment = total_cost * 0.25 

semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

current_savings = 0
number_of_months = 0

while current_savings < portion_down_payment:
    current_savings += (annual_salary * portion_saved / 12) + current_savings * 0.04 / 12
    number_of_months += 1 

    if number_of_months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise

print( "Number of months:", number_of_months )

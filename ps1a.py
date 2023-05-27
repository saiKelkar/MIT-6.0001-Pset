#Problem Set 1 (27-05-2023)
#Name: Sai Kelkar
#Time: 10.30 am

annual_salary = int(input("Enter your annual salary: ")) 
monthly_salary = annual_salary / 12 
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ")) 

total_cost = int(input("Enter the cost of your dream home: ")) 
portion_down_payment = total_cost * 0.25 

current_savings = 0
number_of_months = 0

while current_savings < portion_down_payment:
    current_savings += (monthly_salary * portion_saved) + current_savings * 0.04 / 12
    number_of_months += 1 

print( "Number of months:", number_of_months )

# Write your code below:

wage = float(input("Enter the wage: "))
hours = float(input("Enter the regular hours: "))
overtime = float(input("Enter the overtime hours: "))
overtimeRate = 1.5 * wage
overtimePay = overtimeRate * overtime
total = (hours * wage) + overtimePay

print("The total weekly pay is $" + str(total))

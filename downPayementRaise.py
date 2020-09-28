
# cost of dream house
totalCost = float(input("Cost of house "))
# percent downpayemnt
portion_down_payment= 0.25

currentSavings = 0.0
 # function for each month investement gain
 #  current_savings*r/12
r = 0.04 # percentage investement gain
annualSalary = float(input("Your Annual Salary: "))
portionSaved = float(input("Portion Saved ")) # protion saved for downpayement from salary
semi_year_raise = float(input("Raise Increase % "))
monthlySaved = portionSaved * annualSalary / 12
numberOfMonths = 0

# loop every month and increase the savings once the savings is = or > than stop
while currentSavings < portion_down_payment * totalCost:
    currentSavings += monthlySaved + (currentSavings*r/12)
    if (numberOfMonths) % 6 == 0 :
        monthlySaved *= (1+semi_year_raise)

    numberOfMonths+=1
print(numberOfMonths)

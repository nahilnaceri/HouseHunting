semiRaise = 0.07
r = 0.04
downpayemntPerc = 0.25
houseCost = 1000000.0
monthsToBuy = 36
annualSalary = 300000
currentSavings = 0.0
high = 1.0
low = 0.0
mid =(high + low) / 2
mid = round(mid,4)
monthlySaved = mid * annualSalary / 12
bisectionNum = 1
while abs(currentSavings - houseCost * downpayemntPerc) > 100:
    currentSavings = 0.0
    monthlySaved = mid * annualSalary / 12
    for i in range(1,37):
        currentSavings += monthlySaved + (currentSavings*r/12)
        if i % 6 == 0:
            monthlySaved *= (1+semiRaise)
    if currentSavings < houseCost * downpayemntPerc :
        low = mid
        mid = (high + low) / 2
        mid = round(mid,4)
    else:
        high = mid
        mid = (high + low) / 2
        mid = round(mid,4)
    if high == low :
        print("Impossible to pay")
        break
    print(mid,abs(currentSavings - houseCost * downpayemntPerc))

    bisectionNum +=1
    # if currentSavings >= houseCost * downpayemntPerc :
    #     break

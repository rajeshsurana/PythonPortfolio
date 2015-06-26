def pay(balance, annualInterestRate, minMonthlyPay):

    totPaid = 0.0
    
    for month in range(1,13):
        totPaid += minMonthlyPay
        balRemain = balance - minMonthlyPay
        balance = balRemain + balRemain * (annualInterestRate / 12.0)
    return balance
    
def findMinMontlyPay(balance, annualInterestRate):
    finalBalRemain = 10.0
    lowPay = balance / 12
    highPay = (balance * (1 + annualInterestRate/12.0) ** 12) / 12.0
    monthlyPay = 0
    while True:
        monthlyPay = (lowPay + highPay) / 2
        finalBalRemain = pay(balance, annualInterestRate, monthlyPay)
        if finalBalRemain <= 0.01 and finalBalRemain >= -0.01:
            break
        if finalBalRemain > 0:
            lowPay = monthlyPay
        else:
            highPay = monthlyPay

    print 'Lowest Payment:', round(monthlyPay, 2)


            
findMinMontlyPay(320000, 0.2)
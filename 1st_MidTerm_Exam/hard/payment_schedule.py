loan_amount = eval(input("Enter loan amount: "))
loan_period = (eval(input("Enter loan period in years: ")))

loan_period *= 12 # to convert the input year\s to a month
principal = loan_amount/loan_period
balance = loan_amount
interest = 0
print("PAYMENT SCHEDULE")
print("Month\t|Monthly Payment\t|Interest\t|Principal\t|Remaining Loan")
print("-"*80)
for i in range(1,loan_period+1,1):
    balance -= principal
    interest = balance * 0.0125
    monthly = interest + principal
    print(f"{i}\t|{round(monthly,2)}\t\t\t|{round(interest,2)}\t\t|{round(interest,2)}\t\t|{round(principal,2)}")

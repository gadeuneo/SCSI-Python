# James Gardner

money = 732 # change

dollar = money / 100 # number of dollars to give
dollarR = money % 100 # amount of change left

quarter = dollarR / 25 # number of quarters to give
quarterR = dollarR % 25 # amount of change left

dime = quarterR / 10 # number of dimes to give
dimeR = quarterR % 10 #amount of change left

nickel = dimeR / 5 # number of nickels to give
nickelR = dimeR % 5 # amount of change left

penny = nickelR / 1 # number of pennies to give

print
print "Dollars:", dollar
print "Quarters:", quarter
print "Dimes:", dime
print "Nickels:", nickel
print "Pennies:", penny


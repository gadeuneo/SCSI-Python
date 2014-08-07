# James Gardner

money = 45447 # change

onehundreddollar = money / 10000 # number of one hundred dollars to give
onehundreddollarR = money % 10000 # amount of change left

fiftydollar = onehundreddollarR / 5000 # number of fifty dollars to give
fiftydollarR = onehundreddollarR % 5000 # amount of change left

twentydollar = fiftydollarR / 2000 # number of twenty dollars to give
twentydollarR = fiftydollarR % 2000 # amount of change left

tendollar = twentydollarR / 1000 # number of ten dollars to give
tendollarR = twentydollarR % 1000 # amount of change left

fivedollar = tendollarR / 500 # number of five dollars to give
fivedollarR = tendollarR % 500 # amount of change left

dollar = fivedollarR / 100 # number of dollars to give
dollarR = fivedollarR % 100 # amount of change left

quarter = dollarR / 25 # number of quarters to give
quarterR = dollarR % 25 # amount of change left

dime = quarterR / 10 # number of dimes to give
dimeR = quarterR % 10 #amount of change left

nickel = dimeR / 5 # number of nickels to give
nickelR = dimeR % 5 # amount of change left

penny = nickelR / 1 # number of pennies to give

print
print "One Hundred Dollars:", onehundreddollar
print "Fifty Dollars:", fiftydollar
print "Twenty Dollars:", twentydollar
print "Ten Dollars:", tendollar
print "Five Dollars:", fivedollar
print "Dollars:", dollar
print "Quarters:", quarter
print "Dimes:", dime
print "Nickels:", nickel
print "Pennies:", penny

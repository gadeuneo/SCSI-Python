# James Gardner

bedLen = 2 # in feet
bedWid = 1.5 # in feet
flowerWid = 6 # in inches
flowerLen = 6 #in inches

bedLenInch = bedLen * 12 # bedLen in inches
bedWidInch = bedWid * 12 # bedWid in inches

totalArea = bedLenInch * bedWidInch #total area in square inches

flowerArea = flowerWid * flowerLen #in inches

flowerNum = totalArea / flowerArea

print
print flowerNum

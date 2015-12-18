hrs = raw_input("Enter Worked Hours in the Previous Week:")
try:
    hrs = float(hrs)
except:
    hrs = -1
if  hrs > 0 :
    if hrs > 40 :
        print "You've worked extra hours"
        ehrs = hrs - 40
        pay = (10.5*40) + ehrs*10.5*1.5
        print pay
    else :
        print "You have worked ", hrs ," hours"
        pay = (8*hrs)
        print "You will get pay ", pay ,"euros;"
    print "Enjoy your wage"
else:
    print "Not a number"

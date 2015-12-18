def computepay(hrs,rph):
    if hrs > 40 :
        pay = (rph*40) + (hrs - 40)*rph*1.5
    else :
        pay = (rph*hrs)
    return pay
try:
    hrs = raw_input("Enter Hours:")
    hrs = float(hrs)
    rph = raw_input("Enter Rate per Hours:")
    rph = float(rph)
except:
    print 'Error, please enter numeric input' 
p = computepay(hrs,rph)
print "Pay",p
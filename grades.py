grade = raw_input("Enter your Score (between 0.0 and 1.0):")
try:
    grade = float(grade)
except:
    grade = -1
if grade < 0 :
    print "Error: enter a correct grade"
elif grade > 1:
    print "Error: enter a correct grade"
elif grade >= 0.9:
    print "A"
elif grade >= 0.8:
    print "B"
elif grade >= 0.7:
    print "C"
elif grade >= 0.6:
    print "D"
else :
    print "F"
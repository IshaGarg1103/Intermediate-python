# %, format(), f-strings

#% method
var="Tom"
age=18
percentile=92.3498
mystr="my name is %s and my age is %d and my percentile is %.2f%% %s" % (var, age,percentile,var)
print(mystr) #my name is Tom and my age is 18 and my cgpa is 9.23

#format()
mystr= "the variable is {:.2f} and {}".format(percentile,age)
print(mystr)
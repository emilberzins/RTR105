Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter rate:")
r = float(rate)
pay  = h * r 

if h <=40:
    pay  = h * r  
else:
    pay = r * 40 + (r * 1.5 * ( h - 40 ))
    print pay
    
Enter Hours:45
>>> 





























>>> inp = raw_input ('Enter Hours: ')
hours = float(inp)
inp = raw_input ('Enter Rate: ')
rate = float(inp)

print rate, hours

if hours <= 40 :
   pay = hours * rate
else :
   pay = rate * 40 + (rate * 1.5 * ( hours - 40 ))

print pay
Enter Hours:

    def computepay(hours,rate):
 if hours>40.0:
  p = rate * 40.0
  p = p+(1.5*rate*(hours-40))
 else:
  p = rate*hours
 return p
hours = float(raw_input("Enter worked hours: "))
rate = float(raw_input("Enter Pay rate per hour: "))
print(computepay(hours,rate))



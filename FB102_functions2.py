
# ********************************
# functions

def fibonacci( n ):
    a, b = 0, 1
    while b < n:
        print( b )
        a, b = b, a+b
        
def fibonacci3( n ):
    a, b = 0, 1
    while b < n:print( b );a, b = b, a+b

def multiplyage( name, age, mult):
   "This prints a passed info into this function"
   print "Name:",name,"| Age:",age,"|Mult:",mult
   age2= age*mult  
   return age2;

# ********************************
# Now you can call printinfo function
fibonacci( 100 )
print"--"
age2 = multiplyage( age=50, name="miki",mult=4 )
print age2
print"--"
age2 = multiplyage("ebu",22,4)
print age2
print"--"


input( '\n\nPress Enter to exit...' )

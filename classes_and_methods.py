class foo:
	def bar(self): #The 'self' is a reference to the class instance
		print ("Hi")
#Now we can create an instance of foo and call the method on it, the self parameter is added by Python in this case:
f = foo()
f.bar()
print("Printed f.bar()")

#But it can be passed in as well if the method call isn't in the context of an instance of the class
f = foo()
foo.bar(f)

#Interestingly the variable name 'self' is just a convention. The below definition will work exactly the same.. Having said that it is very strong convention which should be followed always, but it does say something about flexible nature of the language

class poo:
    def bar(s):
            print ("hi")

p = poo()
p.bar()
print("Printed p.bar()")

#
#  Python allows function parameters to have default values
#  If the function is called without the argument, the parameter gets its default value.

# We needs to keep the following points in mind while calling functions: 

def func1(firstName = "First", lastName = "Last", grade = "grade"):
    print("func1: {} {} {}".format(firstName,lastName,grade))

# The passed keyword name should match with the actual parameter keyword name.

func1()
func1("John", "Smith", "freshman")
func1(lastName = "Majors", grade= "sophomore",
      firstName = "Lee")
func1("Ann","Taylor")

# In the case of calling a function using non-keyword arguments, order is important.

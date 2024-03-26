"Objectives"
"" '' # Understand the purpose of using kwargs and arguments
"" '' # Use kwargs and arguments


"" '' # Using  kwargs and Args
def kwargsArgsV1(*args, **kwargs):
    print(f"The args {args}")
    print(f"The kwargs {kwargs}")



def kwargsArgsV2(*args, **kwargs):
    userArgs = args
    userkwargs = kwargs
    return userArgs, userkwargs
  
    
kwargsArgsV1("Em","123 No Way","Coding","happy","gaming","Python","java", num1=1,num2=2,num3=3, num4=10)

returnedArgskwargs = kwargsArgsV2("Em", "123 No Way", "Coding","happy","gaming","Python","java",num1=1,num2=2,num3=3,num4=10)
print(f"Returned args and kwargs\n {returnedArgskwargs}\n")


theArgs = kwargsArgsV2(1,2,3,4,5)
print(theArgs[0])

theKwargs = kwargsArgsV2(num1 =1,num2=2,num3=3,num4=4,num5=5)
print(theKwargs[1])
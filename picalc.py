def calculate (intoperand, num1, num2) :
  if intoperand == "+" :
    return(num1+num2)
  elif intoperand == "-" :
    return(num1-num2)
  elif intoperand == "*" :
    return(num1*num2)
  elif intoperand == "/" :
    return(num1/num2)
    
n1 = 0
n2 = 0
op = ""

def go () :
  while True :
    n1 = input("Number 1 : ")
    n1 = int(n1)
    op = input("Operator : ")
    n2 = input("Number 2 : ")
    n2 = int(n2)
    print(calculate(op, n1, n2))

go()

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
    if n1 == "kill" : break
    n1 = int(n1)
    op = input("Operator : ")
    if op == "kill" : break
    n2 = input("Number 2 : ")
    if n2 == "kill" : break
    n2 = int(n2)
    print(calculate(op, n1, n2))

go()

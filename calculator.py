num1=int(input('enter num 1='))
num2=int(input('enter num 2='))
def calc(num1,num2):
    add=num1+num2
    diff=num1-num2
    mul=num1*num2
    div=num1//num2
    return add,diff,mul,div
a,b,c,d=calc(num1,num2)
print(a)
print(b)
print(c)
print(d)

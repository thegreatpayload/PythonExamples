#program cal perimeter of area of triangle by accepting base and height
a=float(input("Enter First side :"))
b=float(input("Enter Second side :"))
c=float(input("Enter Third side :"))
p=a+b+c
print("Perimeter Of First is={}".format(a))
print("Perimeter Of Second is={}".format(b))
print("Perimeter Of Third is={}".format(c))
print("Perimeter Of triangle is={}".format(p))
print("-"*30,"OR","-"*30)
#area of triangle by accepting base and height
base=float(input("Enter the base :"))
height=float(input("Enter the height :"))
area = base*height/2
print("base of triangle={}".format(base))
print("height of triangle={}".format(height))
print("area of triangle =%0.2f" %(area))
print("-"*30,"end","-"*30)


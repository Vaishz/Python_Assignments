# Area of circle

r=float(input("Enter the radius of the circle"))
area=3.14*r*r
print("Area of  circle with radius "r" is", area)



#Program to print extension
filename=input("Enter filename: ")
ext=filename.split(".")
extension=(ext[-1])

if (extension=="py"):
    print("The extension of the file is python")
elif (extension=="c"):
    print("The extension of the file is C")
elif (extension=="java"):
    print("The extension of the file is Java")
elif (extension=="cpp"):
    print("The extension of the file is C++")
elif (extension=="php"):
    print("The extension of the file is PHP")
elif (extension=="jpeg"):
    print("The extension of the file is JPEG")
elif (extension=="vb"):
    print("The extension of the file is Visual Basic")
elif (extension=="gif"):
    print("The extension of the file is gif")
else:
    print("Re-Enter")

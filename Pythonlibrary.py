class MultiFunctionAI():
    def Subfields():
        print("Sub-fields in AI are:")
        List1=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for subfield in List1:
            print(subfield)
            
    def OddEven():
        num=int(input("Enter a number: "))
        if(num%2==0):
            print(num,"is Even number")
        else:
            print(num,"is Odd number")
            
    def eligibleMrge():
        Age=input("Your Gender:")
        Age=int(input("Your Age:"))
        if(Age==21):
            print("ELIGIBLE")
        elif(Age==18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
            
    def percentage():
        s1=int(input("subject1= "))
        s2=int(input("subject2= "))
        s3=int(input("subject3= "))
        s4=int(input("subject4= "))
        s5=int(input("subject5= "))
        Total=s1+s2+s3+s4+s5
        print("Total : ",Total)
        print("Percentage : ",(Total/500)*100)
        
    def triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        print("Area formula:  (Height*Breadth/2)")
        print("Area of Triangle: ",(Height*Breadth/2))
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ",Height1+Height2+Breadth)    
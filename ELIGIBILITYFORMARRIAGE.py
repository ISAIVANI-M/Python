class EligibilityForMarriage():
    def eligible():
        gender=input("Enter your gender:")
        age=int(input("Enter your age:"))
        if(gender=="male"):
            if(age>=21):
                print("eligible")
                message="eligible"
            else:
                print("not eligible")
                message="eligible"
        elif(gender=="female"):
            if(age>=18):
                print("eligible")
                message="not eligible"
            else:
                print("not eligible")
                message=" not eligible"
        return message
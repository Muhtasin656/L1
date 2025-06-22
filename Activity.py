medical_cause=input("Do you have a medical cause Y or N")
attendance=int(input("what is your attendance"))
if medical_cause=="Y": 
    print("You are allowed")
else:
    if attendance>=75:
        print("you are allowed")
    else:
        print("you are not allowed")
    


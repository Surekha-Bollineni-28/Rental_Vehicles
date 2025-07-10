import time
"PONDICHERRY"
print("Welcome to pondicherry....!")
print("what do you want wanna rent??")
print("1.Two Wheeler\n 2. Four Wheeler")
rent = int(input())
def booking():
    amount = price * days
    print("Your Booking Details are as follows")
    print("--------------------------------")
    print("Vehicle :", vehicle)
    print("Amount per day :", price)
    print("Number of days :", days)
    print("Your Aadhar number is :", aadhar)
    print("Your Driving License Number is :", driving_license)
    print("Total amount :", amount)
    print("--------------------------------")
    print("Do you want to continue???")
    print("1.Yes\n 2. No")
    choice = int(input())
    if choice == 1:
        print("Congratulations...! \n Your Booking has been confirmed...!!!")
        print("Please pay at the time of pick-up by providing your documents")
        print("Enjoy the trip!!!")
    else:
        print("Your Booking has been cancelled!!!")
if rent == 1:
    print("1.Bike\n 2.scooty")
    two = int(input())
    if two == 1:
        print("Please select a Bike.....")
        print("1.MT\n 2. TVS")
        bike = int(input())
        print("How many days if you want Bike?")
        days = int(input())
        print("Enter your Aadhar Number")
        aadhar = int(input())
        print("Enter your driving license number")
        driving_license = int(input())

        if bike == 1 :
            price = 2100
            vehicle = "MT"
            booking()
        elif bike == 2:
            price = 1500
            vehicle = "TVS"
            booking()
        else:
            print("Please select valid option")
    elif two == 2:
        print("Please select a scooter.....")
        print("1.Vesapa 125\n 2.TVS")
        scooter = int(input())
        print("How many days if you want Bike?")
        days = int(input())
        print("Enter your Aadhar Number")
        aadhar = int(input())
        print("Enter your driving license number")
        driving_license = int(input())

        if scooter == 1:
            price = 800
            vehicle = "Vesapa 125"
            booking()
        elif scooter == 2:
            price = 600
            vehicle = "TVS"
            booking()
        else:
            print("Please select valid option")
    else:
        print("Please select valid option")
elif rent == 2:
    print("Select a car below")
    print("1.Tata punch\n 2.Tata nexon")
    car = int(input())
    print("How many days if you want Bike?")
    days = int(input())
    print("Enter your Aadhar Number")
    aadhar = int(input())
    print("Enter your driving license number")
    driving_license = int(input())

    if car == 1:
        price = 3000
        vehicle = "Tata punch"
        booking()
    elif car == 2:
        price = 2500
        vehicle = "Tata nexon"
        booking()
    else:
        print("Please select valid option")
else:
    print("Please select valid option")

rent=int(input("enter your flat/hostel rent ="))
food=int (input("enter the amount of food ordered ="))
electricity_spend=int(input("enter the total of electricity units spend ="))
charge_per_unit=float(input("enter the charge per unit ="))
persons=int(input("enter the number of persons living in flat/room ="))

total_electricity_bill=(electricity_spend*charge_per_unit)

output=(rent+food+total_electricity_bill)//persons

print ("amount for each person=",output)
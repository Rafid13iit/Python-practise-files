weight = input("Please input your weight : ")
weight_unit = input("(K)g or (L)bs : ")

if weight_unit.upper() ==  "K" :
    weight_in_lbs = float(weight) / .45
    print("Weight in Lbs : " + str(weight_in_lbs))

elif weight_unit.upper() == "L" :
    weight_in_kg = float(weight) * .45
    print("Weight in Kg : " + str(weight_in_kg))

else :
    print("You inputed wrong character!")
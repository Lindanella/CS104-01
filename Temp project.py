#CS104
#Linda Pimpinella
#conditions.py
temp = "xyz" 
x = temp
temp = input ("Please enter the current temperature:")
x = int (temp)
if x >= 90:
    print ("Wear Shorts")
elif x >= 70:
    print ("Short sleeves is fine")
elif x >= 50:
    print ("Wear a jacket")
elif x >= 32:
    print ("Wear a heavy jacket")
elif x < 32:
    print ("Stay inside")


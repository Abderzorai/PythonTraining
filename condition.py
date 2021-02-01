#Write a script that converts euros into dollars.
currency = str(input("choose the currency you want to convert 'E' for euro and '$' for Dollars"))
Amount = int(input("What is the amount you want to convert"))

if currency == 'E':
    print("you have {} € which in dollars equal {} $".format(Amount,(Amount*1.21)))
elif currency == '$':
    print("you have {} $ which in dollars equal {} €".format(Amount,(Amount*0.81)))
# Based on a Codeacademy python project

lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00

stylish_setee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15

sales_tax = 1.088
total = 0
itemization = []

while(True):
    request = input("How can I help? \n")
    if request == "buy":
        request = input("What would you like to buy? \n")
        if request == "loveseat":
            total += lovely_loveseat_price
            itemization.append(lovely_loveseat_description)
        elif request == "lamp":
            total += luxurious_lamp_price
            itemization.append(luxurious_lamp_description)
        elif request == "settee":
            total += stylish_settee_price
            itemization.append(luxurious_lamp_description)
    elif request == "checkout":
        break

total = total * sales_tax

print("Purchased Items:")
for x in itemization:
    print(x)
print(f"Total Price: ${total:.2f}")
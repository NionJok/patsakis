import string
rot13 = str.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
keimeno=input("Δώσε ένα κείμενο για να γίνει κρυπτογράφηση με το ROT13:")
print(keimeno.translate(rot13))

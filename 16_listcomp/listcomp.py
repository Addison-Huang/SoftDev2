'''
Team Zadical -- Addison Huang and Zane Wang
softDev2 pd 8
k16 -- do you even list?
2019 - 04 - 11
'''
UC="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LC="abcdefghijklmnopqrstuvwxyz"
nums="0123456789"
chars =".?!&#,;:-_*"

def passThresh(password):
    thresh = [0 if x in UC else 1 if x in LC else 2 if x in nums else 3 for x in password]
    return (0 in thresh and 1 in thresh and 2 in thresh)

print(passThresh("123"))
print(passThresh("loL"))
print(passThresh("lol1"))
print(passThresh("LOl1"))

def passStrength(password):
    thresh = [0 if x in UC else 1 if x in LC else 2 if x in nums else 3 if x in chars else 4 for x in password]
    strength = 0
    if (0 in thresh):
        strength += 3
    if (1 in thresh):
        strength += 2
    if (2 in thresh):
        strength += 2
    if (3 in thresh):
        strength += 3
    return strength

print(passStrength("123"))
print(passStrength("loL"))
print(passStrength("lol1"))
print(passStrength("LOl1"))
print(passStrength("LOl1#"))
    

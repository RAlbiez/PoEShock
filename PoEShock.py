
avgHit = int(input("Average Lightning Damage Hit: "))
critMulti = int(input("Critical Strike Multiplier (in %): "))
shockEffect = int(input("Shock Effect (in %): "))

shaperLife = 20000000
differenceToLast = 100
previousShock = 0

shockSteps = []

firstPass = True
while firstPass or differenceToLast > 1:
    firstPass = False

    nextShock = 0.5*(avgHit*critMulti/100/shaperLife)**0.4*(1+shockEffect/100)*(1+previousShock)

    shockSteps.append(nextShock)
    differenceToLast = abs((previousShock-nextShock)/nextShock)*100

    previousShock = nextShock

i = 1
for step in shockSteps:
    print("Hit Nr: " + str(i) + "\tShock: " + str(round(step*100,2)) + "%")
    i+=1

    
import random
pc= random.randint(10,20)
pl= 0
ppl=0
for p in range (pc):
    pesop =random.randint(100,2000)
    if pesop<800:
        pl+=1
    else:
        ppl+=1
print (f"La cantida de peces para enlatar es {pl} ")
print (f"La cnatidad de peces para la plancha es {ppl}")
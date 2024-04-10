
dist=float(input("digite uma distancia em metros..  "))
if dist < 0:
        print ("tente outro numero ")
else :
        km =(dist*1000)
        print("essa e sua distancia em km {}".format (km))
        cm =( dist / 100)
        print ("essa e sua distancia em cm {}".format(cm))

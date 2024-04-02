a, b = 0 , 1
n= int (input("digite seu numero :  "))
count = 0

if n<= 0:
        print ("digiteoutro numero pois esse e invalido :  ")
        
elif n ==1 :
    print ("esse e o resultado :  ",a, n ,".")

else :
     print ("essa e sua sequencia ")
     while count < n :
           print (a,end= " ")
           fib = a + b 
           a= b
           b = fib 
           count +=1

               

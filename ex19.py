def cheese_and_crackers(cheese_count, boxes_of_crackers):      #create a function and include two value
    print(f"You have {cheese_count} cheeses!")        
    print(f"You have {boxes_of_crackers} boxes of crackers!")       
    print("Man that's enough for a party!")        
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)                                      #print the number of cheese boxes and crackers


print("OR, we can use variables from our script:")    #assign the number of cheese and crackers as 10 and 50 by cheese_and_crackers
amount_of_cheese =10    
amount_of_crackers =50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")   
cheese_and_crackers(10+20,5+6)        #do a caulate in cheese_and_crackers


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese +100, amount_of_crackers+1000)  #do a caulate with amount of cheese and crackers
   # STRING FUNCTIONS  

# count 
     # it is find then word is whomany is  come 
 
# x="gwalior and morena"
# t=x.count("a")
# print(t)


# x="gwalior and morena"
# t=x.count("and",7)
# print(t)



  #endswith
   # return true if the string is end with the given substring otherwise return false

# x="jaipur"
# t=x.endswith("pur")
# print(t)

# x="jaipur"
# t=x.endswith("pura",5)
# print(t)

# x="malayalam"
# t=x.endswith("am",4)
# print(t)

  # endswith 
    
# k=["gwalior","bhopal","jaipur","indore","rampur"]
# for city in k:
#       if city.endswith("pur"):
#           print(city)


   
# k=["gwalior","bhopal","jaipur","indore","rampur"]
# for city in k:
#       if "io" in city or "do" in city:
#           print(city)


  #LJUST and rjust
# k="AGRA"
# j=k.ljust(10,"*")
# print(j)

# k="AGRA"
# j=k.rjust(20,"*")
# print(j)

# k=input("enter mobile number: ")
# # j=k[5:].rjust(10,"*")
# print(j)
  
  # center
# k="Harry"
# j=k.center(20,"*")  
# print(j)

  # strip
# k="     harry    "
# print(k)
# j=k.strip()
# print(j)

# k="-----harry-----"
# print(k)
# j=k.strip("-")
# print(j)


  # rstrip and lstrip
# k="-----harry-----"
# print(k)
# j=k.rstrip("-")
# print(j)


# k="-----harry-----"
# print(k)
# j=k.lstrip("-")
# print(j)


  #split
# k="mohit, harry, rahul, abhipal"
# print(k)
# t=k.split(",")
# print(t)

# k="mohit, harry, rahul, abhipal"
# print(k)
# t=k.split(",")
# print(t[3])

# k="mohit  harry rahul abhipal"
# print(k)
# t=k.split(" ",1)
# print(t)

  #rsplit
# k="mohit  harry rahul abhipal"
# print(k)
# t=k.rsplit(" ")
# print(t)


# k="mohit  harry rahul abhipal"
# print(k)
# t=k.rsplit(" ",1)
# print(t)


# rfind
# k="ram go to market"
# j=k.rfind("to")
# print(j)

  #partition
k="karan and arjun"
j=k.partition("and")
print(j)




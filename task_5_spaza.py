shopping_list = ["bread", "milk", "maputi", "coke", "sweets"]
print(shopping_list[0])
print(shopping_list[-1])

for item in shopping_list:
    print("Looking for:", item)
    
    if item == "coke": 
      print("Found coke stoping search")

    break
for item in shopping_list:
    
    if item == "sweets":
       print("Sweets are expensive")

       continue
    else:
       print("item sold")
  
"""This script calculates the financial and portion breakdowns for a braai event.
It culculates the total cost of meat, the cost distribution per guest, 
and determines any leftover meat after equal distribution among guests."""
meat_kg = 15.0                          
cost_per_kg = 86.0                               
number_of_guests = 10                       
is_vegan_included = False                         

#calculation Total cost of the meat by multiplying the cost per kg with the meat
TotalCost = meat_kg * cost_per_kg 
print("Total cost of the meat is R",TotalCost)

#Calculating the moneny each guest is supposed to pay by dividing the total cost by the number of Guests
CostPerGuest = TotalCost / number_of_guests
print("Each guest is supposed to pay R",CostPerGuest)

#caulculating the meat that will remain if each guest gets 1kg of meat
leftover_meat = meat_kg % number_of_guests
print(leftover_meat,"kg of meat is left" )

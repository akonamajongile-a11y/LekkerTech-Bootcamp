guest_age = 17
has_ticket = True
is_vip = False

if guest_age >= 18 and has_ticket == True:
    print("Welcome")
elif guest_age >= 18 and has_ticket == False:
    print("You need a ticket")
elif guest_age < 18 and is_vip is True: 
    print("VIP underage guest, please see the manager.")
else: 
    print("Access denied.")

    
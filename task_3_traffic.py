is_car_stopped = True
license_valid = True
speed_limit = 60
actual_speed = 50

if is_car_stopped == True:
    #print("Let them drive")
 #is_car_stopped:
    if license_valid == True:
        if actual_speed > speed_limit:
            print("Speeding fine issued!")
        else:
            print("Warning issued.")
    else:
        print("Arrested for driving without license")
else:
   print("Let them drive")
   

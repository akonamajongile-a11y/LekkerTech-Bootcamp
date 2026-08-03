battery_level = 100

while battery_level > 0:
    battery_level -= 15
    print(battery_level)

    if battery_level == 40:
        
        print("TikTok crashed, skipping this hour.")
   
    elif battery_level <= 10:
                  
        print("Phone died! Game over.")
        break
pass #add more apps later        
taxi_queue = ["Sandton", "Soweto", "Midrand", "Randburg", "CBD", "Alex"]

print("First taxi", taxi_queue[0])
print("Last taxi", taxi_queue[-1])


next_departures= taxi_queue[0:3]
print("The next 3 departing taxis", next_departures)

print("The last 2 Taxis", taxi_queue[-2:])

print("Every second taxi in the line", taxi_queue[::2])

taxi_queue[0] = "Bree Street"
print("Changed the 1st taxi in queue", taxi_queue)
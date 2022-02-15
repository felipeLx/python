# linear relationship

# model as description
    # range of y data, in miles
y_range = np.max(y) - np.min(y) = 300 - 0 = 300
6
    # range of x data, in hours
x_range = np.max(x) - np.min(x) = 6 - 0 = 6

    # estimating the speed
mph = y_range / x_range = 300 / 6 = 50

# model as prediction
    # model as python expression
miles = 50*hours

    # model predicts distance is 300 miles at 6 hours
time = 6
distance = 50 * time = 50 * 6 = 300

def model(time):
    return 50*time

predicted_distance = model(time=10)

# interpolation is a model prediction for points "in between" the times we actually measured
# extrapolation is a model prediction for a distance for a time outside the range of measured times

# Compute the total change in distance and change in time
total_distance = distances[-1] - distances[0]
total_time = times[-1] - times[0]

# Estimate the slope of the data from the ratio of the changes
average_speed = total_distance / total_time

# Predict the distance traveled for a time not measured
elapse_time = 2.5
distance_traveled = average_speed * elapse_time
print("The distance traveled is {}".format(distance_traveled))

# Select a time not measured.
time = 8

# Use the model to compute a predicted distance for that time.
distance = model(time)

# Inspect the value of the predicted distance traveled.
print(distance)

# Determine if you will make it without refueling.
answer = (distance <= 400)
print(answer)

# Complete the function to model the efficiency.
def efficiency_model(miles, gallons):
   return np.mean( miles / gallons )

# Use the function to estimate the efficiency for each car.
car1['mpg'] = efficiency_model(car1['miles'] , car1['gallons'] )
car2['mpg'] = efficiency_model(car2['miles'] , car2['gallons'] )

# Finish the logic statement to compare the car efficiencies.
if car1['mpg'] > car2['mpg'] :
    print('car1 is the best')
elif car1['mpg'] < car2['mpg'] :
    print('car2 is the best')
else:
    print('the cars have the same efficiency')
"""Prog to check if tank will overflow, underflow or be filled in finite time

Given tank with definite height and radius and flow of water available to fill the tank.
Need to find if tank will do one of the 3 above.

Approach is :

Volume of cyclindriacal tank is (22/7)*radius*radius*height . Given the flow rate, find the amount of time required
to completely fill the tank then compare it with the given time.If given time > required time, wil result in overflwo condition and if the 
given time is less than required time then uderflow results.Else the tank is filled"""

def volume(radius,height):
    return ((22/7)*radius*radius*height)

def findtimes(required_time, given_time):
    if required_time < given_time:
       print('Overflow')
    elif required_time > given_time:
       print('Underflow')
    else:
       print('filled')

# driver prog

radius = 5 # radius of tank

height = 10 # height of the tank

rate_of_flow = 10 # rate of flow of water

given_time = 70.0  # time given

# calculate the required time

required_time = volume(radius,height)/rate_of_flow

findtimes(required_time,given_time)

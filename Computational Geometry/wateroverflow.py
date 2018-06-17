""" Program to check if water tank overflows when solid spherical balls are immersed in the tank.

Given to you is the amount of water in the tank as well"""

def overflow(H,r,h,N,R):
    tank_cap = 3.14*r*r*H  # cyclinder capacity

    water_vol = 3.14*r*r*h  # vol of water in tank

    balls_vol = N*(4/3)*3.14*R*R*R  # vol of n balls

    vol = water_vol + balls_vol # volume of n balls

    if vol > tank_cap:
        print("Overflow")
    else:
        print("Not in overflow state")

# driver code

H = 10
r = 5
h = 5
N = 2
R = 2

overflow(H,r,h,N,R)


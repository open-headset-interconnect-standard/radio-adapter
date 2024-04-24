#!/usr/bin/python3
from math import sin, cos, radians

# Calculate the (X, Y) coordinates for the pins, relative to pin 8 at the center, given a radius.

def pinToX(pin: int) -> float:
    return(cos(pinToRadians(pin)) * radius)


def pinToY(pin: int) -> float:
    return(sin(pinToRadians(pin)) * radius)

def pinToRadians(pin: int) -> float:
    deg = -120 - (pin-1)*50
    return(radians(deg))


# Drawing says 8.5mm diameter.
radius = (8.5/2)

for pin in range(1, 8):
    print(F"Pin {pin}, X: {pinToX(pin):.3f}  Y: {pinToY(pin):.3f}")



from math import *

def cartToPol(real, img):
    tg = sqrt(real**2 + img**2) 
    arcTg = atan2(img, real)

    return tg, arcTg, degrees(arcTg)

def polToCart(arg, cpx):
    real = cpx * cos(radians(arg))
    img = cpx * sin(radians(arg))

    return real, img

def multComplexEq(z1Real, z1Img, z2Real, z2Img):
    z1 = complex(z1Real, z1Img)
    z2 = complex(z2Real, z2Img)

    return z1*z2

def divComplexEq(z1Real, z1Img, z2Real, z2Img):
    z1 = complex(z1Real, z1Img)
    z2 = complex(z2Real, z2Img)

    return z1/z2

def funcToUnicSinusoid(a, b):
    imgConv = b*-1
    c, theta, thetaDeg = cartToPol(a, imgConv)

    return c, theta, thetaDeg
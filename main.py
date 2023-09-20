from pdsiMath import *

resultQ1a = cartToPol(2, 3)
resultQ1b = cartToPol(-2, 1)

resultQ2 = polToCart(-135, 4)

resultQ3Mult = multComplexEq(3, 4, 2, 3)
resultQ3Div = divComplexEq(3, 4, 2, 3)

resultQ4 = funcToUnicSinusoid(-3, 4)

len = 50
print('='*len)
print('RESPOSTAS'.center(len))
print('='*len)
print(f'Q1.a. tg, arcTg, arcTgDg = [{resultQ1a[0]:.2f}; {resultQ1a[1]:.2f}; {resultQ1a[2]:.2f}]')
print(f'Q1.b. tg, arcTg, arcTgDg = [{resultQ1b[0]:.2f}; {resultQ1b[1]:.2f}; {resultQ1b[2]:.2f}]')
print('='*len)
print(f'Q2. real, img = [{resultQ2[0]:.2f}; {resultQ2[1]:.2f}]')
print('='*len)
print(f'Q3. z1*z2 = [{resultQ3Mult:.2f}] | z1/z2 = [{resultQ3Div:.2f}]')
print('='*len)
print(f'Q4. c, theta, thetaDg = [{resultQ4[0]:.2f}; {resultQ4[1]:.2f}; {resultQ4[2]:.2f}]')
print('='*len)
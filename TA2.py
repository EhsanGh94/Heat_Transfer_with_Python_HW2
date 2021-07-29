# Internal Flow & Constant Surface Heat Flux

from math import pi

while 7 > 2:

    D = float(input("\nD(m) = "))
    m_dot = float(input("m_dot(kg/s) = "))
    x = float(input("x(m) = "))
    mu = float(input("\xb5(N.s/m^2) = "))
    Pr = float(input("Pr = "))

    Re = (4 * m_dot)/(pi * D *mu)
    Re_cr = 2300
    x_lam = 0.05 * Re * Pr * D
    x_turb = 10 * D

    if Re <= Re_cr and x >= x_lam:
        Nu = 4.36
        print("\nRe = ", Re, "&", "Nu = ", Nu, "Laminar Flow & The Fully Developed region. ")

    elif Re > Re_cr and x >= x_turb:
        Nu = 0.02 * Re ** (4/5) * Pr ** (0.4)
        print("\nRe = ", Re, "&", "Nu = ", Nu, "Turbulent Flow & The Fully Developed region. ")

    elif Re <= Re_cr and x < x_lam:
        Nu = 0.08 * Re ** (4/5) * Pr ** (0.4)
        print("\nRe = ", Re, "&", "Nu = ", Nu, "Laminar Flow & The Entry region. ")

    elif Re > Re_cr and x < x_lam:
        Nu = 0.1 * Re ** (4/5) * Pr ** (0.4)
        print("\nRe = ", Re, "&", "Nu = ", Nu, "Turbulent Flow & The Entry region. ")

    con = input("Do you want to continue?? y/n ?? ")
    if con == "n":
        print("The End")
        break
    
    print("\n-------------------")

print("***********************")
print()


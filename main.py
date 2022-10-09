import numpy as np
import math as m
import position_functions as pf

if __name__ == "__main__":
    print("Deseja utilizar a aceleração da gravidade como: ")
    print("1) 10 m/s2\t 2) 9.8 m/s2\t 3) 9.78 m/s2")
    while True:
        option = input("Insira a opção desejada: ")
        if option == "1":
            g = 10; break
        elif option == "2":
            g = 9.8; break
        elif option == "3":
            g = 9.78; break
        else:
            print("Essa alternativa não é válida. Tente novamente.\n"); continue

    S0y = float(input("\nInsira a altura inicial do lançamento: "))
    Sfy = float(input("Insira a altura final do lançamento: "))

    print("\nSelecione a opção que apresente os dados conhecidos: ")
    print("1) Velocidade resultante e ângulo\t 2) Vx e Vy")
    while True:
        option = input("Insira a opção desejada: ")
        if option == "1":
            Vr = float(input("\nInsira a velocidade resultante do lançamento: "))
            a = float(input("Insira o ângulo de lançamento: "))
            Vx = Vr*(np.cos(np.deg2rad(a)))
            Vy = Vr*(np.sin(np.deg2rad(a)))
            break
        elif option == "2":
            Vx = float(input("\nInsira Vx do lançamento: "))
            Vy = float(input("Insira Vy do lançamento: "))
            Vr = m.sqrt((Vx**2) + (Vy**2))
            a = np.rad2deg(np.arctan([Vy/Vx]))
            break
        else:
            print("Essa alternativa não é válida. Tente novamente.\n"); continue

    t_hmax = Vy/g
    hmax = pf.svt2(S0y, Vy, t_hmax, g)

    t_total = pf.t_trajetoria(S0y, Sfy, Vy, g)
    distancia_total = pf.svt(0, Vx, t_total)

    print("\nAltura máxima %.2fm no instante t = %.2f" % (hmax, t_hmax))
    print("Distância total %.2fm no instante t = %.2f" % (distancia_total, t_total))
    print("V = %.2f\t Vx = %.2f\t Vy = %.2f\t â = %.2f\t" % (Vr, Vx, Vy, a))
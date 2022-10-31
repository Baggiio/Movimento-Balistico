import numpy as np
import math as m

def mod(Vx, Vy):
    return m.sqrt((Vx**2) + (Vy**2))

def velocidade(V0, g, t):
    return (V0 - (g*t))

def svt(S0, v, t):
    return (S0 + (v*t))

def svt2(S0, v, t, g):
    return (S0 + (v*t) - ((g*(t**2))/2))

def t_trajetoria(S0y, Sfy, Vy, g):
    a = g/2
    b = -(Vy)
    c = (Sfy - S0y)
    p = np.array([a, b, c])
    return np.roots(p)[0]

if __name__ == "__main__":

    # print("Deseja utilizar a aceleração da gravidade como: ")
    # print("1) 10 m/s2\t 2) 9.8 m/s2\t 3) 9.78 m/s2")
    # while True:
    #     option = input("Insira a opção desejada: ")
    #     if option == "1":
    #         g = 10; break
    #     elif option == "2":
    #         g = 9.8; break
    #     elif option == "3":
    #         g = 9.78; break
    #     else:
    #         print("Essa alternativa não é válida. Tente novamente.\n"); continue

    g = 9.8

    print("Deseja usar a velocidade com qual unidade de medida?")
    print("1) m/s\t 2) km/h\t 3) cm/s\t 4) km/s")
    while True:
        option = input("Insira a opção desejada: ")
        if option == "1":
            v_aux = 1; break
        elif option == "2":
            v_aux = 3.6; break
        elif option == "3":
            v_aux = 100; break
        elif option == "4":
            v_aux = 1000; break
        else:
            print("Essa alternativa não é válida. Tente novamente.\n"); continue

    print("\nSelecione a opção que apresente os dados conhecidos: ")
    print("1) Velocidade inicial e ângulo\t 2) Vx e Vy")
    while True:
        option = input("Insira a opção desejada: ")
        if option == "1":
            Vr = float(input("\nInsira a velocidade inicial do lançamento: "))/v_aux
            a = float(input("Insira o ângulo de lançamento: "))
            Vx = Vr*(np.cos(np.deg2rad(a)))
            Vy = Vr*(np.sin(np.deg2rad(a)))
            break
        elif option == "2":
            Vx = float(input("\nInsira Vx inicial do lançamento: "))/v_aux
            Vy = float(input("Insira Vy inicial do lançamento: "))/v_aux
            Vr = mod(Vx, Vy)
            a = np.rad2deg(np.arctan([Vy/Vx]))
            break
        else:
            print("Essa alternativa não é válida. Tente novamente.\n"); continue

    print("\nSelecione a opção que apresente os dados conhecidos: ")
    print("1) Altura inicial\t 2) Tempo de queda")
    while True:
        option = input("Insira a opção desejada: ")
        if option == "1":
            S0y = float(input("Insira a altura inicial do lançamento (em metros): "))
            break
        elif option == "2":
            t_queda = float(input("Insira o tempo de queda (em segundos): "))
            S0y = abs(svt2(0, 0, t_queda, g))
            break
        else:
            print("Essa alternativa não é válida. Tente novamente.\n"); continue
    # Sfy = float(input("Insira a altura final do lançamento (em metros): "))
    Sfy = 0

    print("\nDeseja calcular a trajetória em um instante de tempo específico?")
    print("1) Sim\t 2) Não")
    while True:
        option = input("Insira a opção desejada: ")
        if option == "1":
            td = float(input("Insira o instante Td (em segundos): "))
            distancia_td = svt(0, Vx, td)
            h_td = svt2(S0y, Vy, td, g)
            vy_td = velocidade(Vy, g, td)
            vmod_td = mod(Vx, vy_td)
            break
        elif option == "2":
            td = None
            break
        else:
            print("Essa alternativa não é válida. Tente novamente.\n"); continue

    t_hmax = Vy/g
    hmax = svt2(S0y, Vy, t_hmax, g)
    vy_hmax = velocidade(Vy, g, t_hmax)
    vmod_hmax = mod(Vx, vy_hmax)

    t_total = t_trajetoria(S0y, Sfy, Vy, g)
    distancia_total = svt(0, Vx, t_total)
    vy_ttotal = velocidade(Vy, g, t_total)
    vmod_ttotal = mod(Vx, vy_ttotal)

    # print("\nAltura máxima %.2fm no instante t = %.2f" % (hmax, t_hmax))
    # print("Distância total %.2fm no instante t = %.2f" % (distancia_total, t_total))
    # print("V = %.2f\t Vx = %.2f\t Vy = %.2f\t â = %.2f\t" % (Vr, Vx, Vy, a))

    print("\n============== RESPOSTAS: ==============\n")
    print("a) Calcule as componentes nos eixos x e y da velocidade inicial do objeto.")
    print("V0x = %.3f m/s;\t V0y = %.3f m/s\n" % (Vx, Vy))

    print("b) Calcule o tempo em que o objeto permanece no ar.")
    print("%.3f s\n" % (t_total))

    if td != None:
        print("c) Ache a posição do objeto no instante td = %.3f s." % (td))
        print("x = %.3f m;\t y = %.3f m\n" % (distancia_td, h_td))

        print("d) Calcule a velocidade e suas componentes nos eixos x e y no instante td = %.3f s." % (td))
        print("Vx = %.3f m/s;\t Vy = %.3f m/s;\t |v| = %.3f m/s\n" % (Vx, vy_td, vmod_td))
    
    print("e) Ache a altura máxima alcançada pelo objeto.")
    print("%.3f m\n" % (hmax))

    print("f) Ache o alcance horizontal — ou seja, a distância entre o ponto inicial e o ponto onde o objeto atinge o solo.")
    print("%.3f m\n" % (distancia_total))

    print("g) Calcule a velocidade do objeto imediatamente antes de alcançar o solo e suas componentes nos eixos x e y.")
    print("Vx = %.3f m/s;\t Vy = %.3f m/s;\t |v| = %.3f m/s\n" % (Vx, vy_ttotal, vmod_ttotal))

    print("h) Calcule a velocidade no instante em que o objeto atinge a altura máxima e suas componentes nos eixos x e y.")
    print("Vx = %.3f m/s;\t Vy = %.3f m/s;\t |v| = %.3f m/s\n" % (Vx, vy_hmax, vmod_hmax))

    input("Pressione qualquer tecla para sair...")
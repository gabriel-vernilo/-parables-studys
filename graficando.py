import matplotlib.pyplot as plt #para construir o gráfico na tela
import numpy # para cáculo da parábula

#pega os valores dados pelo usuario
a = float(input("digite o valor de a (acompanha x^2)\n"))
b = float(input("digite o valor de b (acompanha x)\n"))
c = float(input("digite o valor de c (não acompanha variável)\n"))

print("\033[1;93m" "RESPOSTAS :")
print('\033[1;97m' "-" * 20, )
print("\n")

#Equação do segundo grau para descobrir os pontos do gráfico
delta = (b**2 -4 * a * c) #calcula o delta
x1 = ((b * -1) + (delta**(1/2))) / (2*a) #calcula o x1, +
x2 = ((b * -1) - (delta**(1/2))) / (2*a) # calcula o x2, -
print("seu delta é {}".format(delta))# mostra qual seu delta
print("seu x1 é {}, e seu x2 é {}".format(x1, x2)) #mostra seu x1 e x2



def parabula(a,b,delta):

    #calula os vertices, ponto onde a parábula "vira", ponto máximo ou mínimo
    xv = (b*-1) / (2*a) #Calcula ponto x(horizontal) do vértice
    yv = (delta*-1) / (4*a) #calcula o ponto y (vertical) do vértice
    print("seu vértice de X é {}, e seu vértice de y é {}".format(xv,yv)) #mostra os vértices
    if a > 0:
        print("tem concavidade para cima,") #se a é positivo forma um "U"
        print(f"a imagem vai para infinito positivo, ou seja, é {yv};infinito+") #imagem é yv e algum infinito, nesse caso (a>0), para o positivo
        print(f"tem ponto mínimo, sendo ele, {xv}, {yv}") # o U tem seu vertice em baixo, minimo
    elif a < 0:
        print("tem concavidade para baixo") # U de cabeça para baixo
        print(f"a imagem vai para infinito negativo, sendo infinito negativo;{yv}")
        print(f"tem ponto máximo, sendo {xv};{yv}")
    else:
        print("NÃO É UMA EQUAÇÃO DE SEGUNDO GRAU")



    '''plt.title("Parábola") #define o titulo do gráfico
    plt.xlabel("X HORI") #define o nome da parte horizontal do gráfico
    plt.ylabel("Y Verti") #define o nome da parte vertical do gráfico
    plt.plot([x1,xv,x2], [0,yv,0]) #define a sequencia de pontos a ser ligado
    plt.show() #mostra o gráfico na tela'''

parabula(a,b,delta)
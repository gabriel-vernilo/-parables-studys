a = float(input("digite o valor de a\n"))
b = float(input("digite o valor de b\n"))
c = float(input("digite o valor  de c\n"))

def DeixaOTextoBonito():
    print("\033[1;93m" "RESPOSTAS :")
    print('\033[1;97m' "-" * 20, )

def Bhaskara(a,b,c):
    delta = (b**2 -4 * a * c)
    x1 = ((b*-1) + (delta**(1/2))) / (2*a)
    x2 = ((b*-1)-(delta**(1/2))) / (2*a)
    print(f"seu delta é {delta}")
    print(f"seu x1 é {x1} e seu x2 é {x2}")
    return delta

def CalculoParabola(a,b,c,delta):
    VerticeX = (b*-1) / (2*a)
    VerticeY = (delta * -1) / (4*a)
    print(f"Vertice de x = {VerticeX} , Vertice de y = {VerticeY}")
    if a > 0:
        print(f"concavidade para cima,\n",
              f"imagem {VerticeY};Infinito+\n",
              f"ponto mínimo = {VerticeX} ; {VerticeY}")
    elif a < 0:
        print(f"concavidade para baixo\n",
              f"imagem {VerticeY} ; Infinito-\n",
              f"ponto máximo {VerticeX} ; {VerticeY}")
    else:
        print("NÃO É EQUAÇÃO DE SEGUNDO GRAU")

formatacao = DeixaOTextoBonito()
Equacao2grau = Bhaskara(a,b,c)
Calculofinal = CalculoParabola(a,b,c,Equacao2grau)
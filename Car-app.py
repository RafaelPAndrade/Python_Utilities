#coding: utf-8

atualdeposito = int(input ("Litros agora?"))
consumoaos100 = float(input ("Consumo?"))
consumo = consumoaos100/100
distancia = float(input ("Distância da bomba de gasolina?"))


def Previsaoalcance ():
    alcance = ((atualdeposito)/consumo)-5

    return alcance

def Precofinal(price, distance):
    preçototal = ((price*((distance*consumo)+(vdeposito-atualdeposito)))*100//1)/100
    
    return preçototal




if Previsaoalcance() <= distancia:
    print("Pode não chegar à bomba de gasolina")


else:
    print ("É para atestar, certo?")
    preço = float(input ("Preço?"))
    vdeposito = int(input ("Volume do depósito?"))
    
    print ("Para encher, vai pagar", Precofinal(preço, distancia),"€")

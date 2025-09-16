nome=(input("qual seu nome:"))
peso=float(input("qual é seu peso"))
altura=float(input("qual é sua altura"))

imc=peso/(altura*altura)


if imc <=18.5:
    print(f"{nome}esta abaixo do peso {imc}")
elif imc <=24.9:
    print(f"{nome} esta com peso normal {imc}")
elif imc<=29.9:
    print(f"{nome} esta com sobrepeso {imc}")
elif imc <=34.9:
    print(f"{nome} esta com obeasidade grau I (imc)")
elif imc <=39.9:
    print(f"{nome} esta com obesidade grau II (imc)")
else:
    print(f"{nome} esta com obesidade grau III (mórbida) {imc}")

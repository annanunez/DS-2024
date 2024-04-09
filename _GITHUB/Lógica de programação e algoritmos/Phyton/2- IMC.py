altura = float(input('Digite a altura: '))

peso =  float(input('Digite seu peso: '))
IMC = peso / altura**2


print(f"O seu IMC é:  {round(IMC, 2)}")
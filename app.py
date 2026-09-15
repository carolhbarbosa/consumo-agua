# Sistema de Classificação de Consumo de Água

# Solicita os dados do usuário
tipo_imovel = input("Qual o tipo do imóvel? (comercial, casa ou apartamento): ").strip().lower()
consumo = float(input("Qual o consumo mensal de água em m³? "))

# Classifica o consumo de acordo com as regras de negócio
if tipo_imovel == "comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")
elif tipo_imovel == "apartamento" and consumo < 10:
    print("Consumo econômico – excelente controle de água!")
elif (tipo_imovel == "apartamento" or tipo_imovel == "casa") and consumo <= 25:
    print("Consumo moderado – dentro do padrão residencial.")
else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
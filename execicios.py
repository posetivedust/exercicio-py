salario = input("coloque um salario:")

salario = float(salario)
    
if salario <= 280:
    print("o salario anterior é:",salario)
    aumento = salario * (20 / 100) 
    print("o aumento é de:",aumento)
    total = salario + aumento 
    print("o salario total é",total)
if salario <= 700:
    print("o salario anterior é:",salario)
    aumento = salario * (15 / 100) 
    print("o aumento é de:",aumento)
    total = salario + aumento 
    print("o salario total é",total)
if salario <= 1500:
    print("o salario anterior é:",salario)
    aumento = salario * (10 / 100) 
    print("o aumento é de:",aumento)
    total = salario + aumento 
    print("o salario total é",total)
if salario > 1500:
    print("o salario anterior é:",salario)
    aumento = salario * ( 5 / 100) 
    print("o aumento é de:",aumento)
    total = salario + aumento 
    print("o salario total é",total)
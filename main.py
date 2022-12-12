from random import randint

cpf = ''.join([str(randint(0, 9)) for _ in range(9)])

for i in range(2):
    digit = 0
    for idx, value in enumerate(cpf[:9 + i][::-1], start=2):
        digit += idx * int(value)
    digit = (digit * 10) % 11; 
    digit = 0 if digit > 9 else digit
    cpf += str(digit)    
    
print(f'CPF gerado: {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}')
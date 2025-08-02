import re
import sys

entrada = input("Digite o seu cpf...: ")
cpf_usuario = re.sub(r'[^0-9]', '', entrada)
entrada_e_sequencial = cpf_usuario == cpf_usuario[0] * len(cpf_usuario)


if entrada_e_sequencial:
    print('Dados sequencias identificados...')
    sys.exit()

nove_digitos_cpf = cpf_usuario[:9]
contador_regressivo_1 = 10
contador_regressivo_2 = 11
resultado = 0
resultado_2 = 0

for digitos in nove_digitos_cpf:
    resultado += int(digitos) * contador_regressivo_1
    contador_regressivo_1 -= 1

primeiro_digito = (resultado * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

dez_digitos = nove_digitos_cpf + str(primeiro_digito)

for digitos in dez_digitos: 
    resultado_2 += int(digitos) * contador_regressivo_2
    contador_regressivo_2 -= 1

segundo_digito = (resultado_2 * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

cpf_gerado = f'{nove_digitos_cpf}{primeiro_digito}{segundo_digito}'
print(cpf_gerado)

if cpf_gerado == cpf_usuario:
    print('CPF VÁLIDO')
else:
    print('inválido')

    
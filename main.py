# Programa para verificar se um CPF é válido

"""
Como verificar se um CPF é válido:
- A verificação é feita em 2 etapas e se baseio nos 2 últimos dígitos de um CPF
- Utilizando "529.982.247-25" como base, a verificação deve ser feita utilizando o "25" que vem depois do hífen


***** Regra para validar o primeiro dígito:
Tendo como base o CPF "529.982.247-25"
1- Multiplica-se os 9 primeiros dígitos pela sequência decrescente de 10 a 2, somando os resultados:
5*10 + 2*9 + 9*8 + 9*7 + 8*6 + 2*5 + 2*4 + 4*3 + 7*2 = 295

2- Multiplica-se o resultado por 10 e depois se faz uma divisão inteira com ele por 11:
    - Se o resto da divisão inteira for igual ao primeiro dígito verificador, a primeira parte da validação
    está correta. Caso o resto da divisão seja igual a 10, deve-se considerar == 0.

(295 * 10) // 11:
    - Resultado = 268
    - Resto = 2
    - Como o resto é igual ao primeiro dígito verificador, ou seja, o primeiro dígito depois do hífen, sabemos que
    esse CPF passou no primeiro teste.


***** Regra para validar o segundo dígito:
1- Mesma coisa que o passo anterior, porém, aqui se considera o dígito verificador. Ordem de 11 a 2.
5*11 + 2*10 + 9*9 + 9*8 + 8*7 + 2*6 + 2*5 + 4*4 + 7*3 + 2*2 = 347

2- Mesma coisa que no anterior:
(347 * 10) // 11:
    - Resultado = 315
    - Resto = 5
    - Como o resto é igual ao segundo dígito verificador, ou seja, o segundo dígito depois do hífen, sabemos que esse
    CPF passou no segundo teste e que ele é um CPF real.

"""


def clean_number(number_to_clean: str) -> str:
    items_removed: str = """ ,.+-=()_;:|\\/´`~^[]{}*&¨%$#@!?'"><
    AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzÇç"""
    cleaned_number: str = number_to_clean
    for x in range(len(items_removed)):
        cleaned_number = cleaned_number.replace(items_removed[x], '')
    return cleaned_number


def teste1(lista: list, verificador: int) -> bool:
    teste: int = 0
    for x in range(len(lista)):
        teste += int(lista[x]) * (x + 2)
    if (teste * 10) % 11 != verificador:
        return False
    else:
        return True


def teste2(lista: list, verificador1: int, verificador2: int) -> bool:
    teste: int = 0
    for x in range(len(lista)):
        teste += int(lista[x]) * (x + 3)
    teste += verificador1 * 2
    if (teste * 10) % 11 != verificador2:
        return False
    else:
        return True


def teste3(lista: list, verificador1: int, verificador2: int) -> bool:
    if teste1(lista=lista, verificador=verificador1):
        if teste2(lista=lista, verificador1=verificador1, verificador2=verificador2):
            return True
        else:
            return False
    else:
        return False


def main(value: str) -> bool:
    value = clean_number(value)
    cpf_lista: list[int] = []
    for x in range(len(value)):
        cpf_lista.append(int(value[x]))
    cpf_lista.reverse()
    verificador1: int = int(cpf_lista[1])
    verificador2: int = int(cpf_lista[0])

    cpf_lista.pop(0)
    cpf_lista.pop(0)

    if teste3(lista=cpf_lista, verificador1=verificador1, verificador2=verificador2):
        return True
    else:
        return False


if __name__ == "__main__":
    inputted_cpf = str(input("Digite um CPF: "))
    if main(value=inputted_cpf):
        print("CPF válido.")
    else:
        print("CPF inválido")

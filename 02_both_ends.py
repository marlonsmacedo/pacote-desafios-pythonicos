"""
02. both_ends

Dada uma string s, retorne uma string feita com os dois primeiros
e os dois ultimos caracteres da string original.
Exemplo: 'spring' retorna 'spng'. Entretanto, se o tamanho da string
for menor que 2, retorne uma string vazia.
"""


def both_ends(s):  # Solução Github --> @marlonsmacedo
    """ 
    02. both_ends
    Dada uma string s, retorne uma string feita com os dois primeiros
    e os dois ultimos caracteres da string original.
    Exemplo: 'spring' retorna 'spng'. Entretanto,
    se o tamanho da string for menor que 2, retorne uma string vazia.
    """

    # Solução 1 - one line
    # s = s[:2] + s[len(s)-2:] if len(s) > 2 else ''

    # Solução 2
    i = 0
    word = ''
    while i < len(s):
        if i <= 2 or i >= len(s)-2:
            word += ''.join(s[i])
            i += 1
            print(i)
        else:
            print('')

    return word


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(both_ends, 'spring', 'spng')
    test(both_ends, 'Hello', 'Helo')
    test(both_ends, 'a', '')
    test(both_ends, 'xyz', 'xyyz')

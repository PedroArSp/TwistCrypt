#! python39
from twist_crypt import TwistEncrypt
def gcd(p,q):
# Create the gcd of two positive integers.
    while q != 0:
      p, q = q, p%q
    return p
def is_coprime(x, y):
    return gcd(x, y) == 1


def main():
    bExit = False
    op = int(input('0 Encriptar / 1 Desencriptar:[default 0]') or '0')

    while not bExit:
        keytext = input(f'Key (deve ser primo com {TwistEncrypt.KEYORDER}):')
        if keytext.isdigit():
            key = int(keytext)
            bExit = is_coprime(key,TwistEncrypt.KEYORDER)
            if not bExit:
                print(f'{key} não é co-primo com {TwistEncrypt.KEYORDER}')
        else:
            print(f'Erro - {keytext} não é um numero')
    twist = TwistEncrypt(key)



    inTexto = input('Texto:')
    if op == 0: #Encriptar
        textoCifrado = twist.encriptar(inTexto)
        print('texto cifrado:',textoCifrado)
    else:
        textoPlano = twist.desencriptar(inTexto)
        print('texto decifrado:',textoPlano)


if __name__ == '__main__':
    #help(TwistEncrypt)
    main()
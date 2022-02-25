# TwistCrypt
A quick application for Twist Cryptography

## Using
```
from twist_crypt import TwistEncrypt
twist = TwistEncrypt(key = 15)
crypt = twist.encriptar('esta_e_uma_prova')
decrypt = twist.desencriptar(crypt)
print(crypt,decrypt)

```
## Help
```
 help(twist_crypt.TwistEncrypt) 
Help on class TwistEncrypt in module twist_crypt:

class TwistEncrypt(builtins.object)
 |  TwistEncrypt(Key=1) -> None
 |
 |  TwistEncrypt
 |  Classe para implementar criptografia Twist
 |  Baseado em um trabalho pedido em cursos da USP pelo Departamento de Ciência da
 |  Computação (DCC)
 |  Methods defined here:
 |
 |  __init__(self, Key=1) -> None
 |      Args:
 |      Key (int, optional): chave, preferente primo com KEYORDER. Defaults to 1.
 |
 |  desencriptar(self, inTexto: str) -> str
 |      _desencriptar_
 |
 |      Args:
 |          inTexto (str): texto a descriptografar
 |
 |      Returns:
 |          str: _texto desencriptado_
 |
 |  encriptar(self, inTexto: str) -> str
 |      _encriptar_
 |
 |      Args:
 |          inTexto (str): Texto a criptografar
 |
 |      Returns:
 |          str: _texto encriptado_
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  KEYORDER = 28
 ```

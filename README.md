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
 
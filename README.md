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
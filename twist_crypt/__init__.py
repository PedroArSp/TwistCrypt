#! python39
class TwistEncrypt:
    """TwistEncrypt
        Classe para implementar criptografia Twist 
        Baseado em um trabalho pedido em cursos da USP pelo Departamento de Ciência da
        Computação (DCC)

    """
    _transCodigo =['_']+ list([chr(i) for i in range(ord('a'),ord('z')+1)])+['.']
    _nTransCodigo = len(_transCodigo)
    KEYORDER = _nTransCodigo

    def __init__(self,Key=1) -> None:
        """_summary_

        Args:
            Key (int, optional): chave, preferente primo com KEYORDER. Defaults to 1.
        """
        self.key = Key

        
    def _getTranscodigo(self,letra:str)->int:
        if isinstance(letra,str) and len(letra)==1 and letra in self._transCodigo:
            return self._transCodigo.index(letra)
        else:
            return 0

    def encriptar(self,inTexto:str)->str:
        codigoPlano = [self._getTranscodigo(letra) for letra in inTexto]
        cifraCodigo=[]
        ln = len(codigoPlano)
        for i in range(ln):
            cifraCodigo.append((codigoPlano[(self.key * i)% ln]-i) % self._nTransCodigo)
        textoCifrado=''.join([self._transCodigo[i] for i in cifraCodigo])   
        return textoCifrado

    def desencriptar(self,inTexto:str)->str:
        cifraCodigo = [self._getTranscodigo(letra) for letra in inTexto]
        ln = len(cifraCodigo)
        codigoPlano = [0] * ln
        for i in range(ln):
            codigoPlano[(self.key * i)%ln] = (cifraCodigo[i]+i) % self._nTransCodigo
        textoPlano = ''.join(self._transCodigo[i] for i in codigoPlano)
        return textoPlano



class Entero:
    nombre=""
    desc=""
    codigo=0
    def __init__(self, codigo):
        self.codigo=codigo

    
    def obtenerdato(self):
        return self.codigo

    def igualQue(self, op2):
        n2=Entero(None)
        n2 = op2
        return self.codigo==n2.codigo

    def menorQue(self, op2):
        n2=Entero(None)
        n2 = op2
        return self.codigo<n2.codigo 
    
    def menorIgualQue(self, op2):
        n2=Entero(None)
        n2 = op2
        return self.codigo<=n2.codigo     

    def mayorQue(self, op2):
        n2=Entero(None)
        n2 = op2
        return self.codigo>n2.codigo     
        
    def mayorIgualQue(self, op2):
        n2=Entero(None)
        n2 = op2
        return self.codigo>=n2.codigo  
    
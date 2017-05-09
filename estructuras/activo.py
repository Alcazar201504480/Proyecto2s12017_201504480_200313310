class activo:
    nombre=""
    desc=""
    codigo=""
    def __init__(self, nombre, desc, codigo):
        self.nombre=nombre
        self.desc=desc
        self.codigo=codigo
        
    def obtenerdato(self):
        return self.codigo

    def obtenernombre(self):
        return self.nombre

    def obtenerdesc(self):
    	return self.desc

    def igualQue(self, op2):
        n2=activo(None,None, None)
        n2 = op2
        return self.codigo==n2.codigo

    def menorQue(self, op2):
        n2=activo(None,None, None)
        n2 = op2
        return self.codigo<n2.codigo 
    
    def menorIgualQue(self, op2):
        n2=activo(None,None, None)
        n2 = op2
        return self.codigo<=n2.codigo     

    def mayorQue(self, op2):
        n2=activo(None,None, None)
        n2 = op2
        return self.codigo>n2.codigo     
        
    def mayorIgualQue(self, op2):
        n2=activo(None,None, None)
        n2 = op2
        return self.codigo>=n2.codigo  
    
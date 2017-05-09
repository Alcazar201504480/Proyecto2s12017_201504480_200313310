class HashTable(object):
    def __init__(self):
        self.size = 100
        self.map = [None]*self.size
        self.DOT = []

    def _get_hash(self, key):
        hashValue = 0
        mitad = ""
        digito1 = None
        digito2 = None
        final = ""
        for char in str(key):
            hashValue += ord(char)
        hashValue = hashValue * hashValue
        mitad = str(hashValue)
        digito1 = mitad[int(len(mitad)/2) -1]
        digito2 = mitad[int(len(mitad)/2) ]
        final = digito1 + digito2
        return(int(final))


    def add(self, key, value):
        key_Hash = self._get_hash(key)
        key_Value = [key,value]
        if self.map[key_Hash] is None:
            self.map[key_Hash] = list([key_Value])
            return True
        else:
            for pair in self.map[key_Hash]:
                if pair[0] == key:
                    pair[1] == value
                    return True
            self.map[key_Hash].append(key_Value)
            return True

    def get(self, key):
        key_Hash = self._get_hash(key)
        if self.map[key_Hash] is not None:
            for pair in self.map[key_Hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    def delete(self, key):
        key_Hash = self._get_hash(key)
        if self.map[key_Hash] is None:
            return False
        for i in range(0,len(self.map[key_Hash])):
            if self.map[key_Hash][i][0] == key:
                self.map[key_Hash].pop(i)
                return True

    def display(self):
        index = []
        i = 0
        for value in self.map:
            if value is not None:
                index += [str(self.map.index(value))]
                for value1 in value:
                    self.DOT += ["\""+str(self.map.index(value))+"\"" + "->" + "\""+value1[0]+"-"+value1[1]+"\""]
        while i<len(index)-1:
            self.DOT+= ["\""+index[i]+"\"" + "->" + "\""+index[i+1]+"\""]
            i += 1


    def dot(self):
        self.display()
        archivo = open("tablaHash.txt", "w")
        archivo.write('digraph tablaHash\n')
        archivo.write('{\n')
        archivo.write("rankdir=TB\n")
        for value in self.DOT:
            archivo.write(value+';\n')
        archivo.write('}\n')
        archivo.close()
    def graficar(self):
          check_output('"C:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe" -Tjpg datosm.txt -o "'+os.getcwd()+'\\tablaHash.txt"', shell=True)         


    def show(self):
        print("********************************************")
        for item in self.map:
            if item is not None:
                print(str(item))

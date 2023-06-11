class Nodo:
    def __init__(self, valor):
        self.id = 0
        self.valor = valor
        self.listaH = []
        
    def agregarHijo(self, hijo):
        self.listaH.append(hijo)
    
    def graphviz(self, nodo, c):
        contador = 0
        dot = ""
        if isinstance(nodo, Nodo):
            dot = "nodo"+str(c)+"[label=\""+str(nodo.valor)+"\"];\n"
        else:
            dot = "nodo"+str(c)+"[label=\""+str(nodo)+"\"];\n"
            return dot

        for hijo in range(len(nodo.listaH)):
            temp = hijo+1
            dot += "nodo"+str(c)+" -> nodo"+str(c)+str(contador)+str(temp)+";\n"
            dot += self.graphviz(nodo.listaH[hijo], str(c)+str(contador)+str(temp))
            temp += 1
            contador+=1
        return dot
    
    def instArbol(self):
        dot = self.graphviz(self, 0)
        return dot

    
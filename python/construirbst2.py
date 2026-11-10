class Nodo:
    def _init_(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None



def insertar(raiz: Nodo, valor):
    nuevo = Nodo(valor)
    if raiz is None:
        return nuevo

    n = raiz

    while True:
        if valor < n.valor:
            if n.izq is None:
                n.izq = nuevo
                break
            n = n.izq
        elif valor > n.valor:
            if n.der is None:
                n.der = nuevo
                break
            n = n.der

    return raiz

def construir(valores: list[int]):
    raiz = None
    for v in valores:
        raiz = insertar(raiz,v)
    return raiz


def kmenores(raiz:Nodo , k: int):
    res = []
    pila = []
    n = raiz

    while (n or pila is not None) and len(res) < k :
        while n is not None:
            pila.append(n)
            n = n.izq
        n = pila.pop()
        res.append(n.valor)
        n = n.der

    return res






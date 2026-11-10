# Coste de insertar una clave: O(h), h = altura del arbol
#   - equilibrado: O(log n)      - peor caso (claves ordenadas): O(n)
# Coste de construir con n claves: O(n log n) caso medio, O(n^2) peor caso
# Coste del recorrido (preorden): O(n)
import sys


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None


def insertar(raiz, valor):
    # Iterativo (equivalente a insertarEn de la teoria) para no pasarse
    # del limite de recursion de Python con casos grandes.
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
        else:
            break  # repetido: no se inserta
    return raiz


def construir(valores):
    raiz = None
    for v in valores:
        raiz = insertar(raiz, v)
    return raiz


def preorden(raiz):
    # Iterativo con pila: O(n)
    res = []
    pila = [raiz] if raiz else []
    while pila:
        n = pila.pop()
        res.append(n.valor)
        if n.der:
            pila.append(n.der)  # se mete antes el derecho para sacar antes el izquierdo
        if n.izq:
            pila.append(n.izq)
    return res


# ---------------------------------------------------------------------------
# Ejercicio 2: kmenores
# Coste: O(h + k), h = altura del arbol
#   - bajar por la izquierda hasta el minimo: O(h)
#   - sacar k nodos de la pila (inorden iterativo, parando en k): O(k) amortizado
# Peor caso (arbol degenerado): O(n). Memoria extra: la pila, O(h).
# ---------------------------------------------------------------------------
def kmenores(raiz, k):
    # Inorden iterativo con pila: en un BST sale ORDENADO, asi que los k
    # primeros que se visitan son los k menores. Se para al llegar a k.
    res = []
    pila = []
    n = raiz
    while (pila or n is not None) and len(res) < k:
        while n is not None:      # bajar todo a la izquierda
            pila.append(n)
            n = n.izq
        n = pila.pop()            # el menor que queda por visitar
        res.append(n.valor)
        n = n.der                 # despues, su subarbol derecho
    return res


def main_kmenores():
    # Formato SUPUESTO (cambiar segun el enunciado):
    #   T
    #   n k
    #   v1 ... vn   <- el arbol dado en PREORDEN
    # Insertar un preorden en un BST vacio reconstruye exactamente ese arbol.
    datos = sys.stdin.buffer.read().split()
    pos = 0
    t = int(datos[pos]); pos += 1
    salida = []
    for _ in range(t):
        n = int(datos[pos]); k = int(datos[pos + 1]); pos += 2
        valores = [int(x) for x in datos[pos:pos + n]]
        pos += n
        raiz = construir(valores)
        salida.append(" ".join(map(str, kmenores(raiz, k))))
    sys.stdout.write("\n".join(salida) + "\n")


def main():
    datos = sys.stdin.buffer.read().split()
    pos = 0
    t = int(datos[pos]); pos += 1
    salida = []
    for _ in range(t):
        n = int(datos[pos]); pos += 1
        valores = [int(x) for x in datos[pos:pos + n]]
        pos += n
        raiz = construir(valores)
        salida.append(" ".join(map(str, preorden(raiz))))
    sys.stdout.write("\n".join(salida) + "\n")


if __name__ == "__main__":
    # python3 construirbst.py           -> ejercicio 1 (construirbst)
    # python3 construirbst.py kmenores  -> ejercicio 2 (kmenores)
    if len(sys.argv) > 1 and sys.argv[1] == "kmenores":
        main_kmenores()
    else:
        main()

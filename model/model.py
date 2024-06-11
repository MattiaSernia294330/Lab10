import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo =nx.Graph()
        self._dizionarioNazioni={}
        self._fillDizionario()

    def _fillDizionario(self):
        self._dizionarioNazioni = {}
        lista=DAO.getAllNazioni()
        for nazione in lista:
            self._dizionarioNazioni[nazione.CCode]=nazione
    def creaGrafo(self,anno):
        listaConnessioni=DAO.getConnessioni(anno)
        self._grafo.clear()
        for element in listaConnessioni:
            self._grafo.add_node(self._dizionarioNazioni[element.state1no])
            self._grafo.add_node(self._dizionarioNazioni[element.state2no])
        for element in listaConnessioni:
            if element.conttype==1:
                self._grafo.add_edge(self._dizionarioNazioni[element.state1no],self._dizionarioNazioni[element.state2no])

    def getinfoNodi(self):
        dizio={}
        for nodes in self._grafo.nodes():
            dizio[nodes]=self._grafo.degree(nodes)
        return dizio

    def componenti_connesse(self):
        return nx.number_connected_components(self._grafo)

    def getBFSnodes(self, source):
        edges = nx.bfs_edges(self._grafo, source)
        visited = []
        for u, v in edges:
            visited.append(v)
        return visited






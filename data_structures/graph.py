# Adjacency-list-based implementation
class ALDirectedGraph(object):
    """ Adjacency list-based directed graph. """
    def __init__(self):
        self.adj = {}

    def itervertices(self):
        """ Iterate through all vertices. """
        return self.adj.keys()

    def add_vertex(self, u):
        """ Add a vertex to the graph.
        Input:
            u: vertex's value
        """
        if u not in self.adj:
            self.adj[u] = set()

    def remove_vertex(self, u):
        """ Remove vertex from the graph.
        IMPORTANT: remove all edges associated with u before removing it.
        Input:
            u: vertex's value
        """
        del self.adj[u]

    def add_edge(self, u, v):
        """ Add an edge from u to v to the graph.
        Inputs:
            u: source vertex's value.
            v: destination vertex's value.
        """
        if u not in self.adj:
            self.add_vertex(u)
        if v not in self.adj:
            self.add_vertex(v)
        self.adj[u].add(v)


    def remove_edge(self, u, v):
        """ Remove edge from u to v from the graph.
        Inputs:
            u: source vertex's value.
            v: destination vertex's value.
        """
        self.adj[u].remove(v)

    def neighbors(self, u):
        """ Get all neighbors of a vertex.
        Input:
            u: vertex's value.
        """
        return self.adj[u]

class UndirectedGraphMixin(object):
    """ Mixin class used to create undirected version of graphs."""
    def remove_vertex(self, u):
        """ Remove vertex from graph.
        Input:
            u: vertex's value.
        """
        for v in self.neighbors(u):
            self.remove_edge(v, u)
        super(UndirectedGraphMixin, self).remove_vertex(u)
    
    def add_edge(self, u, v):
        """ Add undirected edge connecting u and v to the graph.
        Inputs:
            u: a vertex's value.
            v: remaining vertex's value.
        """
        super(UndirectedGraphMixin, self).add_edge(u, v)
        super(UndirectedGraphMixin, self).add_edge(v, u)

    def remove_edge(self, u, v):
        """ Remove undirected edge connecting u and v from the graph.
        Inputs:
            u: a vertex's value.
            v: remaining vertex's value.
        """
        super(UndirectedGraphMixin, self).remove_vertex(u, v)
        super(UndirectedGraphMixin, self).remove_vertex(v, u)

class ALUndirectedGraph(UndirectedGraphMixin, ALDirectedGraph):
    """ Adjacency list-based undirected graph. """
    pass

# Object Oriented adjacency list
class OOALVertex(object):
    """ Vertex object used for adjacency-list-based graph. """
    def __init__(self):
        self.neighbors = set()

class OOALDirectedGraph(object):
    """ Directed graph with object-oriented adjacency list implementation. """
    def __init__(self):
        self.vertices = set()

    def itervertices(self):
        """ Iterate through all vertices. """
        return iter(self.vertices)

    def add_vertex(self, u):
        """ Add a vertex to the graph.
        Input:
            u: an OOALVertex object
        """
        if u not in self.vertices:
            self.vertices.add(u)

    def remove_vertex(self, u):
        """ Remove a vertex from the graph.
        Input:
            u: an OOALVertex object.
        """
        self.vertices.remove(u)

    def add_edge(self, u, v):
        """ Add edge from u to v to the graph.
        Inputs:
            u, v: OOALVertex objects
        """
        if u not in self.vertices:
            self.add_vertex(u)
        if v not in self.vertices:
            self.add_vertex(v)
        u.neighbors.add(v)

    def remove_edge(self, u, v):
        """ Remove edge from u to v from the graph.
        Inputs:
            u, v: OOALVertex objects.
        """
        u.neighbors.remove(v)

    def neighbors(self, u):
        """ Get all neighbors of a vertex.
        Input:
            u: an OOALVertex object
        """
        return u.neighbors

class OOALUndirectedGraph(UndirectedGraphMixin, OOALDirectedGraph):
    """ Undirected graph with object-oriented adjacency list implementation. """
    pass


# Object Oriented incidence list
class OOILVertex(object):
    """ Vertex object for object-oriented incidence list-based graph."""
    def __init__(self):
        self.edges = set()

class OOILEdge(object):
    """ Edge object for object-oriented incidence list-based graph."""
    def __init__(self, a, b):
        """ Inputs:
            a, b: vertices' values.
        """
        self.a = a
        self.b = b

    def other_end(self, a_or_b):
        """ Return the other end of the edge.
        Input:
            a_or_b: edge.a or edge.b
        """
        if self.a is a_or_b:
            return self.b
        else:
            return self.a
            
    def as_tuple(self):
        """ Get the tuple form of edge. """
        return (self.a, self.b)

class OOILDirectedGraph(object):
    """ Directed Graph with object-oriented incidence list-based implementation. """
    Vertex = OOILVertex
    Edge = OOILEdge
    def __init__(self):
        self.vertices = set()

    def itervertices(self):
        """ Iterate through all vertices. """
        return iter(self.vertices)

    def add_vertex(self, u):
        """ Add a vertex to the graph.
        Input:
            u: OOILVertex object.
        """
        if u not in self.vertices:
            self.vertices.add(u)

    def remove_vertex(self, u):
        """ Remove a vertex from the graph.
        Input:
            u: OOILVertex object.
        """
        self.vertices.remove(u)

    def add_edge(self, u, v=None):
        """ Add an edge to the graph.
        Inputs:
            - if v != None:
                u, v: OOILVertex objects
            - if v == None:
                u: OOILEdge object
        """
        if v is None:
            edge = u
            u, v = edge.a, edge.b
        else:
            edge = self.Edge(u, v)
        u.edges.add(edge)
        if u not in self.vertices:
            self.add_vertex(u)
        if v not in self.vertices:
            self.add_vertex(v)
    
    def remove_edge(self, u, v=None):
        """ Remove an edge from the graph.
        Inputs:
            - if v != None:
                u, v: OOILVertex objects
            - if v == None:
                u: OOILEdge object
        """
        if v is None:
            edge = u
        else:
            edge = self.Edge(u, v)
        u.edges.remove(edge)

    def neighbors(self, u):
        """ Return a vertex's neighbors.
        Input:
            u: OOILVertex object
        """
        return (edge.other_end(u) for edge in u.edges)

    def indicent_edges(self, u):
        """ Return all outgoing edges from vertex u.
        Input:
            u: OOILVertex object
        """
        return u.edges

class OOILUndirectedEdge(OOILEdge):
    def as_tuple(self):
        """ Return tuple form of edge. """
        if self.a <= self.b:
            return (self.a, self.b)
        else:
            return (self.b, self.a)

class OOILUndirectedGraph(UndirectedGraphMixin, OOILDirectedGraph):
    Edge = OOILUndirectedEdge
    def indicent_edges(self, u):
        """ Return all outgoing edges from vertex u.
        Input:
            u: OOILVertex object.
        """
        return u.edges
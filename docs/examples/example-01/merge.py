from rdflib import Graph

g = Graph()

g.parse("obj.ttl")
g.parse("pro.ttl")

g.serialize(destination="aldrovandi.ttl")
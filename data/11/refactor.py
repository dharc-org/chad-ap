import yaml
from rdflib import Graph, Namespace, URIRef, Literal, BNode

# Load mapping file
with open("mapping.yaml", "r") as f:
    config = yaml.safe_load(f)

namespaces = config["namespaces"]
mapping_rules = config["mapping_rules"]

# Define namespaces
old_abox = Namespace(namespaces["old_ns"]["abox"])
new_abox = Namespace(namespaces["new_ns"]["abox"])
lrmoo = Namespace(namespaces["new_ns"]["lrmoo"])
crm = Namespace(namespaces["new_ns"]["crm"])
crmdig = Namespace(namespaces["new_ns"]["crmdig"])
aat = Namespace(namespaces["new_ns"]["aat"])

# Load the ABox
original_abox = Graph()
original_abox.parse("../development/11/ABox.ttl", format="turtle")

# Create a new RDF graph for the refactored ABox
refactored_abox = Graph()

# Bind namespaces to prefixes
refactored_abox.bind("lrmoo", lrmoo)
refactored_abox.bind("crm", crm)
refactored_abox.bind("crmdig", crmdig)
refactored_abox.bind("aat", aat)

bnode_map = {}

# Apply mapping rules
for s, p, o in original_abox:

    new_s_uri = mapping_rules.get(str(s), str(s)).replace(old_abox, new_abox)
    new_p_uri = mapping_rules.get(str(p), str(p)).replace(old_abox, new_abox)
    
    if isinstance(s, BNode):
        if s not in bnode_map:
            bnode_map[s] = BNode()
        new_s = bnode_map[s]
    else:
        new_s = URIRef(new_s_uri)

    if isinstance(p, BNode):
        if p not in bnode_map:
            bnode_map[p] = BNode()
        new_p = bnode_map[p]
    else:
        new_p = URIRef(new_p_uri)

    if isinstance(o, Literal):
        new_o = Literal(o)
    elif isinstance(o, BNode):
        if o not in bnode_map:
            bnode_map[o] = BNode()
        new_o = bnode_map[o]
    else:
        new_o_uri = mapping_rules.get(str(o), str(o)).replace(old_abox, new_abox)
        new_o = URIRef(new_o_uri)

    refactored_abox.add((new_s, new_p, new_o))

# Serialize the refactored ABox to a new .ttl file
refactored_abox.serialize(destination="ABox.ttl", format="turtle")

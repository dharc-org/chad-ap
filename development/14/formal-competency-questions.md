# Formal Competency Questions

## CQ_14.1
Return the characteristics of all agents that are people.

```SPARQL
PREFIX obj: <https://w3id.org/dharc/ontology/chad-ap/object/development/14/schema/>

SELECT ?full_name ?f_name ?l_name ?country ?language ?gender ?profession ?date_birth ?date_death (GROUP_CONCAT(DISTINCT ?link; separator="; ") AS ?links)
WHERE {
    ?agent a obj:Person .
    OPTIONAL { ?agent obj:isIdentifiedBy [ a obj:Appellation; obj:hasType obj:full-name; obj:hasSymbolicContent ?full_name ] }
    OPTIONAL { ?agent obj:isIdentifiedBy [ a obj:Appellation; obj:hasType obj:first-name; obj:hasSymbolicContent ?f_name ] }
    OPTIONAL { ?agent obj:isIdentifiedBy [ a obj:Appellation; obj:hasType obj:last-name; obj:hasSymbolicContent ?l_name ] }
    OPTIONAL { ?agent obj:hasResidenceIn/obj:isIdentifiedBy/obj:hasSymbolicContent ?country }
    OPTIONAL { ?agent obj:isReferredToBy [ a obj:LinguisticObject; obj:hasSymbolicContent ?profession ] }
    OPTIONAL { 
    ?aa1 obj:assignsAttributeTo ?agent ; obj:assignsPropertyOfType obj:gender ; obj:assigns ?g_val .
    BIND(STR(?g_val) AS ?gender)
    }
    OPTIONAL { ?aa2 obj:assignsAttributeTo ?agent ; obj:assignsPropertyOfType obj:language ; obj:assigns ?language }
    OPTIONAL { 
    ?agent obj:wasPresentAt [ a obj:Event; obj:hasType obj:birth; obj:hasTimeSpan/obj:hasStartTime ?b_dt ] 
    BIND(STRBEFORE(STR(?b_dt), "T") AS ?date_birth)
    }
    OPTIONAL { 
        ?agent obj:wasPresentAt [ a obj:Event; obj:hasType obj:death; obj:hasTimeSpan/obj:hasStartTime ?d_dt ] 
        BIND(STRBEFORE(STR(?d_dt), "T") AS ?date_death)
    }
    OPTIONAL { ?agent obj:isIdentifiedBy [ a obj:Identifier; obj:hasType obj:uri; obj:hasSymbolicContent ?link ] }
}
GROUP BY ?full_name ?f_name ?l_name ?country ?language ?gender ?profession ?date_birth ?date_death
```

## CQ_14.2
Return the characteristics of all agents that are organisations.

```SPARQL
PREFIX obj: <https://w3id.org/dharc/ontology/chad-ap/object/development/13/schema/>

SELECT ?item ?place_label
WHERE {
    ?creation_event obj:createsExpression ?exp .
    ?exp obj:isEmbodiedIn ?mnf .
    ?mnf obj:isExemplifiedBy ?item .
    ?item obj:hasCurrentLocation ?place .
    ?place obj:isIdentifiedBy ?app .
    ?app obj:hasSymbolicContent ?place_label .
}
```

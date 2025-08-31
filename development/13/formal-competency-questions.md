# Formal Competency Questions

## CQ_13.1
Return the items, the name of the location their creation took place at, and eventually the name of the more precise location, if it exists.

```SPARQL
PREFIX obj: <https://w3id.org/dharc/ontology/chad-ap/object/development/13/schema/>

SELECT ?item (GROUP_CONCAT(?place_label; separator=", ") AS ?place_label_combined)
WHERE {
    ?creation_event obj:tookPlaceIn ?place ;
        obj:createsExpression ?exp .
    ?exp obj:isEmbodiedIn ?mnf .
    ?mnf obj:isExemplifiedBy ?item .
    ?place obj:isIdentifiedBy ?placeapp .
    ?placeapp obj:hasSymbolicContent ?place_label .
}
GROUP BY ?item
```

## CQ_13.2
Return the items and their current locations.

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

# Formal Competency Questions
## CQ_3.1
What are the cultural resources whose collections have been curated during curation events carried out by agents located in Bologna?

```SPARQL
PREFIX ex: <https://w3id.org/dharc/ontology/chad-ap/object/development/03/data/>
PREFIX obj: <https://w3id.org/dharc/ontology/chad-ap/object/development/03/schema/>

SELECT ?resource ?collection ?agent
WHERE {
    ?curation a obj:CurationEvent ;
            obj:curates ?collection ;
            obj:isCarriedOutBy ?agent ;
            obj:occurredInThePresenceOf ?resource .
    ?agent obj:hasPlace ex:bologna .
}
```

## CQ_3.2
What are the collections curated during curation events carried out by the Rijksmuseum?

```SPARQL
PREFIX ex: <https://w3id.org/dharc/ontology/chad-ap/object/development/03/data/>
PREFIX obj: <https://w3id.org/dharc/ontology/chad-ap/object/development/03/schema/>

SELECT ?collection
WHERE {
    ?curation a obj:CurationEvent ;
            obj:curates ?collection ;
            obj:isCarriedOutBy ex:rijksmuseum .
}
```

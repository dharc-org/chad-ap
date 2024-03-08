# Formal Competency Questions
## CQ_3.1
Return the `cultural resources` whose `collections` have been curated by `curation events` carried out by `agents` located in `Bologna`.

```SPARQL
PREFIX ex: <http://purl.org/changes/object/development/03/data/>
PREFIX obj: <http://purl.org/changes/object/development/03/schema/>

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
Return all `collections` curated by `curation events` carried out by `Rijksmuseum`.

```SPARQL
PREFIX ex: <http://purl.org/changes/object/development/03/data/>
PREFIX obj: <http://purl.org/changes/object/development/03/schema/>

SELECT ?collection
WHERE {
    ?curation a obj:CurationEvent ;
            obj:curates ?collection ;
            obj:isCarriedOutBy ex:rijksmuseum .
}
```

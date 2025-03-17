# Formal Competency Questions

## CQ_11.1
Return the textual content of the appellation used to label the type of a CHO and also its authority record.

```SPARQL
PREFIX obj: <https://w3id.org/dharc/ontology/chad-ap/object/development/11/schema/>

SELECT ?cho ?label ?auth
WHERE {
    ?cho a obj:Manifestation ;
      obj:hasType ?type .
      
    ?type obj:isIdentifiedBy ?appellation ;
      obj:isDocumentedIn ?auth .
    
    ?appellation obj:hasSymbolicContent ?label .
}
```

## CQ_11.2
Return all the appellations used to label the entities involved in the bibliographic description and the digitisation process of a CHO.

```SPARQL
PREFIX obj: <https://w3id.org/dharc/ontology/chad-ap/object/development/11/schema/>

SELECT ?label ?entity ?type
WHERE {
    ?entity a ?type ; 
      obj:isIdentifiedBy ?appellation .

    ?appellation a obj:Appellation ;
      obj:hasSymbolicContent ?label .
}
```

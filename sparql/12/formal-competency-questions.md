# Formal Competency Questions

## CQ_12.1
Return the type and textual content of the taxonomic ranks used to classify `699690/wrk`.

```SPARQL
PREFIX obj: <https://w3id.org/dharc/ontology/chad-ap/object/development/12/schema/>

SELECT ?type ?content
WHERE {
    <https://w3id.org/changes/4/cappellini/699690/wrk/1> obj:showsFeaturesOf ?rank .
    ?rank obj:hasType ?type ;
      obj:hasSymbolicContent ?content .
}
```

## CQ_12.2
Return the cultural heritage objects classified under the Family "Turrilitidae" and the external resources linked to them.

```SPARQL
PREFIX obj: <https://w3id.org/dharc/ontology/chad-ap/object/development/12/schema/>

SELECT ?cho ?link
WHERE {
    ?cho a obj:CulturalHeritageObject ; 
      obj:showsFeaturesOf ?rank ;
      obj:isDocumentedIn ?link .
    ?rank obj:hasSymbolicContent "Turrilitidae" .
}
```

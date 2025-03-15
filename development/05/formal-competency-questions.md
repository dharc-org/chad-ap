# Formal Competency Questions
## CQ_2.1
What are the identifiers of the printed volumes? What are their types?

```SPARQL
PREFIX ex: <https://w3id.org/dharc/ontology/chad-ap/object/development/02/data/>
PREFIX obj: <https://w3id.org/dharc/ontology/chad-ap/object/development/02/schema/>

SELECT ?resource ?identifier_text ?type
WHERE {
    ?resource a obj:CulturalResource ;
                obj:hasType obj:printed-volume ;
                obj:hasIdentifier ?identifier .
    ?identifier obj:hasType ?type ;
                obj:hasContent ?identifier_text.
}
```
## CQ_2.2
What is the shelf mark of the cultural resource with the project ID "45"?

```SPARQL
PREFIX obj: <https://w3id.org/dharc/ontology/chad-ap/object/development/02/schema/>

SELECT ?identifier_text
WHERE {
    ?resource a obj:CulturalResource ;
    obj:hasIdentifier ?identifier1 ,
                      ?identifier2 .
    ?identifier1 obj:hasType obj:project-id ;
                 obj:hasContent "45" .
    ?identifier2 obj:hasType obj:shelf-mark ;
                 obj:hasContent ?identifier_text.
}
```

## CQ_2.3
What are the descriptive labels of the cultural resources that either have shelf marks or are prints?

```SPARQL
PREFIX obj: <https://w3id.org/dharc/ontology/chad-ap/object/development/02/schema/>

SELECT ?resource ?label_text
WHERE {
    ?resource a obj:CulturalResource ;
                obj:hasIdentifier ?identifier ;
                obj:hasType ?type ;
                obj:hasLabel ?label_text .
    ?identifier obj:hasType ?id_type .
    FILTER(?type = obj:print || ?id_type = obj:shelf-mark)
}
```

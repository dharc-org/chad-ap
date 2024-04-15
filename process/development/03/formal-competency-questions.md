# Formal Competency Questions (Iteration 3)
## CQ_3.1
What are the techniques used in digitization processes?

```SPARQL
PREFIX ex: <https://w3id.org/dharc/ontology/chad-ap/process/development/03/data/>
PREFIX process: <https://w3id.org/dharc/ontology/chad-ap/process/development/03/schema/>

SELECT ?activity ?technique
WHERE {
    ?activity a process:DigitizationProcess ;
    process:hasTechnique ?technique .
}
```

## CQ_3.2
What are the tools and their types used in processing activities?

```SPARQL
PREFIX ex: <https://w3id.org/dharc/ontology/chad-ap/process/development/03/data/>
PREFIX process: <https://w3id.org/dharc/ontology/chad-ap/process/development/03/schema/>

SELECT ?tool ?type
WHERE {
    ?activity a process:SoftwareActivity ;
    process:hasType process:processing ;
    process:hasTool ?tool .
    ?tool a process:Tool ;
    process:hasType ?type .
}
```
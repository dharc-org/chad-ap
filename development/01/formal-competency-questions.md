# Formal Competency Questions (Iteration 1)
## CQ_1.1
What is the cultural object digitized and the digital object produced by the digitization process? What is the latter's license?

```SPARQL
PREFIX ex: <https://w3id.org/dharc/ontology/chad-ap/process/development/01/data/>
PREFIX process: <https://w3id.org/dharc/ontology/chad-ap/process/development/01/schema/>

SELECT ?input ?output ?license_link
WHERE {
    ?activity a process:DigitizationProcess ;
        process:digitizes ?input ;
        process:hasOutput ?output .
    ?license process:hasType process:license ;
        process:refersTo ?output ;
        process:isDocumentedIn ?license_link .
}
```

## CQ_1.2
What are the time spans during which the digitization process and the following software activities were carried out?

```SPARQL
PREFIX ex: <https://w3id.org/dharc/ontology/chad-ap/process/development/01/data/>
PREFIX process: <https://w3id.org/dharc/ontology/chad-ap/process/development/01/schema/>

SELECT ?activity ?start ?end
WHERE {
    ?activity process:hasTimeSpan ?timespan .
    ?timespan process:hasStartDate ?start ;
    process:hasEndDate ?end .
}
```
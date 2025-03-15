# Formal Competency Questions (Iteration 2)
## CQ_2.1
What are the digitization process, its output, the processing activity and its output?
```SPARQL
PREFIX ex: <https://w3id.org/dharc/ontology/chad-ap/process/development/02/data/>
PREFIX process: <https://w3id.org/dharc/ontology/chad-ap/process/development/02/schema/>

SELECT ?input ?output ?activity ?digitization
WHERE {
    ?activity a process:SoftwareActivity ;
    process:hasType process:processing ;
    process:hasInput ?input ;
    process:hasOutput ?output .
    ?digitization process:hasOutput ?input .
}
```
## CQ_2.2
Return the agents (people and institutions) who either carried out or were involved in the processing activity.
```SPARQL
PREFIX ex: <https://w3id.org/dharc/ontology/chad-ap/process/development/02/data/>
PREFIX process: <https://w3id.org/dharc/ontology/chad-ap/process/development/02/schema/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?person ?institution
WHERE {
    ?activity a process:SoftwareActivity ;
    process:hasType process:processing ;
    process:hasParticipant ?institution ;
    process:carriedOutBy ?person .
}
```
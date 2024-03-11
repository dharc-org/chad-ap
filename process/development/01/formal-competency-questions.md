# Formal Competency Questions (Iteration 1)
## CQ_1.1
What is the cultural object digitized and the digital object produced by the digitization process? What is the latter's license?

```SPARQL
PREFIX ex: <http://purl.org/changes/process/development/01/data/>
PREFIX process: <http://purl.org/changes/process/development/01/schema/>

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
Return the time period (start and end) in which the digitization process and the following software activity took place.

```SPARQL
PREFIX ex: <http://purl.org/changes/process/development/01/data/>
PREFIX process: <http://purl.org/changes/process/development/01/schema/>

SELECT ?activity ?start ?end
WHERE {
    ?activity process:hasTimeSpan ?timespan .
    ?timespan process:hasStartDate ?start ;
    process:hasEndDate ?end .
}
```
# Formal Competency Questions (Iteration 1)
## CQ_1.1
Return the input (the cultural object) ingested and the output (the digital object) produced by the Digitization Process, as well as the activity itself.

```SPARQL
PREFIX ex: <http://purl.org/changes/process/development/01/data/>
PREFIX process: <http://purl.org/changes/process/development/01/schema/>

SELECT ?input ?output ?activity
WHERE {
    ?activity a process:DigitizationProcess ;
    process:digitizes ?input ;
    process:hasOutput ?output .
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
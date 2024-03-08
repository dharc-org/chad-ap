# Formal Competency Questions
## CQ_4.1
Return all `cultural resources` and both the beginning and the end time of the `time interval` of their `conception events`

```SPARQL
PREFIX obj: <http://purl.org/changes/object/development/04/schema/>

SELECT ?resource ?beginning ?end
WHERE {
  ?conception_event a obj:ConceptionEvent ;
                    obj:initiates ?resource ;
                    obj:hasTimeInterval ?timeInterval .
  
  ?timeInterval obj:hasBeginning ?beginning ;
                 obj:hasEnd ?end .
}
```

## CQ_4.2
Return the `agents` who carried out the `conception` of a `cultural resource` in a `time interval` that comprises "1590".

```SPARQL
PREFIX obj: <http://purl.org/changes/object/development/04/schema/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?agent ?beginning ?end
WHERE {
    ?conception_event a obj:ConceptionEvent ;
                    obj:initiates ?resource ;
                    obj:isCarriedOutBy ?agent ;
                    obj:hasTimeInterval ?timeInterval .
    ?timeInterval obj:hasBeginning ?beginning ;
                        obj:hasEnd ?end .
    
FILTER (xsd:dateTime(concat(str(?beginning), "T00:00:00")) < xsd:dateTime("1591-01-01T00:00:00") && 
xsd:dateTime(concat(str(?end), "T00:00:00")) > xsd:dateTime("1589-12-31T00:00:00"))
}
```

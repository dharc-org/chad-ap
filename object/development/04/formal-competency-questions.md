# Formal Competency Questions
## CQ_4.1
What are the cultural resources and the time spans of their conception events?

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
What are the cultural resources created in a time interval that includes the year 1590?

```SPARQL
PREFIX obj: <http://purl.org/changes/object/development/04/schema/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?resource ?beginning ?end
WHERE {
    ?conception_event a obj:ConceptionEvent ;
                    obj:initiates ?resource ;
                    obj:hasTimeInterval ?timeInterval .
    ?timeInterval obj:hasBeginning ?beginning ;
                        obj:hasEnd ?end .
    
FILTER (xsd:dateTime(concat(str(?beginning), "T00:00:00")) < xsd:dateTime("1591-01-01T00:00:00") && 
xsd:dateTime(concat(str(?end), "T00:00:00")) > xsd:dateTime("1589-12-31T00:00:00"))
}
```

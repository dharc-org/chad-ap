# Formal Competency Questions
## CQ_4.1
What are the cultural resources and the time spans of their conception events?.

```SPARQL
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX frbroo: <http://iflastandards.info/ns/fr/frbr/frbroo/> 

SELECT ?resource ?beginning ?end
WHERE {
    ?conception_event a frbroo:F27_Work_Conception ;
                        frbroo:R16_initiated ?resource ;
                        crm:P4_has_time-span ?time_interval .
    ?time_interval crm:P82a_begin_of_the_begin ?beginning ;
                        crm:P82b_end_of_the_end ?end .
}
```

## CQ_4.2
What are the cultural resources created in a time interval that includes the year 1590?

```SPARQL
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX frbroo: <http://iflastandards.info/ns/fr/frbr/frbroo/> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 

SELECT ?agent ?beginning ?end
WHERE {
    ?conception_event a frbroo:F27_Work_Conception ;
                    frbroo:R16_initiated ?resource ;
                    crm:P14_carried_out_by ?agent ;
                    crm:P4_has_time-span ?time_interval .
    ?time_interval crm:P82a_begin_of_the_begin ?beginning ;
                        crm:P82b_end_of_the_end ?end .

    FILTER (xsd:dateTime(concat(str(?beginning), "T00:00:00")) < xsd:dateTime("1591-01-01T00:00:00") && 
    xsd:dateTime(concat(str(?end), "T00:00:00")) > xsd:dateTime("1589-12-31T00:00:00"))
}
```

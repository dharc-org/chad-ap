# Formal Competency Questions
## CQ_1.1
What are the cultural resources whose creation involved some illustrator?

```SPARQL
PREFIX aat: <http://vocab.getty.edu/page/aat/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX frbroo: <http://iflastandards.info/ns/fr/frbr/frbroo/> 

SELECT ?resource ?agent
WHERE {
    ?creation_event a frbroo:F28_Expression_Creation ;
            frbroo:R17_created ?resource ;
            crm:P9_consists_of ?activity .
    ?activity crm:P2_has_type aat:300054200 ;
            crm:P14_carried_out_by ?agent .
}
```

## CQ_1.2
What are the agents and the types of  activities they carried out to contribute to the creation of `24-exp`?

```SPARQL
PREFIX ex: <https://w3id.org/dharc/ontology/chad-ap/object/data/01/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX frbroo: <http://iflastandards.info/ns/fr/frbr/frbroo/> 

SELECT ?agent ?type
WHERE {
    ?creation_event a frbroo:F28_Expression_Creation ;
            frbroo:R17_created ex:24-exp ;
            crm:P9_consists_of ?activity .
    ?activity crm:P2_has_type ?type ;
            crm:P14_carried_out_by ?agent .
}
```

## CQ_1.3
What are the agents involved in the creation of the cultural resources that have been created through the engraving technique? What are  the types of the activities they carried out?

```SPARQL
PREFIX aat: <http://vocab.getty.edu/page/aat/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX frbroo: <http://iflastandards.info/ns/fr/frbr/frbroo/>  

SELECT ?resource ?agent ?type
WHERE {
    ?creation_event a frbroo:F28_Expression_Creation ;
            crm:P32_used_general_technique aat:300053225 ;
            frbroo:R17_created ?resource ;
            crm:P9_consists_of ?activity .
    ?activity crm:P2_has_type ?type ;
            crm:P14_carried_out_by ?agent .
}
```

## CQ_1.4
What are the cultural resources whose creation involved at least one agent carrying out more than one activity with different types?

```SPARQL
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX frbroo: <http://iflastandards.info/ns/fr/frbr/frbroo/>

SELECT ?resource
WHERE {
  ?event a frbroo:F28_Expression_Creation ;
         frbroo:R17_created ?resource ;
         crm:P9_consists_of ?activity1 , ?activity2 .
  ?activity1 crm:P14_carried_out_by ?agent ;
             crm:P2_has_type ?type1 .
  ?activity2 crm:P14_carried_out_by ?agent ;
             crm:P2_has_type ?type2 .
  FILTER(?type1 != ?type2)
}
GROUP BY ?resource
HAVING(COUNT(DISTINCT ?agent) = 1)
```
# Formal Competency Questions
## CQ_1.1
Return the `cultural resources` whose `creation` involved some `agent` in the role of `illustration`.

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
Return the `agents` and the role `types` of their respective `activities` that contributed to the `creation` of `ALD-24-exp`.

```SPARQL
PREFIX ex: <http://purl.org/changes/object/data/01/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX frbroo: <http://iflastandards.info/ns/fr/frbr/frbroo/> 

SELECT ?agent ?type
WHERE {
    ?creation_event a frbroo:F28_Expression_Creation ;
            frbroo:R17_created ex:ALD-24-exp ;
            crm:P9_consists_of ?activity .
    ?activity crm:P2_has_type ?type ;
            crm:P14_carried_out_by ?agent .
}
```

## CQ_1.3
Return the `agents` involved in the `creation` of the `cultural resources` that have been created through the technique `engraving`, as well as the role `types` of the `activities` they carried out.

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
Return the `cultural resources` whose `creation` involved at least one `agent` in more than one role `type`.

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
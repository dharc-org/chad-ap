# Formal Competency Questions
## CQ_5.1
What are the titles of the work `L1-work`? What are their types?

```SPARQL
PREFIX ex: <https://w3id.org/dharc/ontology/chad-ap/object/data/05/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX frbroo: <http://iflastandards.info/ns/fr/frbr/frbroo/>  

SELECT ?title ?type ?content
WHERE {
    ?creation a frbroo:F28_Expression_Creation ;
              frbroo:R19_created_a_realisation_of ex:L1-work .
    ex:L1-work crm:P102_has_title ?title .
    ?title crm:P2_has_type ?type ;
                crm:P190_has_symbolic_content ?content .
}
```
## CQ_5.2
What are the subjects of the works that are not part of any parent work?

```SPARQL
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX frbroo: <http://iflastandards.info/ns/fr/frbr/frbroo/> 

SELECT ?work ?subject
WHERE {
    ?creation a frbroo:F28_Expression_Creation ;
              frbroo:R19_created_a_realisation_of ?work ;
              frbroo:R17_created ?expression .
    ?work a frbroo:F1_Work .
    ?expression a frbroo:F2_Expression ;
                crm:P129_is_about ?subject .
    FILTER NOT EXISTS {
    ?parent frbroo:R10_has_member ?work .
  }
}
```

## CQ_5.3
What are the manifestations of the works which are members of parent works that are marine charts?

```SPARQL
PREFIX aat: <http://vocab.getty.edu/page/aat/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX frbroo: <http://iflastandards.info/ns/fr/frbr/frbroo/> 

SELECT ?manifestation
WHERE {
    ?creation a frbroo:F28_Expression_Creation ;
              frbroo:R19_created_a_realisation_of ?work ;
              frbroo:R18_created ?manifestation .
    ?parent a frbroo:F15_Complex_Work ;
            frbroo:R10_has_member ?work ;
            crm:P2_has_type aat:300028309 .
}
```

## CQ_5.4
What are the parent works of the works that have either "Europa" or "tapiro" as their subject?

```SPARQL
PREFIX ex: <https://w3id.org/dharc/ontology/chad-ap/object/data/05/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX frbroo: <http://iflastandards.info/ns/fr/frbr/frbroo/>  

SELECT ?parent ?work ?subject
WHERE {
  ?creation a frbroo:F28_Expression_Creation ;
              frbroo:R19_created_a_realisation_of ?work ;
              frbroo:R17_created ?expression .
    ?parent a frbroo:F15_Complex_Work ;
            frbroo:R10_has_member ?work .
    ?expression a frbroo:F2_Expression ;
                crm:P129_is_about ?subject .
FILTER (?subject IN (ex:sub-tapiro, ex:sub-europa))
}
```

## CQ_5.5
What are the manifestations that compose another manifestation?

```SPARQL
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 

SELECT ?manifestation1 ?manifestation2
WHERE {
  ?manifestation1 crm:P46_is_composed_of ?manifestation2 .
}
```

## CQ_5.6
What are the manifestations that depict other expressions?

```SPARQL
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 

SELECT ?manifestation ?expression
WHERE {
  ?manifestation crm:P62_depicts ?expression .
}
```

## CQ_5.7
What are the license statements referring to the manifestations?

```SPARQL
PREFIX aat: <http://vocab.getty.edu/page/aat/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 

SELECT ?manifestation ?license_link
WHERE {
  ?license crm:P67_refers_to ?manifestation ;
    crm:P2_has_type aat:300435434 ;
    crm:P70i_is_documented_in ?license_link .
}
```
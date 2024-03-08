# Formal Competency Questions
## CQ_5.1
Return the `title` of the `work` `ALD-L1-work` and its `subjects`.

```SPARQL
PREFIX ex: <http://purl.org/changes/object/data/05/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX frbroo: <http://iflastandards.info/ns/fr/frbr/frbroo/>  

SELECT ?title ?type ?content
WHERE {
    ?creation a frbroo:F28_Expression_Creation ;
              frbroo:R19_created_a_realisation_of ex:ALD-L1-work .
    ex:ALD-L1-work crm:P102_has_title ?title .
    ?title crm:P2_has_type ?type ;
                crm:P190_has_symbolic_content ?content .
}
```
## CQ_5.2
Return the `subjects` of the `works` that are not members of any `parent work`.

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
Return the `manifestations` of the `works` which are members of `parent works` whose types is `marine charts`.

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
Return the `parent works` of the `works` that have either `europa` or `tapiro` as their `subject`.

```SPARQL
PREFIX ex: <http://purl.org/changes/object/data/05/>
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
Return the `manifestations` that compose another `manifestation`.

```SPARQL
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 

SELECT ?manifestation1 ?manifestation2
WHERE {
  ?manifestation1 crm:P46_is_composed_of ?manifestation2 .
}
```

## CQ_5.6
Return the `manifestations` that depict other `expressions`.

```SPARQL
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 

SELECT ?manifestation ?expression
WHERE {
  ?manifestation crm:P62_depicts ?expression .
}
```
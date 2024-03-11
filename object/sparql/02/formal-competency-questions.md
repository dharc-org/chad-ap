# Formal Competency Questions
## CQ_2.1
What are the identifiers of the printed volumes? What are their types?

```SPARQL
PREFIX aat: <http://vocab.getty.edu/page/aat/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX frbroo: <http://iflastandards.info/ns/fr/frbr/frbroo/> 

SELECT ?resource ?identifier_text ?type
WHERE {
    ?resource a frbroo:F4_Manifestation_Singleton ;
                crm:P2_has_type aat:300265632 ;
                crm:P48_has_preferred_identifier ?identifier .
    ?identifier crm:P2_has_type ?type ;
                crm:P190_has_symbolic_content ?identifier_text.
}
```
## CQ_2.2
What is the shelf mark of the cultural resource with the project ID "ALD-45"?

```SPARQL
PREFIX aat: <http://vocab.getty.edu/page/aat/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX frbroo: <http://iflastandards.info/ns/fr/frbr/frbroo/> 

SELECT ?identifier_text
WHERE {
    ?resource a frbroo:F4_Manifestation_Singleton ;
    crm:P48_has_preferred_identifier ?identifier1 ,
                      ?identifier2 .
    ?identifier1 crm:P2_has_type aat:300312355 ;
                 crm:P190_has_symbolic_content "ALD-45" .
    ?identifier2 crm:P2_has_type aat:300404704 ;
                 crm:P190_has_symbolic_content ?identifier_text.
}
```

## CQ_2.3
What are the descriptive labels of the cultural resources that either have shelf marks or are prints?

```SPARQL
PREFIX aat: <http://vocab.getty.edu/page/aat/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX frbroo: <http://iflastandards.info/ns/fr/frbr/frbroo/> 

SELECT ?resource ?label
WHERE {
    ?resource a frbroo:F4_Manifestation_Singleton ;
                crm:P48_has_preferred_identifier ?identifier ;
                crm:P2_has_type ?type ;
                crm:P3_has_note ?label .
    ?identifier crm:P2_has_type ?id_type .
    FILTER(?type = aat:300041273 || ?id_type = aat:300404704)
}
```

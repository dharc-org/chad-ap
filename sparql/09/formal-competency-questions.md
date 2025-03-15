# Formal Competency Questions
## CQ_6.1
What are the titles of the work? What are their types?

```SPARQL
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX lrmoo: <http://iflastandards.info/ns/lrm/lrmoo/>

SELECT ?title ?type ?content
WHERE {
    ?creation a lrmoo:F28_Expression_Creation ;
      lrmoo:R19_created_a_realisation_of ?work .
    ?work crm:P102_has_title ?title .
    ?title crm:P2_has_type ?type ;
        crm:P190_has_symbolic_content ?content .
}
```

## CQ_6.2
Which work was created and in which period?

```SPARQL
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX lrmoo: <http://iflastandards.info/ns/lrm/lrmoo/>

SELECT ?work ?start_date ?end_date
WHERE {
    ?creation a lrmoo:F28_Expression_Creation ;
      lrmoo:R19_created_a_realisation_of ?work ;
      crm:P4_has_time-span ?time_span .
    ?time_span crm:P82a_begin_of_the_begin ?start_date ;
      crm:P82b_end_of_the_end ?end_date .
}
```

## CQ_6.3
Which works are part of other works? What are the types of the larger works?

```SPARQL
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX lrmoo: <http://iflastandards.info/ns/lrm/lrmoo/>

SELECT ?work ?larger_work ?type
WHERE {
    ?creation a lrmoo:F28_Expression_Creation ;
      lrmoo:R19_created_a_realisation_of ?work .
    ?larger_work a lrmoo:F1_Work ;
      lrmoo:R10_has_member ?work ;
      lrmoo:R3_is_realised_in ?larger_exp .
    ?larger_exp lrmoo:R4i_is_embodied_in ?larger_man .
    ?larger_man crm:P2_has_type ?type .
}
```

## CQ_6.4
What is the cultural object about?

```SPARQL
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX lrmoo: <http://iflastandards.info/ns/lrm/lrmoo/>

SELECT ?expression ?subject
WHERE {
    ?creation a lrmoo:F28_Expression_Creation ;
      lrmoo:R17_created ?expression .
    ?expression a lrmoo:F2_Expression ;
      crm:P129_is_about ?subject .
}
```

## CQ_6.5
What is the type of the cultural object?

```SPARQL
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX lrmoo: <http://iflastandards.info/ns/lrm/lrmoo/>

SELECT ?manifestation ?type
WHERE {
    ?creation a lrmoo:F28_Expression_Creation ;
      lrmoo:R17_created ?expression .
    ?expression lrmoo:R4i_is_embodied_in ?manifestation .
    ?manifestation crm:P2_has_type ?type .
}
```

## CQ_6.6
Which license statement is assigned to the cultural object?

```SPARQL
PREFIX aat: <http://vocab.getty.edu/page/aat/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX lrmoo: <http://iflastandards.info/ns/lrm/lrmoo/>

SELECT ?manifestation ?license ?external_resource
WHERE {
    ?creation a lrmoo:F28_Expression_Creation ;
      lrmoo:R17_created ?expression .
    ?expression lrmoo:R4i_is_embodied_in ?manifestation .
    ?license crm:P2_has_type aat:300435434 ;
      crm:P67_refers_to ?manifestation ;
      crm:P70i_is_documented_in ?external_resource .
}
```

## CQ_6.7
What are the identifiers identifying the cultural object? What are their types?

```SPARQL
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX lrmoo: <http://iflastandards.info/ns/lrm/lrmoo/>

SELECT ?identifier ?type ?content
WHERE {
    ?creation a lrmoo:F28_Expression_Creation ;
      lrmoo:R17_created ?expression .
    ?expression lrmoo:R4i_is_embodied_in ?manifestation .
    ?manifestation lrmoo:R7i_is_exemplified_by ?item .
    ?item crm:P1_is_identified_by ?identifier .
    ?identifier crm:P2_has_type ?type ;
      crm:P190_has_symbolic_content ?content .
}
```

## CQ_6.8
What is the curation activity in which the object is involved? Who carried it out?

```SPARQL
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX lrmoo: <http://iflastandards.info/ns/lrm/lrmoo/>

SELECT ?item ?activity ?actor
WHERE {
    ?creation a lrmoo:F28_Expression_Creation ;
      lrmoo:R17_created ?expression .
    ?expression lrmoo:R4i_is_embodied_in ?manifestation .
    ?manifestation lrmoo:R7i_is_exemplified_by ?item .
    ?activity crm:P16_used_specific_object ?item ;
      crm:P14_carried_out_by ?actor .
}
```

## CQ_6.9
What is the description of the cultural object?

```SPARQL
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX lrmoo: <http://iflastandards.info/ns/lrm/lrmoo/>

SELECT ?item ?description
WHERE {
    ?creation a lrmoo:F28_Expression_Creation ;
      lrmoo:R17_created ?expression .
    ?expression lrmoo:R4i_is_embodied_in ?manifestation .
    ?manifestation lrmoo:R7i_is_exemplified_by ?item .
    ?item crm:P3_has_note ?description .
}
```
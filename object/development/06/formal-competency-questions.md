# Formal Competency Questions
## CQ_6.1
What are the titles of the work? What are their types?

```SPARQL
PREFIX ex: <https://w3id.org/dharc/ontology/chad-ap/object/development/06/data/>
PREFIX obj: <https://w3id.org/dharc/ontology/chad-ap/object/development/06/schema/>

SELECT ?title ?type ?content
WHERE {
    ?creation a obj:CreationEvent ;
      obj:createsWork ?work .
    ?work obj:hasTitle ?title .
    ?title obj:hasType ?type ;
        obj:hasContent ?content .
}
```
## CQ_6.2
Which work was created and in which period?

```SPARQL
PREFIX ex: <https://w3id.org/dharc/ontology/chad-ap/object/development/06/data/>
PREFIX obj: <https://w3id.org/dharc/ontology/chad-ap/object/development/06/schema/>

SELECT ?work ?start_date ?end_date
WHERE {
    ?creation a obj:CreationEvent ;
      obj:createsWork ?work ;
      obj:hasTimeSpan ?time_span .
    ?time_span obj:hasStartDate ?start_date ;
      obj:hasEndDate ?end_date .
}
```

## CQ_6.3
Which works are part of other works? What are the types of the larger works?

```SPARQL
PREFIX ex: <https://w3id.org/dharc/ontology/chad-ap/object/development/06/data/>
PREFIX obj: <https://w3id.org/dharc/ontology/chad-ap/object/development/06/schema/>

SELECT ?work ?larger_work ?type
WHERE {
    ?creation a obj:CreationEvent ;
      obj:createsWork ?work .
    ?larger_work a obj:Work ;
      obj:hasMember ?work ;
      obj:isRealizedIn ?larger_exp .
    ?larger_exp obj:isEmbodiedIn ?larger_man .
    ?larger_man obj:hasType ?type .
}
```

## CQ_6.4
What is the cultural object about?

```SPARQL
PREFIX ex: <https://w3id.org/dharc/ontology/chad-ap/object/development/06/data/>
PREFIX obj: <https://w3id.org/dharc/ontology/chad-ap/object/development/06/schema/>

SELECT ?expression ?subject
WHERE {
    ?creation a obj:CreationEvent ;
      obj:createsExpression ?expression .
    ?expression a obj:Expression ;
      obj:isAbout ?subject .
}
```

## CQ_6.5
What is the type of the cultural object?

```SPARQL
PREFIX ex: <https://w3id.org/dharc/ontology/chad-ap/object/development/06/data/>
PREFIX obj: <https://w3id.org/dharc/ontology/chad-ap/object/development/06/schema/>

SELECT ?manifestation ?type
WHERE {
    ?creation a obj:CreationEvent ;
      obj:createsExpression ?expression .
    ?expression obj:isEmbodiedIn ?manifestation .
    ?manifestation obj:hasType ?type .
}
```

## CQ_6.6
Which license statement is assigned to the cultural object?

```SPARQL
PREFIX ex: <https://w3id.org/dharc/ontology/chad-ap/object/development/06/data/>
PREFIX obj: <https://w3id.org/dharc/ontology/chad-ap/object/development/06/schema/>

SELECT ?manifestation ?license ?external_resource
WHERE {
    ?creation a obj:CreationEvent ;
      obj:createsExpression ?expression .
    ?expression obj:isEmbodiedIn ?manifestation .
    ?license obj:type obj:license-statement ;
      obj:refersTo ?manifestation ;
      obj:isDocumentedIn ?external_resource .
}
```

## CQ_6.7
What are the identifiers identifying the cultural object? What are their types?

```SPARQL
PREFIX ex: <https://w3id.org/dharc/ontology/chad-ap/object/development/06/data/>
PREFIX obj: <https://w3id.org/dharc/ontology/chad-ap/object/development/06/schema/>

SELECT ?identifier ?type ?content
WHERE {
    ?creation a obj:CreationEvent ;
      obj:createsExpression ?expression .
    ?expression obj:isEmbodiedIn ?manifestation .
    ?manifestation obj:isExemplifiedBy ?item .
    ?item obj:hasIdentifier ?identifier .
    ?identifier obj:hasType ?type ;
      obj:hasContent ?content .
}
```

## CQ_6.8
What is the curation activity in which the object is involved? Who carried it out?

```SPARQL
PREFIX ex: <https://w3id.org/dharc/ontology/chad-ap/object/development/06/data/>
PREFIX obj: <https://w3id.org/dharc/ontology/chad-ap/object/development/06/schema/>

SELECT ?item ?activity ?actor
WHERE {
    ?creation a obj:CreationEvent ;
      obj:createsExpression ?expression .
    ?expression obj:isEmbodiedIn ?manifestation .
    ?manifestation obj:isExemplifiedBy ?item .
    ?activity obj:usesObject ?item ;
      obj:isCarriedOutBy ?actor .
}
```

## CQ_6.9
What is the description of the cultural object?

```SPARQL
PREFIX ex: <https://w3id.org/dharc/ontology/chad-ap/object/development/06/data/>
PREFIX obj: <https://w3id.org/dharc/ontology/chad-ap/object/development/06/schema/>

SELECT ?item ?description
WHERE {
    ?creation a obj:CreationEvent ;
      obj:createsExpression ?expression .
    ?expression obj:isEmbodiedIn ?manifestation .
    ?manifestation obj:isExemplifiedBy ?item .
    ?item obj:hasDescription ?description .
}
```
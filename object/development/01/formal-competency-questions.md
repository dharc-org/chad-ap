# Formal Competency Questions
## CQ_1.1
What are the cultural resources whose creation involved some illustrator?

```SPARQL
PREFIX ex: <http://purl.org/changes/object/development/01/data/>
PREFIX obj: <http://purl.org/changes/object/development/01/schema/>

SELECT ?resource ?agent
WHERE {
    ?creation_event a obj:CreationEvent ;
            obj:creates ?resource ;
            obj:consistsOf ?activity .
    ?activity obj:hasType obj:illustration ;
            obj:isCarriedOutBy ?agent .
}
```
## CQ_1.2
What are the agents and the types of  activities they carried out to contribute to the creation of `ALD-24-exp`?

```SPARQL
PREFIX ex: <http://purl.org/changes/object/development/01/data/>
PREFIX obj: <http://purl.org/changes/object/development/01/schema/>

SELECT ?agent ?type
WHERE {
    ?creation_event a obj:CreationEvent ;
            obj:creates ex:ALD-24-exp ;
            obj:consistsOf ?activity .
    ?activity obj:hasType ?type ;
            obj:isCarriedOutBy ?agent .
}
```

## CQ_1.3
What are the agents involved in the creation of the cultural resources that have been created through the engraving technique? What are  the types of the activities they carried out?

```SPARQL
PREFIX ex: <http://purl.org/changes/object/development/01/data/>
PREFIX obj: <http://purl.org/changes/object/development/01/schema/>

SELECT ?resource ?agent ?type
WHERE {
    ?creation_event a obj:CreationEvent ;
            obj:usesTechnique obj:engraving ;
            obj:creates ?resource ;
            obj:consistsOf ?activity .
    ?activity obj:hasType ?type ;
            obj:isCarriedOutBy ?agent .
}
```

## CQ_1.4
What are the cultural resources whose creation involved at least one agent carrying out more than one activity with different types?

```SPARQL
PREFIX ex: <http://purl.org/changes/object/development/01/data/>
PREFIX obj: <http://purl.org/changes/object/development/01/schema/>

SELECT ?resource
WHERE {
  ?event a obj:CreationEvent ;
         obj:creates ?resource ;
         obj:consistsOf ?activity1 , ?activity2 .
  ?activity1 obj:isCarriedOutBy ?agent ;
             obj:hasType ?type1 .
  ?activity2 obj:isCarriedOutBy ?agent ;
             obj:hasType ?type2 .
  FILTER(?type1 != ?type2)
}
GROUP BY ?resource
HAVING(COUNT(DISTINCT ?agent) = 1)
```
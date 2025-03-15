# Formal Competency Questions
## CQ_7.1
Return the digital representation of a cultural heritage object at the Manifestation level.

```SPARQL
PREFIX ex: <https://w3id.org/dharc/ontology/chad-ap/object/development/07/data/>
PREFIX obj: <https://w3id.org/dharc/ontology/chad-ap/object/development/07/schema/>

SELECT ?cho ?digital_rep
WHERE {
    ?cho a obj:Manifestation ;
      obj:hasCopy ?digital_rep .
}
```

## CQ_7.2
Return the data object used as a base for the data object taken as the input of the optimization phase during the digitization process of a cultural heritage object.

```SPARQL
PREFIX ex: <https://w3id.org/dharc/ontology/chad-ap/object/development/07/data/>
PREFIX obj: <https://w3id.org/dharc/ontology/chad-ap/object/development/07/schema/>

SELECT ?item ?existing_obj
WHERE {
    ?item a obj:Item ;
      obj:hasCopy ?data_obj .

    ?data_obj a obj:DataObject ;
      obj:isCopyOf ?existing_obj .

    ?activity a obj:SoftwareActivity ;
      obj:hasInput ?data_obj ;
      obj:hasType obj:optimization .
}
```

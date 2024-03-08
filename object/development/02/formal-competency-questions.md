# Formal Competency Questions
## CQ_2.1
Return all `identifiers` of the `cultural resources` with `type` `printed volume`, as well as their `types`.

```SPARQL
PREFIX ex: <http://purl.org/changes/object/development/02/data/>
PREFIX obj: <http://purl.org/changes/object/development/02/schema/>

SELECT ?resource ?identifier_text ?type
WHERE {
    ?resource a obj:CulturalResource ;
                obj:hasType obj:printed-volume ;
                obj:hasIdentifier ?identifier .
    ?identifier obj:hasType ?type ;
                obj:hasContent ?identifier_text.
}
```
## CQ_2.2
Return the `identifier` with `type` `shelf mark` of the `cultural resource` with an `identifier` with `type` `project id` equal to "ALD-45".

```SPARQL
PREFIX obj: <http://purl.org/changes/object/development/02/schema/>

SELECT ?identifier_text
WHERE {
    ?resource a obj:CulturalResource ;
    obj:hasIdentifier ?identifier1 ,
                      ?identifier2 .
    ?identifier1 obj:hasType obj:changes-id ;
                 obj:hasContent "ALD-45" .
    ?identifier2 obj:hasType obj:shelf-mark ;
                 obj:hasContent ?identifier_text.
}
```

## CQ_2.3
Return the `descriptive labels` of the `cultural resources` that either have `identifiers` with `type` `shelf mark` or have `type` `print`.

```SPARQL
PREFIX obj: <http://purl.org/changes/object/development/02/schema/>

SELECT ?resource ?label_text
WHERE {
    ?resource a obj:CulturalResource ;
                obj:hasIdentifier ?identifier ;
                obj:hasType ?type ;
                obj:hasLabel ?label_text .
    ?identifier obj:hasType ?id_type .
    FILTER(?type = obj:print || ?id_type = obj:shelf-mark)
}
```

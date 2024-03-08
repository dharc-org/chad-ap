# Formal Competency Questions
## CQ_5.1
Return the `title` of the `work` `ALD-L1-work` and its `subjects`.

```SPARQL
PREFIX ex: <http://purl.org/changes/object/development/05/data/>
PREFIX obj: <http://purl.org/changes/object/development/05/schema/>

SELECT ?title ?subject
WHERE {
    ?creation a obj:CreationEvent ;
              obj:createsWork ex:ALD-L1-work ;
              obj:createsExpression ?expression .
    ex:ALD-L1-work obj:hasTitle ?title .
    ?expression a obj:Expression ;
                obj:isAbout ?subject .
}
```
## CQ_5.2
Return the `subjects` of the `works` that are not members of any `parent work`.

```SPARQL
PREFIX ex: <http://purl.org/changes/object/development/05/data/>
PREFIX obj: <http://purl.org/changes/object/development/05/schema/>

SELECT ?work ?subject
WHERE {
    ?creation a obj:CreationEvent ;
              obj:createsWork ?work ;
              obj:createsExpression ?expression .
    ?work a obj:Work .
    ?expression a obj:Expression ;
                obj:isAbout ?subject .
    FILTER NOT EXISTS {
    ?parent obj:hasMember ?work .
  }
}
```

## CQ_5.3
Return the `manifestations` of the `works` which are members of `parent works` whose types is `marine charts`.

```SPARQL
PREFIX ex: <http://purl.org/changes/object/development/05/data/>
PREFIX obj: <http://purl.org/changes/object/development/05/schema/>

SELECT ?manifestation
WHERE {
    ?creation a obj:CreationEvent ;
              obj:createsWork ?work ;
              obj:createsManifestation ?manifestation .
    ?parent a obj:ParentWork ;
            obj:hasMember ?work ;
            obj:hasType obj:marine-chart .
}
```

## CQ_5.4
Return the `parent works` of the `works` that have either `europa` or `tapiro` as their `subject`.

```SPARQL
PREFIX ex: <http://purl.org/changes/object/development/05/data/>
PREFIX obj: <http://purl.org/changes/object/development/05/schema/>

SELECT ?parent ?work ?subject
WHERE {
  ?creation a obj:CreationEvent ;
              obj:createsWork ?work ;
              obj:createsExpression ?expression .
    ?parent a obj:ParentWork ;
            obj:hasMember ?work .
    ?expression a obj:Expression ;
                obj:isAbout ?subject .
  
  FILTER(?subject == ex:sub-tapiro ||
         ?subject == ex:sub-europa)
}
```

## CQ_5.5
Return the `manifestations` that compose another `manifestation`.

```SPARQL
PREFIX ex: <http://purl.org/changes/object/development/05/data/>
PREFIX obj: <http://purl.org/changes/object/development/05/schema/>

SELECT ?manifestation1 ?manifestation2
WHERE {
  ?manifestation1 obj:isComposedOf ?manifestation2 .
}
```

## CQ_5.6
Return the `manifestations` that depict other `expressions`.

```SPARQL
PREFIX ex: <http://purl.org/changes/object/development/05/data/>
PREFIX obj: <http://purl.org/changes/object/development/05/schema/>

SELECT ?manifestation ?expression
WHERE {
  ?manifestation obj:depicts ?expression .
}
```
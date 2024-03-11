# Formal Competency Questions
## CQ_5.1
What are the titles of the work `L1-work`? What are their types?

```SPARQL
PREFIX ex: <http://purl.org/changes/object/development/05/data/>
PREFIX obj: <http://purl.org/changes/object/development/05/schema/>

SELECT ?title ?type ?content
WHERE {
    ?creation a obj:CreationEvent ;
              obj:createsWork ex:L1-work .
    ex:L1-work obj:hasTitle ?title .
    ?title obj:hasType ?type ;
        obj:hasContent ?content .
}
```
## CQ_5.2
What are the subjects of the works that are not part of any parent work?

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
What are the manifestations of the works which are members of parent works that are marine charts?

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
What are the parent works of the works that have either "Europa" or "tapiro" as their subject?

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
What are the manifestations that compose another manifestation?

```SPARQL
PREFIX ex: <http://purl.org/changes/object/development/05/data/>
PREFIX obj: <http://purl.org/changes/object/development/05/schema/>

SELECT ?manifestation1 ?manifestation2
WHERE {
  ?manifestation1 obj:isComposedOf ?manifestation2 .
}
```

## CQ_5.6
What are the manifestations that depict other expressions?

```SPARQL
PREFIX ex: <http://purl.org/changes/object/development/05/data/>
PREFIX obj: <http://purl.org/changes/object/development/05/schema/>

SELECT ?manifestation ?expression
WHERE {
  ?manifestation obj:depicts ?expression .
}
```

## CQ_5.7
What are the license statements referring to the manifestations?

```SPARQL
PREFIX ex: <http://purl.org/changes/object/development/05/data/>
PREFIX obj: <http://purl.org/changes/object/development/05/schema/>

SELECT ?manifestation ?license_link
WHERE {
  ?license obj:refersTo ?manifestation ;
    obj:hasType obj:license ;
    obj:isDocumentedIn ?license_link .
}
```
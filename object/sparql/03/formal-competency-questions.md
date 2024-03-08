# Formal Competency Questions
## CQ_3.1
Return the `cultural resources` whose `collections` have been curated by `curation events` carried out by `agents` located in `Bologna`.

```SPARQL
PREFIX ex: <http://purl.org/changes/object/data/03/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 

SELECT ?resource ?collection ?agent
WHERE {
    ?curation a crm:E87_Curation_Activity ;
            crm:P147_curated ?collection ;
            crm:P14_carried_out_by ?agent ;
            crm:P12_occurred_in_the_presence_of ?resource .
    ?agent crm:P74_has_current_or_former_residence ex:bologna .
}
```

## CQ_3.2
Return all `collections` curated by `curation events` carried out by `Rijksmuseum`.

```SPARQL
PREFIX ex: <http://purl.org/changes/object/data/03/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 

SELECT ?collection
WHERE {
    ?curation a crm:E87_Curation_Activity ;
            crm:P147_curated ?collection ;
            crm:P14_carried_out_by ex:rijksmuseum .
}
```

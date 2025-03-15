# Formal Competency Questions
## CQ_7.1
Return the digital representation of a cultural heritage object at the Manifestation level.

```SPARQL
PREFIX aat: <http://vocab.getty.edu/page/aat/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX crmdig: <http://www.cidoc-crm.org/extensions/crmdig/>
PREFIX lrmoo: <http://iflastandards.info/ns/lrm/lrmoo/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT ?cho ?digital_rep
WHERE {
    ?cho a lrmoo:F3_Manifestation ;
      crm:P130i_features_are_also_found_on ?digital_rep .
}
```

## CQ_7.2
Return the data object used as a base for the data object taken as the input of the optimization phase during the digitization process of a cultural heritage object.

```SPARQL
PREFIX aat: <http://vocab.getty.edu/page/aat/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX crmdig: <http://www.cidoc-crm.org/extensions/crmdig/>
PREFIX lrmoo: <http://iflastandards.info/ns/lrm/lrmoo/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT ?item ?existing_obj
WHERE {
    ?item a lrmoo:F5_Item ;
      crm:P130i_features_are_also_found_on ?data_obj .

    ?data_obj a crmdig:D9_Data_Object ;
      crm:P130_shows_features_of ?existing_obj .

    ?activity a crmdig:D10_Software_Execution ;
      crmdig:L10_had_input ?data_obj ;
      crm:P2_has_type aat:300386427 .
}
```

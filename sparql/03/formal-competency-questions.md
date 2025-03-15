# Formal Competency Questions (Iteration 2)
## CQ_3.1
Return the techniques used in acquisition activities.

```SPARQL
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX crmdig: <http://www.ics.forth.gr/isl/CRMdig/>

SELECT ?technique ?activity
WHERE {
    ?activity a crmdig:D2_Digitization_Process ;
    crm:P32_used_general_technique ?technique .
}
```
## CQ_3.2
What are the tools and their types used in processing activities?

```SPARQL
PREFIX aat: <http://vocab.getty.edu/page/aat/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX crmdig: <http://www.ics.forth.gr/isl/CRMdig/>

SELECT ?tool ?type
WHERE {
    ?activity a crmdig:D10_Software_Execution ;
        crm:P2_has_type aat:300054636 ;
        crmdig:L23_used_software_or_firmware ?tool .
    ?tool a crmdig:D14_Software ;
        crm:P2_has_type ?type .
}
```
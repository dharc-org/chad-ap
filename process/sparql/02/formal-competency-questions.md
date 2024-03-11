# Formal Competency Questions (Iteration 2)
## CQ_2.1
What are the digitization process, its output, the processing activity and its output?

```SPARQL
PREFIX aat: <http://vocab.getty.edu/page/aat/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX crmdig: <http://www.ics.forth.gr/isl/CRMdig/>

SELECT ?digitization ?input ?activity ?output
WHERE {
    ?activity a crmdig:D10_Software_Execution ;
    crm:P2_has_type aat:300054636 ;
    crmdig:L10_had_input ?input ;
    crmdig:L11_had_output ?output .
    ?digitization crmdig:L11_had_output ?input .
}
```
## CQ_2.2
Return the agents (people and institutions) who either carried out or were involved in the processing activity.

```SPARQL
PREFIX aat: <http://vocab.getty.edu/page/aat/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX crmdig: <http://www.ics.forth.gr/isl/CRMdig/>

SELECT ?person ?institution
WHERE {
    ?activity a crmdig:D10_Software_Execution ;
    crm:P2_has_type aat:300054636 ;
    crm:P14_carried_out_by ?person ;
    crm:P11_had_participant ?institution .
}
```
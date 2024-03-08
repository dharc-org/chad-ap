# Formal Competency Questions

## CQ_1.1
Return the input (the cultural object) ingested and the output (the digital object) produced by the digitization process, as well as the activity itself.

```SPARQL
PREFIX crmdig: <http://www.ics.forth.gr/isl/CRMdig/> 

SELECT ?input ?output ?activity
WHERE {
    ?activity a crmdig:D2_Digitization_Process ;
        crmdig:L1_digitized ?input ;
        crmdig:L11_had_output ?output .
}
```

## CQ_1.2
Return the time period (start and end) in which the digitization process and the following software activity took place.

```SPARQL
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> 
PREFIX crmdig: <http://www.ics.forth.gr/isl/CRMdig/> 

SELECT ?activity ?start ?end
WHERE {
    ?activity a crmdig:D2_Digitization_Process;
        crm:P4_has_time-span ?timespan .
    ?timespan crm:P82a_begin_of_the_begin ?start ;
        crm:P82b_end_of_the_end ?end .
}
```
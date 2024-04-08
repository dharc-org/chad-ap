# Formal Competency Questions

## CQ_1.1
What is the cultural object digitized and the digital object produced by the digitization process? What is the latter's license?

```SPARQL
PREFIX aat: <http://vocab.getty.edu/page/aat/>
PREFIX crmdig: <http://www.ics.forth.gr/isl/CRMdig/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT ?input ?output ?license_link
WHERE {
    ?activity a crmdig:D2_Digitization_Process ;
        crmdig:L1_digitized ?input ;
        crmdig:L11_had_output ?output .
    ?license crm:P2_has_type aat:300435434 ;
        crm:P67_refers_to ?output ;
        crm:P70i_is_documented_in ?license_link .
}
```

## CQ_1.2
What are the time spans during which the digitization process and the following software activities were carried out?

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
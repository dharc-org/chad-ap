## Description

The Cultural Heritage Acquisition and Digitisation Application Profile (CHAD-AP, https://w3id.org/dharc/ontology/chad-ap) is a CIDOC CRM application profile implemented as an OWL ontology that can be logically split into two separate abstract modules: the _Object Module_ (OM), dedicated to describing the CHOs, and the _Process Module_ (PM), for describing the acquisition and digitisation process.

Both CHAD-AP and its [documentation](https://w3id.org/dharc/ontology/chad-ap) are living artefacts that have been drafted in the context of the [Project CHANGES](https://sites.google.com/uniroma1.it/changes/) ("Cultural Heritage Active Innovation For Next-Gen Sustainable Society"), an EU-funded project that aims at increasing, at the Italian level, the curation, and management of cultural heritage artefacts in all forms, expanding the involvement of the general public, making more sustainable the exhibition potential, and including crucial social functions (accessibility, inclusiveness, critical thinking, participation, enjoyment, sustainability) into the cultural heritage environment.

Currently, CHAD-AP is able to describe the following entities:
* CHOs, described according to the Functional Requirements for Bibliographic Records (FRBR) data model, which uses several descriptive layers for its representation. In particular, CHAD-AP considers: the essence or conceptualisation of the CHO (_Work_); the intellectual content of the CHO (_Expression_); the embodiment of the CHO in terms of its format (_Manifestation_); and the physical exemplar of the CHO (_Item_);
* Activities, events, agents involved and their roles;
* Descriptive components, such as labels, types, identifiers and titles;
* Entities related to curation and conservation, like curation events, places of conservation, agent responsible for its conservation, etc.
* Concepts and other immaterial objects, such as the subjects illustrated by CHOs and the licenses or right statements assigned to them;
* Digitization processes used to capture 3D data of CHOs and to output their digital models, and software activities leveraging these DCHOs as input for further processes.

The current version of the application profile reuses a subset of classes and properties selected from the following models:

* [CIDOC CRM](http://www.cidoc-crm.org/cidoc-crm/) is an international ISO standard that provides an ontology related to cultural heritage and museum documentation, which can be extended with additional modules for covering particular descriptions at hand;
* [CRMdig](http://www.ics.forth.gr/isl/CRMdig/) is an extension of CIDOC CRM for describing metadata related to the digital provenance of digitisation processes and digital representations;
* [LRMoo](http://iflastandards.info/ns/lrm/lrmoo/) is an ontology for representing bibliographic information according to the LRM data model within the CIDOC CRM framework;
* [AAT](http://vocab.getty.edu/page/aat/) is a structured vocabulary of terms used to describe art, architecture, decorative arts, and material culture.

A full version of CHAD-AP is available at [https://w3id.org/dharc/ontology/chad-ap](https://w3id.org/dharc/ontology/chad-ap).

The next subsections provide a quick overview of all the entities defined, some exemple of usage, and some of the queries that CHAD-AP can answer.

### Object Module (OM)
As shown in the diagram below, a Cultural Heritage Object (CHO) is described in CHAD-AP according to the Functional Requirements for Bibliographic Records (FRBR) data model, which uses several descriptive layers for its representation. 

![A diagram of the CHAD-AP Object Module (OM).](diagrams/object-model.png)

In particular, the _Work_ (`lrmoo:F1_Work`) represents the _essence_ or conceptualization of the CHO. Each work is associated with a series of titles (`crm:E35_Title`), each classified according to a particular type (`crm:E55_Type`), which can be an _original title_ (`aat:300417204`) or an _exhibition title_ (`aat:300417207`). Furthermore, a Work can be part of a larger Work, like a series of printed volumes, which is classified under a particular type (`crm:E55_Type`).

The _Expression_ (`lrmoo:F2_Expression`) is the realisation of a Work, and refers to the intellectual _content_ of the object. Both the Expression and the Work are generated through a creation event (`lrmoo:F28_Expression_Creation`) occurring within a specific time span (`crm:E52_Time-Span`), which can be expressed as either a precisely defined period with exact starting and ending date times (`crm:P82a_begin_of_the_begin` and `crm:P82b_end_of_the_end`) or a fuzzy label if its temporal extents are not precisely known (`crm:P82_at_some_time_within`). A creation event is made of smaller activities (`crm:E7_Activity`), each conducted by one or more agents (`crm:E39_Actor`) and characterised by a specific type (`crm:E55_Type`) that defines, implicitly, the role assumed by the agent for that activity. For example, if the agent is identified as the author of the Expression, the activity type is represented as _writing_ (`aat:300054698`). Also, creation events employ various creation techniques (`crm:E55_Type`). For example, `aat:300054196` is used to express _drawing technique_. An Expression can also be associated with one or more subjects defining its contents. In CHAD-AP, a generic _concept_ is represented with the class `crm:E73_Information_Object` with the type `aat:300404126` (i.e. _subject_) explicitly specified.

The _Manifestation_ (`lrmoo:F3_Manifestation`) represents the embodiment of the CHO's content in a physical format. It is characterised by having a type (`crm:E55_Type`). In addition, Manifestations are associated with copyright or licensing statements (represented through the combination of `crm:E73_Information_Object` having type `aat:300435434`, i.e.  _copyright/licensing statement_), linked with the document introducing the actual license or right statements through the property `crm:P70i_is_documented_in`.

Finally, the _Item_ (`lrmoo:F5_Item`) represents the physical, localised exemplar of the CHO. It is accompanied with descriptive components like labels (expressed through the use of the property `crm:P3_has_note`) and identifiers (`crm:E42_Identifier`, each with its own content and type). Items can depict the content (`lrmoo:F2_Expression`) of another CHO. Sometimes, an Item may be linked to a curation activity (represented through the combination of `crm:E7_Activity` with type `aat:300054277`, i.e. _curating_) carried out by a keeper (`crm:E39_Actor`) who manages a collection (`crm:E24_Physical_Human-Made_Thing` with type `aat:300025976`, i.e. _collections_) to which the object belongs, located in a specific place (`crm:E53_Place`). An Item can also be composed of (`crm:P46_is_composed_of`) other Items.

Whenever possible, instances of `crm:E39_Actor` and `crm:E53_Place` are also linked with existing authority records through the property `crm:P1_is_identified_by`.

### Process Module (PM)
As shown in the diagram below, CHAD-AP also describes the entities for defining a 3D digitisation workflow as a sequence of activities classified according to two main categories. 

![A diagram of the CHAD-AP Process Module (PM).](diagrams/process-model.png)

On the one hand, we have the _acquisition activity_ (`crmdig:D2_Digitization_Process`), which involves the digitisation of a CHO (`crm:E24_Physical_Human-Made_Thing`) to produce a Digital CHO (DCHO) (`crmdig:D9_Data_Object`). Similarly to its physical counterpart, the DCHO can be associated with copyright statements or licenses (`crm:E73_Information_Object` with `aat:300435434` as its type). The acquisition occurs within a time span (`crm:E52_Time-Span`) with defined starting and ending date times, and engages various agents, including individuals (`crm:E21_Person`) and institutions (`crm:E74_Group`) responsible for the activity. During the acquisition, a series of techniques (`crm:E55_Type`) can be used, such as _photogrammetry_ (`aat:300053580`) or _structured light scanning_ (`aat:300391312`), along with tools (`crmdig:D8_Digital_Device`) like _digital cameras_ (`aat:300266792`) and _structured light scanners_ (`aat:300429747`).

On the other hand, we have a series of _software activities_ (`crmdig:D10_Software_Execution`), each representing a specific stage or phase of digitisation workflow. Such stage is denoted by its type (`crm:E55_Type`), such as _processing_ (`aat:300054636`), _modelling_ (`aat:300391447`), and _optimization_ (`aat:300386427`). It involves the manipulation of the DCHO (`crmdig:D9_Data_Object`) produced previously as input and the production of a modified version of that DCHO (`crmdig:D9_Data_Object`) as output. The activity also occurs within a defined time span (`crm:E52_Time-Span`) with precise start and end date times, engages various agents, including individuals (`crm:E21_Person`) and institutions (`crm:E74_Group`), and uses software as tools to produce its output (`crmdig:D14_Software`).

## Examples of use
CHAD-AP can be used for modelling  scenarios related to cultural heritage acquisition and digitisation processes. In the following subsections we introduce some of them, and we accompany them with exemplar instantiations. 

The prefixes that are used in all the examples provided below are defined as follows:

    @prefix aat: <http://vocab.getty.edu/page/aat/> .
    @prefix ex: <https://w3id.org/dharc/ontology/chad-ap/data/example/> .
    @prefix crm: <http://www.cidoc-crm.org/cidoc-crm/> .
    @prefix crmdig: <http://www.ics.forth.gr/isl/CRMdig/> .
    @prefix lrmoo: <http://iflastandards.info/ns/lrm/lrmoo/> .
    @prefix owl: <http://www.w3.org/2002/07/owl#> .
    @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
    @prefix xml: <http://www.w3.org/XML/1998/namespace> .
    @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

### Scenario 
The creation event `32-expression-creation` created the work `32-work` and its expression `32-expression` within a time span ranging from 1500 to 1599. The creation event is carried out through the `drawing` technique and consists of an activity `32-expression-creation-01`, carried out by `ulisse-aldrovandi` (ULAN:`500342675`) as a creator of the work.

`32-work` has two titles: `32-work-title-01` with type `original-title` ("Essere umano ermafrodita"), and `32-work-title-02` with type `exhibition-title` ("Essere umano ermafrodita" and "Human hermaphrodite"). It is member of another work `tavole-di-animali-work`, whose manifestation has `print-volume` as its type. It is realised in `32-expression`.

`32-expression` is about the concept `ermafrodita`. It is embodied in the manifestation `L1-manifestation`.

`32-manifestation` has `manuscript` as its type. It is referred to by a license statement `32-manifestation-license` documented in the external document "http://rightsstatements.org/vocab/InC/1.0/". It is exemplified by `32-item`.

`32-item` is identified by three identifiers: `32-item-identifier-01` ("32") with type `collection-id`; `32-item-identifier-02` ("5") with type `volume-number`; and `32-item-identifier-03` ("Ms. Aldrovandi, Tavole di animali, vol. 5, carta 86") with type `shelf-mark`. The item is used in a curation activity `32-item-curation` carried out by `bub`. Its description reads: "Essere umano ermafrodita Human hermaphrodite (Monstrum humanum hermaphroditicum) sec. XVI 16th century BUB, Ms. Aldrovandi, Tavole di animali, vol. 5, carta 86".

```
ex:32-expression-creation a lrmoo:F28_Expression_Creation ;
    crm:P9_consists_of ex:32-expression-creation-activity-01 ;
    crm:P32_used_general_technique aat:300054196 ;
    lrmoo:R19_created_a_realisation_of ex:32-work ;
    lrmoo:R17_created ex:32-expression ;
    crm:P4_has_time-span ex:1500-1599 .

ex:32-expression-creation-activity-01 a crm:E7_Activity ;
    crm:P2_has_type aat:300404387 ;
    crm:P14_carried_out_by ex:ulisse-aldrovandi .

ex:ulisse-aldrovandi a crm:E39_Actor ;
    crm:P70i_is_documented_in <http://vocab.getty.edu/page/ulan/500342675> .

ex:1500-1599 a crm:E52_Time-Span ;
    crm:P82a_begin_of_the_begin "1500-01-01T00:00:00Z"^^xsd:dateTime ;
    crm:P82b_end_of_the_end "1599-12-31T23:59:59Z"^^xsd:dateTime .

ex:32-work a lrmoo:F1_Work ;
    crm:P102_has_title ex:32-work-title-01 ,
        ex:32-work-title-02 ;
    lrmoo:R3_is_realised_in ex:32-expression .

ex:32-work-title-01 a crm:E35_Title ;
    crm:P2_has_type aat:300417204 ;
    crm:P190_has_symbolic_content "Essere umano ermafrodita"@it .

ex:32-work-title-02 a crm:E35_Title ;
    crm:P2_has_type aat:300417207 ;
    crm:P190_has_symbolic_content "Essere umano ermafrodita"@it ,
        "Human hermaphrodite"@en .
                
ex:32-expression a lrmoo:F2_Expression ;
    crm:P129_is_about ex:ermafrodita ;
    lrmoo:R4i_is_embodied_in ex:32-manifestation .

ex:32-manifestation a lrmoo:F3_Manifestation ;
    crm:P2_has_type aat:300028569 ;
    lrmoo:R7i_is_exemplified_by ex:32-item .

ex:32-manifestation-license a crm:E73_Information_Object ;
    crm:P2_has_type aat:300435434 ;
    crm:P67_refers_to ex:32-manifestation ;
    crm:P70i_is_documented_in <http://rightsstatements.org/vocab/InC/1.0/> .

ex:tavole-di-animali-work a lrmoo:F1_Work ;
    lrmoo:R10_has_member ex:32-work ;
    lrmoo:R3_is_realised_in ex:tavole-di-animali-expression .

ex:tavole-di-animali-expression a lrmoo:F2_Expression ;
    lrmoo:R4i_is_embodied_in ex:tavole-di-animali-manifestation .

ex:tavole-di-animali-manifestation a lrmoo:F3_Manifestation ;
    crm:P2_has_type aat:300265632 ;
    lrmoo:R7i_is_exemplified_by ex:tavole-di-animali-item .

ex:tavole-di-animali-item a lrmoo:F5_Item .

ex:ermafrodita a crm:E73_Information_Object ;
    crm:P2_has_type aat:300404126 .

ex:32-item a lrmoo:F5_Item ;
    crm:P1_is_identified_by ex:32-item-identifier-01 ,
        ex:32-item-identifier-02 ,
        ex:32-item-identifier-03 ;
    crm:P3_has_note '''
        Essere umano ermafrodita 
        Human hermaphrodite (Monstrum humanum hermaphroditicum) 
        sec. XVI 
        16th century 
        BUB, 
        Ms. Aldrovandi, Tavole di animali, vol. 5, carta 86
    '''^^rdfs:Literal .

ex:32-item-identifier-01 a crm:E42_Identifier ;
    crm:P2_has_type aat:300312355 ;
    crm:P190_has_symbolic_content "32"^^rdfs:Literal .

ex:32-item-identifier-02 a crm:E42_Identifier ;
    crm:P2_has_type aat:300445021 ;
    crm:P190_has_symbolic_content "5"^^rdfs:Literal .

ex:32-item-identifier-03 a crm:E42_Identifier ;
    crm:P2_has_type aat:300404704 ;
    crm:P190_has_symbolic_content "Ms. Aldrovandi, Tavole di animali, vol. 5, carta 86"^^rdfs:Literal .

ex:32-item-curation a crm:E7_Activity ;
    crm:P2_has_type aat:300054277 ;
    crm:P16_used_specific_object ex:32-item ;
    crm:P12_occurred_in_the_presence_of ex:bub .

ex:bub a crm:E39_Actor .
```

On `2023-05-08`, `alice-bordignon` acquired digital data of `32-item` on behalf of `unibo-ficlit`, leveraging `photogrammetry` and using the `panasonic-dmc-lx100` camera, resulting in a digital model `32-model-00`.

Subsequently, on `2023-05-10`, Alice processed `32-model-00` on behalf of `unibo-ficlit` using the `3df-zephyr` software, creating a processed digital model `32-model-01`.

From `2023-05-17` to `2023-05-18`, Alice further modeled `32-model-01` on behalf of `unibo-ficlit` using the `blender` software, resulting in a refined digital model `32-model-02`.

From `2023-05-18` to `2023-05-19`, Alice optimized `32-model-02` on behalf of `unibo-ficlit` using the `instantmeshes` and `3df-zephyr` software, resulting in an optimized digital model `32-model-03`.

Finally, on `2023-05-19`, Alice exported `32-model-03` on behalf of `unibo-ficlit` using the `blender` software, resulting in the final exported model `32-model-04` as an output.

Each digital model is licensed under a CC BY-NC 4.0 license.

```
ex:unibo-ficlit a crm:E74_Group .

ex:panasonic-dmc-lx100 a crmdig:D8_Digital_Device ;
    crm:P2_has_type aat:300266792 .

ex:32-acquisition a crmdig:D2_Digitization_Process ;
    crmdig:L1_digitized ex:32-item ;
    crmdig:L11_had_output ex:32-model-00 ;
    crm:P4_has_time-span ex:32-acquisition-timespan ;
    crm:P11_had_participant ex:unibo-ficlit ;
    crm:P14_carried_out_by ex:alice-bordignon ;
    crm:P32_used_general_technique aat:300391312 ;
    crm:P16_used_specific_object ex:panasonic-dmc-lx100 .

ex:3df-zephyr a crmdig:D14_Software ;
    crm:P2_has_type aat:300426696 .

ex:32-processing a crmdig:D10_Software_Execution ;
    crm:P2_has_type aat:300054636 ;
    crmdig:L10_had_input ex:32-model-00 ;
    crmdig:L11_had_output ex:32-model-01 ;
    crm:P4_has_time-span ex:32-processing-timespan ;
    crm:P11_had_participant ex:unibo-ficlit ;
    crm:P14_carried_out_by ex:alice-bordignon ;
    crmdig:L23_used_software_or_firmware ex:3df-zephyr .

ex:blender a crmdig:D14_Software ;
    crm:P2_has_type aat:300426696 .

ex:32-modeling a crmdig:D10_Software_Execution ;
    crm:P2_has_type aat:300391447 ;
    crmdig:L10_had_input ex:32-model-01 ;
    crmdig:L11_had_output ex:32-model-02 ;
    crm:P4_has_time-span ex:32-modeling-timespan ;
    crm:P11_had_participant ex:unibo-ficlit ;
    crm:P14_carried_out_by ex:alice-bordignon ;
    crmdig:L23_used_software_or_firmware ex:blender .

ex:instantmeshes a crmdig:D14_Software ;
    crm:P2_has_type aat:300426696 .

ex:32-optimisation a crmdig:D10_Software_Execution ;
    crm:P2_has_type aat:300386427 ;
    crmdig:L10_had_input ex:32-model-02 ;
    crmdig:L11_had_output ex:32-model-03 ;
    crm:P4_has_time-span ex:32-optimisation-timespan ;
    crm:P11_had_participant ex:unibo-ficlit ;
    crm:P14_carried_out_by ex:alice-bordignon ;
    crmdig:L23_used_software_or_firmware ex:instantmeshes, ex:3df-zephyr .

ex:32-export a crmdig:D10_Software_Execution ;
    crm:P2_has_type aat:300417260 ;
    crmdig:L10_had_input ex:32-model-03 ;
    crmdig:L11_had_output ex:32-model-04 ;
    crm:P4_has_time-span ex:32-export-timespan ;
    crm:P11_had_participant ex:unibo-ficlit ;
    crm:P14_carried_out_by ex:alice-bordignon ;
    crmdig:L23_used_software_or_firmware ex:blender .

ex:alice-bordignon a crm:E21_Person .

ex:32-model-00 a crmdig:D9_Data_Object .

ex:32-model-01 a crmdig:D9_Data_Object .

ex:32-model-02 a crmdig:D9_Data_Object .

ex:32-model-03 a crmdig:D9_Data_Object .

ex:32-model-04 a crmdig:D9_Data_Object .

ex:32-model-00-license a crm:E73_Information_Object ;
    crm:P2_has_type aat:300435434 ;
    crm:P67_refers_to ex:32-model-00 ;
    crm:P70i_is_documented_in <https://creativecommons.org/licenses/by-nc/4.0/> .

ex:32-model-01-license a crm:E73_Information_Object ;
    crm:P2_has_type aat:300435434 ;
    crm:P67_refers_to ex:32-model-01 ;
    crm:P70i_is_documented_in <https://creativecommons.org/licenses/by-nc/4.0/> .

ex:32-model-02-license a crm:E73_Information_Object ;
    crm:P2_has_type aat:300435434 ;
    crm:P67_refers_to ex:32-model-02 ;
    crm:P70i_is_documented_in <https://creativecommons.org/licenses/by-nc/4.0/> .

ex:32-model-03-license a crm:E73_Information_Object ;
    crm:P2_has_type aat:300435434 ;
    crm:P67_refers_to ex:32-model-03 ;
    crm:P70i_is_documented_in <https://creativecommons.org/licenses/by-nc/4.0/> .

ex:32-model-04-license a crm:E73_Information_Object ;
    crm:P2_has_type aat:300435434 ;
    crm:P67_refers_to ex:32-model-04 ;
    crm:P70i_is_documented_in <https://creativecommons.org/licenses/by-nc/4.0/> .

ex:32-acquisition-timespan a crm:E52_Time-Span ;
    crm:P82a_begin_of_the_begin "2023-05-08T00:00:00Z"^^xsd:dateTime ;
    crm:P82b_end_of_the_end "2023-05-08T23:59:59Z"^^xsd:dateTime .

ex:32-processing-timespan a crm:E52_Time-Span ;
    crm:P82a_begin_of_the_begin "2023-05-10T00:00:00Z"^^xsd:dateTime ;
    crm:P82b_end_of_the_end "2023-05-10T23:59:59Z"^^xsd:dateTime .

ex:32-modeling-timespan a crm:E52_Time-Span ;
    crm:P82a_begin_of_the_begin "2023-05-17T00:00:00Z"^^xsd:dateTime ;
    crm:P82b_end_of_the_end "2023-05-18T23:59:59Z"^^xsd:dateTime .

ex:32-optimisation-timespan a crm:E52_Time-Span ;
    crm:P82a_begin_of_the_begin "2023-05-18T00:00:00Z"^^xsd:dateTime ;
    crm:P82b_end_of_the_end "2023-05-19T23:59:59Z"^^xsd:dateTime .

ex:32-export-timespan a crm:E52_Time-Span ;
    crm:P82a_begin_of_the_begin "2023-05-19T00:00:00Z"^^xsd:dateTime ;
    crm:P82b_end_of_the_end "2023-05-19T23:59:59Z"^^xsd:dateTime .
```

### Competency questions
CHAD-AP can be used for answering several questions related to the acquisition and digitisation of cultural heritage objects. In the following subsections we introduce some of them, and we accompany them with exemplar SPARQL queries. 

The prefixes that are used in all the SPARQL queries provided below are defined as follows:

    PREFIX aat: <http://vocab.getty.edu/page/aat/>
    PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
    PREFIX crmdig: <http://www.ics.forth.gr/isl/CRMdig/>
    PREFIX ex: <https://w3id.org/dharc/ontology/chad-ap/data/example/>
    PREFIX lrmoo: <http://iflastandards.info/ns/fr/frbr/lrmoo/>  

#### Question 1
What are the CHOs whose creation involved some author?

    SELECT ?resource ?agent
    WHERE {
        ?creation_event a lrmoo:F28_Expression_Creation ;
            lrmoo:R17_created ?resource ;
            crm:P9_consists_of ?activity .
        ?activity crm:P2_has_type aat:300054698 ;
            crm:P14_carried_out_by ?agent .
    }

#### Question 2
What are the agents and the types of  activities they carried out to contribute to the creation of `32-expression`?

    SELECT ?agent ?type
    WHERE {
        ?creation_event a lrmoo:F28_Expression_Creation ;
            lrmoo:R17_created ex:32-expression ;
            crm:P9_consists_of ?activity .
        ?activity crm:P2_has_type ?type ;
            crm:P14_carried_out_by ?agent .
    }

#### Question 3
What are the agents involved in the creation of the CHOs that have been created through the drawing technique? What are the types of the activities they carried out?

    SELECT ?resource ?agent ?type
    WHERE {
        ?creation_event a lrmoo:F28_Expression_Creation ;
            crm:P32_used_general_technique aat:300054196 ;
            lrmoo:R17_created ?resource ;
            crm:P9_consists_of ?activity .
        ?activity crm:P2_has_type ?type ;
            crm:P14_carried_out_by ?agent .
    }

#### Question 4
What are the identifiers of a manuscript? What are their types?

    SELECT ?resource ?identifier_text ?type
    WHERE {
        ?resource a lrmoo:F5_Item ;
            crm:P2_has_type aat:300028569 ;
            crm:P1_is_identified_by ?identifier .
        ?identifier crm:P2_has_type ?type ;
            crm:P190_has_symbolic_content ?identifier_text.
    }

#### Question 5
What is the shelf mark of the CHO with the project ID '32'?

    SELECT ?identifier_text
    WHERE {
        ?resource a lrmoo:F5_Item ;
        crm:P1_is_identified_by ?identifier1 ,
            ?identifier2 .
        ?identifier1 crm:P2_has_type aat:300312355 ;
            crm:P190_has_symbolic_content "32"^^rdfs:Literal .
        ?identifier2 crm:P2_has_type aat:300404704 ;
            crm:P190_has_symbolic_content ?identifier_text.
    }

#### Question 6
What are the descriptive labels of the CHOs that either have shelf marks or are prints?

    SELECT ?resource ?label
    WHERE {
        ?manifestation a lrmoo:F3_Manifestation ;
            lrmoo:R7i_is_exemplified_by ?resource ;
            crm:P2_has_type ?type .
        ?resource a lrmoo:F5_Item ;
            crm:P1_is_identified_by ?identifier ;
            crm:P3_has_note ?label .
        ?identifier crm:P2_has_type ?id_type .
        FILTER(?type = aat:300041273 || ?id_type = aat:300404704)
    }

#### Question 7
What are the CHOs whose collections have been curated by agents located in Bologna?

    SELECT ?resource ?agent
    WHERE {
        ?curation a crm:E7_Activity ;
            crm:P2_has_type aat:300054277 ;
            crm:P14_carried_out_by ?agent ;
            crm:P16_used_specific_object ?resource .
        ?agent crm:P74_has_current_or_former_residence ex:bologna .
    }

#### Question 8
What are the CHOs and the time spans of their creation events?

    SELECT ?resource ?time_interval
    WHERE {
        ?creation_event a lrmoo:F28_Expression_Creation ;
            lrmoo:R19_created_a_realisation_of ?resource ;
            crm:P4_has_time-span ?time_interval .
    }
    
#### Question 9
What are the titles of the work `32-work`? What are their types?
    
    SELECT ?title ?type ?content
    WHERE {
        ?creation a lrmoo:F28_Expression_Creation ;
            lrmoo:R19_created_a_realisation_of ex:32-work .
        ex:32-work crm:P102_has_title ?title .
        ?title crm:P2_has_type ?type ;
            crm:P190_has_symbolic_content ?content .
    }

#### Question 10
What are the parent works of the works that have 'ermafrodita' as their subject?
    
    SELECT ?parent ?work ?subject
    WHERE {
        ?creation a lrmoo:F28_Expression_Creation ;
            lrmoo:R19_created_a_realisation_of ?work ;
            lrmoo:R17_created ?expression .
        ?parent a lrmoo:F1_Work ;
            lrmoo:R10_has_member ?work .
        ?expression a lrmoo:F2_Expression ;
            crm:P129_is_about ex:ermafrodita .
    }

#### Question 11
Which license statements are assigned to the manifestations?
    
    SELECT ?manifestation ?license_link
    WHERE {
        ?license crm:P67_refers_to ?manifestation ;
            crm:P2_has_type aat:300435434 ;
            crm:P70i_is_documented_in ?license_link .
    }

#### Question 12
What is the CHO digitized and the DCHO produced by an acquisition activity? What is the latter's license?
     
    SELECT ?input ?output ?license_link
    WHERE {
        ?activity a crmdig:D2_Digitization_Process ;
            crmdig:L1_digitized ?input ;
            crmdig:L11_had_output ?output .
        ?license crm:P2_has_type aat:300435434 ;
            crm:P67_refers_to ?output ;
            crm:P70i_is_documented_in ?license_link .
    }

#### Question 13
What are the starting and ending date times in which the acquisition activity occurred?

    SELECT ?activity ?start ?end
    WHERE {
        ?activity a crmdig:D2_Digitization_Process;
            crm:P4_has_time-span ?timespan .
        ?timespan crm:P82a_begin_of_the_begin ?start ;
            crm:P82b_end_of_the_end ?end .
    }

#### Question 14
What are the acquisition activities, its output, the processing activity and its output?

    SELECT ?digitization ?input ?activity ?output
    WHERE {
        ?activity a crmdig:D10_Software_Execution ;
            crm:P2_has_type aat:300054636 ;
            crmdig:L10_had_input ?input ;
            crmdig:L11_had_output ?output .
        ?digitization crmdig:L11_had_output ?input .
    }

#### Question 15
What are the people and institutions who either carried out or were participants in the processing activity?

    SELECT ?person ?institution
    WHERE {
        ?activity a crmdig:D10_Software_Execution ;
            crm:P2_has_type aat:300054636 ;
            crm:P14_carried_out_by ?person ;
            crm:P11_had_participant ?institution .
    }

#### Question 16
What are the techniques used in acquisition activities?

    SELECT ?technique ?activity
    WHERE {
        ?activity a crmdig:D2_Digitization_Process ;
            crm:P32_used_general_technique ?technique .
    }

#### Question 17
What are the tools and their types used in processing activities?

    SELECT ?tool ?type
    WHERE {
        ?activity a crmdig:D10_Software_Execution ;
            crm:P2_has_type aat:300054636 ;
            crmdig:L23_used_software_or_firmware ?tool .
        ?tool a crmdig:D14_Software ;
            crm:P2_has_type ?type .
    }

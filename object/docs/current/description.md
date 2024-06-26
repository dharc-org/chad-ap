# Objects of Aldrovandi's exhibition

## Description
An object or cultural resource featured in Aldrovandi's exhibition is analyzed according to the Functional Requirements for Bibliographic Records (FRBR) model, which breaks down the entity into four key components:

* _Work_ (`lrmoo:F1_Work`): This represents the essence or conceptualization of the object. Each Work is associated with a series of titles (`crm:E35_Title`), which can be original titles or titles specifically used for the exhibition (`crm:E55_Type`). Furthermore, a Work may be part of a larger Work, like a series of printed volumes, which is classified under a certain type (`crm:E55_Type`).
* _Expression_ (`lrmoo:F2_Expression`): This refers to the intellectual content of the object. Expression and Work are generated through a creation event (`lrmoo:F28_Expression_Creation`) that occurs within a specific time span (`crm:E52_Time-Span`) expressed either by defined start and end dates, or by a fuzzy label if its temporal extents are not precisely known. The creation event may involve various smaller activities (`crm:E7_Activity`) conducted by one or more agents (`crm:E39_Actor`) assuming specific roles in them(`crm:E55_Type`). Additionally, creation events employ various creation techniques (`crm:E55_Type`). Expressions can also be associated with one or more subjects related to their contents (`crm:E73_Information_Object` with type `aat:300404126`).
* _Manifestation_ (`lrmoo:F3_Manifestation`): This represents the object in terms of its format. It is characterised by having a type (`crm:E55_Type`) and being referred to by copyright or licensing statements (`crm:E73_Information_Object` with type `aat:300435434`), linked with their respective licenses or statements through the property `crm:P70i_is_documented_in`. 
* _Item_ (`lrmoo:F5_Item`): This represents the physical, localised object. It is described with textual notes and identifiers (`crm:E42_Identifier`, each with its own content and type). It can depict the content (`lrmoo:F2_Expression`) of another cultural object. Sometimes, an item may be linked to a curation activity (`crm:E7_Activity` with type `aat:300054277`) carried out by a keeper (`crm:E39_Actor`) who manages a collection (`crm:E24_Physical_Human-Made_Thing` with type `aat:300025976`) to which the object belongs, located in a specific place (`crm:E53_Place`). An item can also be composed of other items. 

Whenever possible, instances of `crm:E39_Actor` and `crm:E53_Place` are linked with existing authority records through the property `crm:P48_has_preferred_identifier`.

## Object model
![Object model](diagrams\object-model.png)
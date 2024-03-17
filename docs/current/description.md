# CIDOC CRM Application Profile for Digitizing Exhibitions 

## Object level
An object or cultural resource featured in Aldrovandi's exhibition is analyzed according to the Functional Requirements for Bibliographic Records (FRBR) model, which breaks down the entity into three key components:

* Work (`frbroo:F1_Work`): This represents the essence or conceptualization of the object. It begins with a conception event (`frbroo:F27_Work_Conception`) that occurs within a specific time span (`crm:E52_Time-Span`). A time span can be expressed either by defined start and end dates, or by a fuzzy label if its temporal extents are not precisely known. Each Work is associated with a series of titles (`crm:E35_Title`), which can be original titles or titles specifically used for the exhibition (`crm:E55_Type`). Furthermore, a Work may be part of a larger Work (`frbroo:F15_Complex_Work`), like a series of printed volumes, which is classified under a certain type (`crm:E55_Type`).
* Expression (`frbroo:F2_Expression`): This refers to the intellectual content of the object. It is generated through a creation event (`frbroo:F28_Expression_Creation`), which may involve various smaller activities (`crm:E7_Activity`) conducted by one or more agents (`crm:E39_Actor`) assuming specific roles (`crm:E55_Type`). Additionally, creation events employ various creation techniques (`crm:E55_Type`). Expressions can also be associated with one or more subjects related to their contents (`crm:E73_Information_Object` with type `aat:300404126`).
* Manifestation (`frbroo:F4_Manifestation_Singleton`): This represents the physical object itself. It encompasses descriptive components like labels, types (`crm:E55_Type`), and identifiers (`crm:E42_Identifier`). In some cases, it may be linked to a curation activity (`crm:E87_Curation_Activity`) carried out by a keeper (`crm:E39_Actor`) who manages a collection (`crm:E78_Curated_Holding`) to which the object belongs, located in a specific place (`crm:E53_Place`). Manifestations can consist of other Manifestations and may depict the Expression of another related object, such as a video displaying a manuscript or a tablet showing the picture of a specimen. Additionally, Manifestations are associated with copyright or licensing statements (`crm:E73_Information_Object` with type `aat:300435434`), linked with their respective licenses or statements through the property `crm:P70i_is_documented_in`.

Whenever possible, instances of `crm:E39_Actor` and `crm:E53_Place` are linked with existing authority records through the property `crm:P48_has_preferred_identifier`.

## Process level
A 3D digitization workflow comprises two primary types of activities:
* Digitization Process (`crmdig:D2_Digitization_Process`):
    - Involves the digitization of a real-world object (`frbroo:F4_Manifestation_Singleton`).
    - Produces a digital model (`crmdig:D9_Data_Object`) representing the original physical object. The digital object can be associated with copyright statements or licenses (`crm:E73_Information_Object` with type `aat:300435434`).
    - Occurs within a defined time span (`crm:E52_Time-Span`) with a start and end date.
    - Engages various agents, including individuals (`crm:E21_Person`) and institutions (`crm:E74_Group`) responsible for the process.
    - Utilizes techniques such as photogrammetry or structured light scanning (`crm:E55_Type`) and tools like structured light scanners (e.g. Scanner Spider) (`crmdig:D8_Digital_Device`).
* Software Execution (`crmdig:D10_Software_Execution`):
    - Represents a specific stage or phase of digitization within the workflow, denoted by its type (`crm:E55_Type`) (e.g. processing, modeling, optimization, etc.).
    - Involves the manipulation of a digital object (`crmdig:D9_Data_Object`) as input.
    - Produces a digital model (`crmdig:D9_Data_Object`) as output. The digital object can be associated with copyright statements or licenses (`crm:E73_Information_Object` with type `aat:300435434`).
    - Occurs within a defined time span (`crm:E52_Time-Span`) with a start and end date.
    - Engages various agents, including individuals (`crm:E21_Person`) and institutions (`crm:E74_Group`) responsible for the execution.
    - Utilizes tools such as 3D scanning software (e.g. Artec Studio 14) (`crmdig:D14_Software`).

## Complete model
![Profile model](diagrams\profile-model.png)
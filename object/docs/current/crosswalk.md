| Spreadsheet column                     | CRM pattern                                                                                                                                                                                                                                                                                                                                                                                                                            |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **NR** (Main identifier)                               | (part of URI)<br><br>`frbroo:F4_Manifestation_Singleton`<br>----`crm:P48_has_preferred_identifier`<br>--------`crm:E42_Identifier`<br>------------`crm:P2_has_type`<br>----------------`aat:300312355`                                                                                                                                                                                                                                 |
| **Relation**                        | **part of**:<br><br>`frbroo:F4_Manifestation_Singleton`<br>----`crm:P46_is_composed_of`<br>--------`frbroo:F4_Manifestation_Singleton`<br><br>**represents**:<br><br>`frbroo:F4_Manifestation_Singleton`<br>----`crm:P62_depicts`<br>--------`frbroo:F2_Expression`                                                                                                                                                                      |
| **Descriptive label**                       | `frbroo:F4_Manifestation_Singleton`<br>----`crm:P3_has_note`<br>--------`rdfs:Literal`                                                                                                                                                                                                                                                                                                                                               |
| **Document type**           | `frbroo:F4_Manifestation_Singleton`<br>----`crm:P2_has_type`<br>--------`crm:E55_Type`                                                                                                                                                                                                                                                                                                                                                 |
| **Technique**                          | `frbroo:F28_Expression_Creation`<br>----`crm:P32_used_general_technique`<br>--------`crm:E55_Type`                                                                                                                                                                                                                                                                                                                                     |
| **In-exhibition object type** | `frbroo:F4_Manifestation_Singleton`<br>----`crm:P62_depicts`<br>--------`frbroo:F4_Manifestation_Singleton`<br>----`crm:P2_has_type`<br>--------`crm:E55_Type`                                                                                                                                                                                                                                                                         |
| **Subjects**                         | `frbroo:F2_Expression`<br>----`crm:P129_is_about`<br>--------`crm:E73_Information_Object`<br>------------`crm:P2_has_type`<br>----------------`aat:300404126`                                                                                                                                                                                                                                                                                                                                               |
| **Original title**                 | `frbroo:F1_Work`<br>----`crm:P102_has_title`<br>--------`crm:E35_Title`<br>------------`crm:P2_has_type`<br>----------------`aat:300417204`<br>------------`crm:P190_has_symbolic_content`<br><br>**Different languages**<br><br>----------------`rdfs:Literal`@ISO_639_Set-1_language_code                                                                                                                                                                                                                                                                                                                                                             |
| **Museum title**                   | `frbroo:F1_Work`<br>----`crm:P102_has_title`<br>--------`crm:E35_Title`<br>------------`crm:P2_has_type`<br>----------------`aat:300417207`                                                                                                                                                                                                                                                                                                                                            |
| **Date**                             | `frbroo:F27_Work_Conception`<br>----`crm:P4_has_time-span`<br>--------`crm:P82a_begin_of_the_begin`<br>------------`rdfs:Literal`<br>--------`crm:P82b_end_of_the_end`<br>------------`rdfs:Literal`                                                                                                                                                                                                                     |
| **Discoverer**                       | `frbroo:F28_Expression_Creation`<br>----`crm:P9_consists_of`<br>--------`crm:E7_Activity`<br>------------`crm:P14_carried_out_by`<br>----------------`crm:E39_Actor`<br>------------`crm:P2_has_type`<br>----------------`aat:300404386`                                                                                                                                                                                               |
| **Author**                           | `frbroo:F28_Expression_Creation`<br>----`crm:P9_consists_of`<br>--------`crm:E7_Activity`<br>------------`crm:P14_carried_out_by`<br>----------------`crm:E39_Actor`<br>------------`crm:P2_has_type`<br>----------------`aat:300404387`                                                                                                                                                                                               |
| **Translator**                       | `frbroo:F28_Expression_Creation`<br>----`crm:P9_consists_of`<br>--------`crm:E7_Activity`<br>------------`crm:P14_carried_out_by`<br>----------------`crm:E39_Actor`<br>------------`crm:P2_has_type`<br>----------------`aat:300069831`                                                                                                                                                                                               |
| **Draftsman**                      | `frbroo:F28_Expression_Creation`<br>----`crm:P9_consists_of`<br>--------`crm:E7_Activity`<br>------------`crm:P14_carried_out_by`<br>----------------`crm:E39_Actor`<br>------------`crm:P2_has_type`<br>----------------`aat:300054200`                                                                                                                                                                                               |
| **Engraver**                         | `frbroo:F28_Expression_Creation`<br>----`crm:P9_consists_of`<br>--------`crm:E7_Activity`<br>------------`crm:P14_carried_out_by`<br>----------------`crm:E39_Actor`<br>------------`crm:P2_has_type`<br>----------------`aat:300053225`                                                                                                                                                                                               |
| **Publisher**                          | `frbroo:F28_Expression_Creation`<br>----`crm:P9_consists_of`<br>--------`crm:E7_Activity`<br>------------`crm:P14_carried_out_by`<br>----------------`crm:E39_Actor`<br>------------`crm:P2_has_type`<br>----------------`aat:300054686`                                                                                                                                                                                               |
| **Publisher place**                    | `frbroo:F28_Expression_Creation`<br>----`crm:P9_consists_of`<br>--------`crm:E7_Activity`<br>------------`crm:P14_carried_out_by`<br>----------------`crm:E39_Actor`<br>--------------------`crm:P74_has_current_or_former_residence`<br>------------------------`crm:E53_Place`<br>------------`crm:P2_has_type`<br>----------------`aat:300054686`                                                                                   |
| **Museum preparator**              | `frbroo:F28_Expression_Creation`<br>----`crm:P9_consists_of`<br>--------`crm:E7_Activity`<br>------------`crm:P14_carried_out_by`<br>----------------`crm:E39_Actor`<br>------------`crm:P2_has_type`<br>----------------`aat:300077565`                                                                                                                                                                                               |
| **Client**                      | `frbroo:F28_Expression_Creation`<br>----`crm:P9_consists_of`<br>--------`crm:E7_Activity`<br>------------`crm:P14_carried_out_by`<br>----------------`crm:E39_Actor`<br>------------`crm:P2_has_type`<br>----------------`aat:300417639`                                                                                                                                                                                               |
| **Parent work type**          | `frbroo:F15_Complex_Work`<br>----`frbroo:R10_has_member`<br>--------`frbroo:F1_Work`<br>----`crm:P2_has_type`<br>--------`crm:E55_Type`                                                                                                                                                                                                                                                                                                |
| **Parent work title**             | `frbroo:F15_Complex_Work`<br>----`crm:P102_has_title`<br>--------`crm:E35_Title`                                                                                                                                                                                                                                                                                                                                                       |
| **Volume**                           | `frbroo:F4_Manifestation_Singleton`<br>----`crm:P48_has_preferred_identifier`<br>--------`crm:E42_Identifier`<br>------------`crm:P2_has_type`<br>----------------`aat:300445021`                                                                                                                                                                                                                                                      |
| **Collection**                       | `crm:E87_Curation_Activity`<br>----`crm:P147_curated`<br>--------`crm:E78_Curated_Holding`<br>----`crm:P12_occurred_in_the_presence_of`<br>--------`frbroo:F4_Manifestation_Singleton`                                                                                                                                                                                                                                                 |
| **Curation agent**               | `crm:E87_Curation_Activity`<br>----`crm:P147_curated`<br>--------`crm:E78_Curated_Holding`<br>----`crm:P12_occurred_in_the_presence_of`<br>--------`frbroo:F4_Manifestation_Singleton`<br>------------`crm:P49_has_former_or_current_keeper`<br>----------------`crm:E39_Actor`<br>----`crm:P14_carried_out_by`<br>--------`crm:E39_Actor`                                                                                             |
| **Curation place**              | `crm:E87_Curation_Activity`<br>----`crm:P147_curated`<br>--------`crm:E78_Curated_Holding`<br>----`crm:P12_occurred_in_the_presence_of`<br>--------`frbroo:F4_Manifestation_Singleton`<br>------------`crm:P49_has_former_or_current_keeper`<br>----------------`crm:E39_Actor`<br>----`crm:P14_carried_out_by`<br>--------`crm:E39_Actor`<br>------------`crm:P74_has_current_or_former_residence`<br>----------------`crm:E53_Place` |
| **Shelf mark**                     | `frbroo:F4_Manifestation_Singleton`<br>----`crm:P48_has_preferred_identifier`<br>--------`crm:E42_Identifier`<br>------------`crm:P2_has_type`<br>----------------`aat:300404704`                                                                                                                                                                                                                                                      |
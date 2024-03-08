# Digitization process of Aldrovandi's exhibition

## Description
A 3D digitization workflow is made up by two main types of activity:
* a **digitization process** (`crmdig:D2_Digitization_Process`);
* a series of **software executions** (`crmdig:D10_Software_Execution`).

![Digitization process](final-model-01.png)

A **digitization process** has the following characteristics:
* it involves the digitization (`crmdig:L1_digitized`) of a real-world object (`crm:E24_Physical_Human-Made_Thing`)
* it produces an output (`crmdig:L11_had_output`) that is a digital model (`crmdig:D9_Data_Object`) of the original physical object;
* it takes place (`crm:P4_has_time-span`) within a certain period of time (`crm:E52_Time-Span`), defined by a start date (`crm:P82a_begin_of_the_begin`) and a end date (`crm:P82b_end_of_the_end`);
* it involves agents - such as people (`crm:E21_Person`), who participate in such activity (`crm:P14_carried_out_by`), and intitutions (`crm:E74_Group`), which are responsible for it (`crm:P11_had_participant`);
* it also involves using techniques (such as photogrammetry or structured light scanning) (`crm:P32_used_general_technique` - `crm:E55_Type`) and tools (like structured light scanners - e.g. Scanner Spider) (`crm:P16_used_specific_object` - `crmdig:D8_Digital_Device`).

![Digitization process](final-model-02.png)

A **software execution**  has the following characteristics:
* it has a type (`crm:P2_has_type`) that reflects a certain stage or phase of digitization (`crm_E55_Type`) within the workflow (e.g. processing, modelling, optimization, etc.);
* it involves the treatment of a digital object as an input (`crmdig:L10_had_input`);
* it produces an output (`crmdig:L11_had_output`) that is a digital model (`crmdig:D9_Data_Object`);
* it takes place (`crm:P4_has_time-span`) within a certain period of time (`crm:E52_Time-Span`), defined by a start date (`crm:P82a_begin_of_the_begin`) and a end date (`crm:P82b_end_of_the_end`);
* it involves agents - such as people (`crm:E21_Person`), who participate in such activity (`crm:P14_carried_out_by`), and intitutions (`crm:E74_Group`), which are responsible for it (`crm:P11_had_participant`);
* it also involves using tools (like 3D scanning software - e.g. Artec Studio 14) (`crmdig:L23_used_software_or_firmware` - `crmdig:D14_Software`).

## Complete model
![Final model](final-model.png)
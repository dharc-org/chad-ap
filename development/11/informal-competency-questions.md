# Informal Competency Questions
## Question 1
### Identifier
CQ_11.1

### Question
Return the textual content of the appellation used to label the type of a CHO and also its authority record.

### Expected outcome
List of: `cho`, `label`, `auth`

### Result
* `22/mnf`, "Stampa", `aat:30004127`

### Based on 
Example 1

*** 

## Question 2
### Identifier 
CQ_11.2

### Question
Return all the appellations used to label the entities involved in the bibliographic description and the digitisation process of a CHO.

### Expected outcome
List of: `label`, `entity`, `type`

### Result
* "Stampa", `typ/300041273`, `Type`
* "Dioscorides Pedanius", `act/dioscorides-pedanius`, `Actor`
* "Fondo Storico Bertoloni", `col/fondo-storico-bertoloni`, `Collection`
* "Bologna", `plc/bologna`, `Place`
* "Alice Bordignon", `psn/alice-bordignon`, `Person`
* "Nikon D7200 Nikor 50mm", `dev/nikon-d7200-nikor-50mm`, `DigitalDevice`
* "Unibo Ficlit", `grp/unibo-ficlit`, `Group`
* "3df Zephyr", `sfw/3df-zephyr`, `Software`

### Based on
Example 1, 2
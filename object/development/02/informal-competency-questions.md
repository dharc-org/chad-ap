# Informal Competency Questions
## Question 1
### Identifier
CQ_2.1

### Question
Return all `identifiers` of the `cultural resources` with `type` `printed volume`, as well as their `types`.

### Expected outcome
List of triples: `cultural resource`, `identifier`, `type`

### Result
* `ALD-05-exp`, "ALD-05", `project id`
* `ALD-05-exp`, "9", `volume number`
* `ALD-05-exp`, "A.V.GG.VII.28", `shelf mark`

### Based on 
Example 2

*** 

## Question 2
### Identifier 
CQ_2.2

### Question
Return the `identifier` with `type` `shelf mark` of the `cultural resource` with an `identifier` with `type` `project id` equal to "ALD-45".

### Expected outcome
List of strings

### Result
* "Erbario Aldrovandi, vol.13, carta 77"

### Based on
Example 3

***

## Question 3
### Identifier
CQ_2.3

### Question
Return the `descriptive labels` of the `cultural resources` that either have `identifiers` with `type` `shelf mark` or have `type` `print`.

### Exprected outcome
List of tuples: `cultural resource`, `descriptive label`

### Result
* `ALD-01-exp`, "Amerigo Vespucci sveglia l’America Amerigo Vespucci awakens a sleeping America In Jan van del Straet (Stradano), Nova Reperta, c. 1589 – c.1593, Antwerp Amsterdam, Rijksmuseum"
* `ALD-05-exp`, "Aristoteles De Historia Animalium lib. 9 Venezia, Girolamo Scoto, 1545 BUB, A.V.GG.VII.28"
* `ALD-45-exp`, "Dryas octopetala L. Camedrio alpino Mountain avens Erbario Aldrovandi, vol.13, carta 77 sec. XVI 16th century  Bologna, Orto Botanico ed Erbario, Sistema Museale di Ateneo"

### Based on
Example 1, Example 2, Example 3

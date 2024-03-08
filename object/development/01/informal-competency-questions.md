# Informal Competency Questions
## Question 1
### Identifier
CQ_1.1

### Question
Return the `cultural resources` whose `creation` involved some `agent` in the role of `illustration`.

### Expected outcome
List of tuples: `cultural resource`, `agent`

### Result
* `ALD-01-exp`, `Jan van der Straet (ULAN:500011304)`
* `ALD-35-exp`, `Pietro Andrea Mattioli (VIAF:61549376)`

### Based on 
Example 1, Example 2

*** 

## Question 2
### Identifier 
CQ_1.2

### Question
Return the `agents` and the role `types` of their respective `activities` that contributed to the `creation` of `ALD-24-exp`.

### Expected outcome
List of tuples: `agent`, `type`

### Result
* `Carl Linnaeus (VIAF:34594730)`, `discovery`
* `Naturaliter`, `museum preparation`

### Based on
Example 3

***

## Question 3
### Identifier
CQ_1.3

### Question
Return the `agents` involved in the `creation` of the `cultural resources` that have been created through the technique `engraving`, as well as the role `types` of the `activities` they carried out.

### Exprected outcome
List of triples: `cultural resource`, `agent`, `type`

### Result
* `ALD-01-exp`, `Jan van der Straet (ULAN:500011304)`, `illustration`
* `ALD-01-exp`, `Philip Galle`, `engraving`
* `ALD-01-exp`, `Theodor Galle`, `engraving`
* `ALD-01-exp`, `Jan Collaert`, `engraving`
* `ALD-01-exp`, `Luigi Alamanni (ULAN:500714480)`, `commission`

### Based on
Example 1

***

## Question 4
### Identifier
CQ_1.4

### Question
Return the `cultural resources` whose `creation` involved at least one `agent` in more than one role `type`.

### Expected outcome
List of: `cultural resource`

### Result
* `ALD-S35-exp`

### Based on
Example 2
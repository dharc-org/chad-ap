# Informal Competency Questions
## Question 1
### Identifier
CQ_5.1

### Question
Return the `titles` of the `work` `ALD-L1-work` and their `types`.

### Expected outcome
List of tuples: `title`, `type`, `content`

### Result
* `ALD-L1-work-title-01`, `original-title`, "Amerigo Vespucci sveglia l'America"
* `ALD-L1-work-title-02`, `museum-title`, "Amerigo Vespucci sveglia l'America"

### Based on 
Example 1

*** 

## Question 2
### Identifier 
CQ_5.2

### Question
Return the `subjects` of the `works` that are not members of any `parent work`.

### Expected outcome
List of tuples: `work`, `subject`

### Result
* `ALD-1-work`, `sub-europa`
* `ALD-1-work`, `sub-africa`
* `ALD-1-work`, `sub-asia`
* `ALD-1-work`, `sub-mar-mediterraneo`

### Based on
Example 2

***

## Question 3
### Identifier
CQ_5.3

### Question
Return the `manifestations` of the `works` which are members of `parent works` whose types is `marine charts`.

### Exprected outcome
List of objects: `manifestation`

### Result
* `ALD-7-man`

### Based on
Example 3

***

## Question 4
### Identifier
CQ_5.4

### Question
Return the `parent works` of the `works` that have either `europa` or `tapiro` as their `subject`.

### Expected outcome
List of triples: `parent work`, `work`, `subject`

### Result
* `nova-reperta-work`, `ALD-L1-work`, `sub-tapiro`
* `atlante-nautico-work`, `ALD-7-work`, `sub-europa`

### Based on
Example 1, Example 2, Example 3

***

## Question 5
### Identifier 
CQ_5.5

### Question
Return the `manifestations` that compose another `manifestation`.

### Expected outcome
List of tuples: `manifestation1`, `manifestation2`

### Result
* `ALD-PTa-1-man`, `ALD-PTa-man`
* `ALD-PTa-2-man`, `ALD-PTa-man`

### Based on
Example 4

***

## Question 6
### Identifier 
CQ_5.6

### Question
Return the `manifestations` that depict other `expressions`.

### Expected outcome
List of tuples: `manifestation`, `expression`

### Result
* `ALD-PTa-3-man`, `ALD-PTa-exp`

### Based on
Example 4
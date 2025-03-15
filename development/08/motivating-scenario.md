# Motivating Scenario
## Name
Parent works and subjects

## Description
A `cultural resource` (which can be considered in terms of its essence (`work`), its content (`expression`) and its format (`manifestation`)), is created in a `creation event`. 

In terms of `work`, it is characterized by a `title` that identifies it. In addition, it may be the member of a `parent work`. In turn, the `parent work` is characterized by a `type`.

In terms of `expression`, it may be characterized by being about some `subjects`.

In terms of `manifestation`, it may depict the contents of another work (thus its `expression`). It also may be composed of other `manifestations`.

## Example 1
The `creation event` `L1-exp-creation` created the `work` `L1-work`, the `expression` `L1-exp` and the `manifestation` `L1-man`. 

`L1-work` has two titles: `L1-work-title-01` with type `original-title` and content "Amerigo Vespucci sveglia l'America", and `L1-work-title-02` with type `museum-title` and content "Amerigo Vespucci sveglia l'America". It is member of the `parent work` `Nova Reperta`, which has `print series` as its `type`.

`L1-exp` is about the following `subjects`: `amerigo vespucci`, `astrolabio`, `vessillo croce del sud`, `formichiere`, `bradipo`, `tapiro`, and `gruppo di cannibali`.

## Example 2
The `creation event` `1-exp-creation` created the `work` `1-work`, the `expression` `1-exp` and the `manifestation` `1-man`. 

`1-work` has two titles: `1-work-title-01` with type `original-title` and content "Carta nautica", and `1-work-title-02` with type `museum-title` and content "Carta nautica".

`1-exp` is about the following `subjects`: `sub-europa`, `sub-africa`, `sub-asia`, and `sub-mar-mediterraneo`.

## Example 3
The `creation event` `7-exp-creation` created the `work` `7-work`, the `expression` `7-exp` and the `manifestation` `7-man`. 

`7-work` has two titles: `7-work-title-01` with type `original-title` and content "Profilo incompleto delle coste del continente americano", and `7-work-title-02` with type `museum-title` and content "Profilo incompleto delle coste del continente americano". It is member of the `parent work` `Atlante Nautico`, which has `marine chart` as its `type`.

`L1-exp` is about the following `subjects`: `sub-america` and `sub-europa`.

## Example 4
The `creation event` `PTa-exp-creation` created the `work` `PTa-work`, the `expression` `PTa-exp` and the `manifestation` `PTa-man`. 

The `creation event` `PTa-1-exp-creation` created the `work` `PTa-1-work`, the `expression` `PTa-1-exp` and the `manifestation` `PTa-1-man`. 

The `creation event` `PTa-2-exp-creation` created the `work` `PTa-2-work`, the `expression` `PTa-2-exp` and the `manifestation` `PTa-2-man`. 

The `creation event` `PTa-3-exp-creation` created the `work` `PTa-3-work`, the `expression` `PTa-3-exp` and the `manifestation` `PTa-3-man`. 

`PTa-man` is composed of `PTa-1-man` and `PTa-2-man`. `PTa-3-man` depicts `PTa-exp`.

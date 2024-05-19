# Motivating Scenario
## Name
Re-engineering object levels

## Description
A `cultural resource` can be considered in terms of its essence (`work`), its content (`expression`), its format (`manifestation`) and its physical localization (`item`). 

The work has a number of `titles`, each with a `type` (e.g. original title, exhibition title, etc.) and a `content`. The work itself can have a `type` as well. Moreover, it can be composed of other works.

The expression is created by a `expression creation event` along with the work. An expression embodies one or more manifestations and can be about some `concepts`.
The expression creation event is carried out in a `time span` that can be expressed through either a fuzzy temporal label or a start and an end date.

The manifestation has a type and is referred to by a `licensing statement` documented in an external `document`. Finally, it is exemplified by a item.

A item is described with natural language descriptions. It can be composed of other physical objects. It is identified by a series of `identifiers`, each with its own type. It can depict the content of another cultural object (its expression). Finally, an item is used in a curation `activity`, as part of a `collection`, carried out by some `actor`.


## Example 1
The creation event `32-expression-creation` created the work `32-work` and the expression `32-expression` within a time span ranging from 1500 to 1599. 

`32-work` has two titles: `32-work-title-01` with type `original-title` ("Essere umano ermafrodita"), and `32-work-title-02` with type `exhibition-title` ("Essere umano ermafrodita" and "Human hermaphrodite"). It is member of another work `tavole-di-animali-work`, whose manifestation has `print-volume` as its type. It is realised in `32-expression`.

`32-expression` is about the concept `ermafrodita`. It embodies the manifestation `L1-manifestation`.

`32-manifestation` has `manuscript` as its type. It is referred to by a license statement `in-copyright` documented in the external document "http://rightsstatements.org/vocab/InC/1.0/". It is exemplified by `32-item`.

`32-item` is identified by three identifiers: `32-item-identifier-01` ("32") with type `collection-id`; `32-item-identifier-02` ("5") with type `volume-number`; and `32-item-identifier-03` ("Ms. Aldrovandi, Tavole di animali, vol. 5, carta 86") with type `shelf-mark`. The item is used in a curation activity `32-item-curation` carried out by `bub`. Its description reads: "Essere umano ermafrodita Human hermaphrodite (Monstrum humanum hermaphroditicum) sec. XVI 16th century BUB, Ms. Aldrovandi, Tavole di animali, vol. 5, carta 86".
---
title: "CIDOC CRM profile for digitization of temporary exhibitions"
---

# SPOKE 4 Application Profile

## Introduction
This is a CIDOC CRM based Application Profile consisting in a set of entities and properties for representing the digitization workflow of an exhibition in a machine-readable format.

The Profile was developed and refined while working on the Aldrovandi case study [1](https://doi.org/10.1016/j.daach.2023.e00309). It includes ontological constructs to formalize the data and metadata of the objects contained in the exhibition and the various activities that make up the digitization workflow.

It was developed by leveraging the Simplified Agile Methodology for Ontology Development (SAMOD)[2](http://dx.doi.org/10.6084/m9.figshare.3189769).

## Description
This repository contains the full documentation produced during the development of the Application Profile. In particular:
* the `docs` folder contains the documentation about the current state of the model and some examples;
* the `object` folder contains the full documentation of the module specific to modelling the exhibition objects starting from their bibliographical metadata;
* the `process` folder contains the full documentation of the module specific to modelling the digitization workflow of the exhibition.

In turn, both the `object` and the `process` folder are organized as follows:
* the `data` directory contains the full set of refactored ABoxes, one for each iteration, written in the Turtle RDF serialization;
* the `development` directory contains a folder per development iteration, each containing a full test case with:
    - a `motivating scenario`, which defines the scope of the single iteration, along with some examples;
    - a list of `informal Competency Questions`, written in natural language;
    - a `glossary of terms`, which defines a set of meaningful words and expressions - representing possible entities and relationships - collected from the scenario and the competency questions;
    - a `visual diagram` of the entites and relationships recorded in the glossary, rendered in .png format and coupled with the .graphml file it has been exported from;
    - a `terminology component (TBox)`, which defines a formal schema based on the diagram;
    - an `assertion component (ABox)`, which organizes the examples data according to the schema;
    - a list of `formal Competency Questions`, which reformulate the informal competency questions into proper SPARQL queries;
    - a `testing notebook`, which is used to test the SPARQL queries against both the TBox and the ABox;
the `diagrams` directory contains the full set of Graffoo diagrams representing the refactored model of each iteration;
the `docs` directory contains the full set of files related to the final model and its versions in time;
the `sparql` directory contains the full set of refactored Formal Competency Questions.
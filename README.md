---
Title: "Cultural Heritage Acquisition and Digitisation Application Profile (CHAD-AP)"
Release: 2024-04-16
Latest version: https://w3id.org/dharc/ontology/chad-ap
Revision: 2.0.1
Issued on: 2024-04-16
Authors: Barzaghi, Sebastian; Peroni, Silvio
Contributors: Heibi, Ivan; Moretti, Arianna
Available formats: JSON-LD, RDF/XML, N-Triples, Turtle
DOI: https://doi.org/10.5281/zenodo.15391304
License: http://creativecommons.org/licenses/by/4.0/
Cite as: Barzaghi, S., Heibi, I., Moretti, A., Peroni, S. (2025). Developing Application Profiles for Enhancing Data and Workflows in Cultural Heritage Digitisation Processes. In "Demartini, G., et al. The Semantic Web – ISWC 2024". ISWC 2024. Lecture Notes in Computer Science, vol 15233. Springer, Cham. https://doi.org/10.1007/978-3-031-77847-6_11.
---

# CHAD-AP

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15391304.svg)](https://doi.org/10.5281/zenodo.15391304)

## Introduction
The _Cultural Heritage Acquisition and Digitisation Application Profile_ (CHAD-AP) is a OWL 2 DL-based metadata application profile of CIDOC CRM for describing cultural heritage digitisation data and processes in a FAIR-compliant and machine-readable format.

CHAD-AP was developed and refined while working on the [Aldrovandi case study](https://doi.org/10.1016/j.daach.2023.e00309). It includes ontological constructs to formalize the data and metadata of the objects contained in the exhibition and the various activities that make up the digitisation workflow.

It was developed by leveraging the [Simplified Agile Methodology for Ontology Development](http://dx.doi.org/10.6084/m9.figshare.3189769) (SAMOD).

## Description
This repository contains the full documentation produced during the development of CHAD-AP. In particular:
* the `data` directory contains the full set of refactored ABoxes, one for each iteration, written in the Turtle RDF serialisation;
* the `development` directory contains a folder per development iteration, each containing a full test case with:
    - a `motivating scenario`, which defines the scope of the single iteration, along with some examples;
    - a list of `informal Competency Questions`, written in natural language;
    - a `glossary of terms`, which defines a set of meaningful words and expressions - representing possible entities and relationships - collected from the scenario and the competency questions;
    - a `visual diagram` of the entites and relationships recorded in the glossary, rendered in .png format and coupled with the .graphml file it has been exported from;
    - a `terminology component (TBox)`, which defines a formal schema based on the diagram;
    - an `assertion component (ABox)`, which organizes the examples data according to the schema;
    - a list of `formal Competency Questions`, which reformulate the informal competency questions into proper SPARQL queries;
    - a `testing notebook`, which is used to test the SPARQL queries against both the TBox and the ABox;
* the `diagrams` directory contains the full set of Graffoo diagrams representing the refactored model of each iteration;
* the `docs` directory contains the full set of files related to the final model and its versions in time;
* the `sparql` directory contains the full set of refactored Formal Competency Questions, along with their respective testing notebooks.
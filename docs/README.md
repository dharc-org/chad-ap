# Main documentation
The directory contains all the files related to the model, its versions in time, and the related documentation. In particular, it includes:

* the current `directory`, where the files of the current version of the model are stored;
* one ore more `MAJOR.MINOR.PATCH` version directory for each of the versions of the model developed;

The current directory contains a `.owl` file named after the lowercase ontology acronym, which is the source of the ontology in a particular format between RDF/XML, Turtle, N-triples, or JSON-LD. In addition to this file, the directory includes other files, named in the same way and with the following extensions: `.ttl` (Turtle), `.nt` (N-Triple), `.jsonld` (JSON-LD), `.html` (HTML, i.e. the human readable documentation of the ontology).

The version directories contain the same kinds of files as those included in the current directory, but specific for that particular version.

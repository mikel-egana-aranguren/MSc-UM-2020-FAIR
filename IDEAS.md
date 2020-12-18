# Posibles ideas

## General

* Mirar bien los links, papers, etc

## Intro

* Explicar quien soy
* Explicar como encontrar el material
* Explicar bien todo lo que tienen en el repo GitHub: papers etc

## Contenido

* FAIR es sobre datos y metadatos: (meta)data
* Estamos usando Linked Data en dos niveles: para datos y metadatos
* RDFLib: SHACL, TARQL
* CSV2RDF.py: linea a linea
* Metadatos: distribuciones, licencia, ... cada triple
* URI Named Graph metida a mano: Añadir uri graph a archivo nt
* blazegraph: por que usamos un namespace (repo) de tipo quad?
* que archivos hay que subir a blazegraph?
* fijarse que en RDF, datos y metadatos juntos
* hacer la misma consulta antes y despues de subir metadatos, fijarse en el grafo de genes y explorar (Queries DESCRIBE o tab explore)
* Como he deducido la URL http://localhost:9999/blazegraph/namespace/um/sparql? Mirando el network en firefox (Aunque lo mejor seria usar la documentacion).
* Si hago un CURL (CURL http://localhost:9999/blazegraph/namespace/um/sparql), me da contenido siguiendo SPARQL Service Description: es semantico, un agente lo puede usar!
* Trifid navegador, agente (cURL)
* Trifid Seguir enlaces
* El agente, al tener un enlace explicito DCAT, es capaz de saber que hay un CSV al final del enlace

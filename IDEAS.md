# Posibles ideas

## Intro

* explicar bien todo lo que tienen en el repo GitHub: papers etc
* vamos a dar ejemplos concretos de implementacion, pero recordar siempre que FAIR no es sobre implementacion! desgranar ambas facetas
* FAIR es tanto sobre datos como metadatos, sabeis la diferencia?

## FAIR

Freely implementable protocol: poner lista de protocolos y preguntar

## FAIRificar

RDFLib: SHACL, TARQL (Ontorefine)
CSV2RDF.py: linea a linea
LOV SIO: protege
Metadatos: distribuciones, licencia, ...

URI Named Graph metida a mano: Añadir uri graph a archivo nt https://um.es/graph/genes

hacer un diagrama que simplifique todo: csv, apache, ...

blazegraph: por que usamos un namespace (repo) de tipo quad?

que archivos hay que subir a blazegraph?

fijarse que en RDF, datos y metadatos juntos

hacer la misma consulta antes y despues de subir metadatos, fijarse en el grafo de genes y explorar (Queries DESCRIBE o tab explore)

Como he deducido la URL http://localhost:9999/blazegraph/namespace/um/sparql? Mirando el network en firefox (Aunque lo mejor seria usar la documentacion). 

Si hago un CURL (CURL http://localhost:9999/blazegraph/namespace/um/sparql), me da contenido siguiendo SPARQL Service Description: es semantico, un agente lo puede usar!

Dominio um.es

Trifid navegador
Trifid Agente: CURL

Seguir enlaces

Fijarse que el agente, al tener un enlace explicito DCAT, es capaz de saber que hay un CSV al final del enlace!

Si sobra tiempo, que empiecen a hacer trabajo:

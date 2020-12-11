# Posibles ideas

## Intro

* explicar bien todo lo que tienen en el repo GitHub: papers etc
* vamos a dar ejemplos concretos de implementacion, pero recordar siempre que FAIR no es sobre implementacion! desgranar ambas facetas
* FAIR es tanto sobre datos como metadatos, sabeis la diferencia?

## FAIR

Freely implementable protocol: poner lista de protocolos y preguntar

Hay dos grandes areas para trabajar FAIR:
* Tecnica: Linked Data etc
* Contenido: ontologias, metadatos, etc

## Linked Data

Adaptar slides de material anterior

FAIRificar (https://www.go-fair.org/fair-principles/fairification-process/): empezar por un CSV y hacer todos los pasos hasta Linked Data FAIR: Crear URIs, anotar con ontologias (elegir!), convertir a RDF, enlazar, añadir metadatos, añadir licencia, 

Meter metadatos con named graphs (estandar W3C named graphs), foaf:primaryTopic

Meter tambien el archivo original CSV en servidor web (enlace simbolico), y enlace con DCAT, como en https://peerj.com/articles/cs-110/#, hacer un diagrama que simplifique todo

DCAT, PROV, VOID

SHACL + librdf de los datos

Trifid: Conneg diferente pero da igual, lo importante es que es para maquinas

Como he deducido la URL http://localhost:9999/blazegraph/namespace/kb/sparql? Mirando el network en firefox (Aunque lo mejor seria usar la documentacion). Si hago un CURL, me da contenido siguiendo SPARQL Service Description (http://www.w3.org/TR/2013/REC-sparql11-service-description-20130321): es semantico, un agente lo puede usar! Comentar tambien SPARQL protocol

http://ma-graph.org/





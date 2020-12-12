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




FAIRificar (https://www.go-fair.org/fair-principles/fairification-process/): empezar por un CSV y hacer todos los pasos hasta Linked Data FAIR: Crear URIs, anotar con ontologias (elegir!), convertir a RDF, enlazar, añadir metadatos, añadir licencia, 

Meter metadatos con named graphs (estandar W3C named graphs), foaf:primaryTopic

Meter tambien el archivo original CSV en servidor web (enlace simbolico), y enlace con DCAT, como en https://peerj.com/articles/cs-110/#, hacer un diagrama que simplifique todo

DCAT, PROV, VOID

https://www.w3.org/TR/vocab-dcat-2
https://www.w3.org/TR/prov-overview/
https://www.w3.org/TR/void/

SHACL + librdf de los datos

Trifid: Conneg diferente pero da igual, lo importante es que es para maquinas

Como he deducido la URL http://localhost:9999/blazegraph/namespace/kb/sparql? Mirando el network en firefox (Aunque lo mejor seria usar la documentacion). Si hago un CURL, me da contenido siguiendo SPARQL Service Description (http://www.w3.org/TR/2013/REC-sparql11-service-description-20130321): es semantico, un agente lo puede usar! Comentar tambien SPARQL protocol

https://www.w3.org/TR/sparql11-protocol/
https://www.w3.org/TR/2013/REC-sparql11-service-description-20130321/




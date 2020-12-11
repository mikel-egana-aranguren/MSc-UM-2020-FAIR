# CSV to RDF

`pip install rdflib`

Convertir un CSV a FAIR, miro un recurso FAIR: UniProt

http://purl.uniprot.org/core

http://purl.uniprot.org/core/organism

Al convertir el CSV a RDF ya lo hacemos vamos haciendo FAIR, e.g. URIs, añadir enlace a 9606 ... 

Convertir CSV a NT luego añadir un grafo, para añaidr metadatos!

Consultas:

```sparql
SELECT DISTINCT ?g 
WHERE {
    GRAPH ?g {?s ?p ?o}
}
```

```sparql
SELECT *
WHERE {
    GRAPH ?g {?s ?p ?o}
}
```

http://localhost:8080/data/LDD012546



Archivo ttl con metadatos DCAT

service apache2 restart

cp GenesUM.csv /var/www/html/

conneg agente contra DCAT

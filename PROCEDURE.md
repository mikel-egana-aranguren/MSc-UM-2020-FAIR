# CSV to RDF



 






 

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

Explicar DCAT

Meter OWL propio

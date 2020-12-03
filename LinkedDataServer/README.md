# Linked Data Server

## Standalone trifid with default data (file)

Exec trifid: `./server.js --config=config.json`

Conneg:

* Turtle: `curl --header "Accept: text/turtle" http://localhost:8080/data/person/leonard-hofstadter`
* JSON-LD: `curl --header "Accept: application/ld+json" http://localhost:8080/data/person/leonard-hofstadter`

## Connect Trifid to Blazegraph through SPARQL service description

Exec blazegraph (`run.sh`): `java -server -Xmx4g -jar blazegraph.jar`

Load data from `trifid/node_modules/tbbt-ld/dist/tbbt.nq`

Exec trifid: `./server.js --config=../blazegraph-config.json`

Go to http://localhost:8080/data/mikel

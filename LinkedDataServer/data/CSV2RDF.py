#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://github.com/SemanticLab/simple-csv-to-rdf

import csv
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, RDF, RDFS, SKOS, XSD

input_file = csv.DictReader(open("GenesUM.csv"))

# Crear un objeto Grafo 
output_graph = Graph()

# URIs base comunes
base_uri = 'https://um.es/data/'

# Objetos comunes
taxon_human = 'http://purl.uniprot.org/taxonomy/9606'

# Propiedades comunes
organism = 'http://purl.uniprot.org/core/organism' 

for row in input_file:

	# Triple con literal
	output_graph.add((URIRef(base_uri + row['Id']), RDFS.label, Literal(row['Nombre'], lang='en')) )

	# Triple con recurso
	# TODO: Logica humano/persona
	output_graph.add((URIRef(base_uri + row['Id']), URIRef(organism), URIRef(base_uri +row['Tx'])) )	

output_graph.serialize(destination='GenesUM.ttl', format='ttl')

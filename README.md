# pangenomeMetagenomicsNormalizer
i just coded another function an the meaning is that most of the metagenomics pipelines gives the gene ontology and the presence absence but nothing more than that. So i coded this that takes a presence absence file and then sum the presence absence across the species and then divide it with the number of the gene ontology plus child categories included and presents you a ratio. The higher the ratio means that the ontology is distributed well across all the species. 

```
pangenomeMetagenomicsNormalize("/Users/gauravsablok/Desktop/CodeCheck/csv_test_datasets/Pangenome.csv")
	go_category	effectsize
0	atp-dependent clp atp-binding subunit	34.50
1	dna a subunit	13.29
2	dna gyrase subunit b	11.50
3	phospho-2-dehydro-3-deoxyheptonate aldolase	17.40
4	6-phospho-beta-glucosidase	27.33
...	...	...
1656	nucleotidyltransferase domain	1.00
1657	sodium-dependent phosphate transporter	0.10
1658	adenine-specific dna-methyltransferase ed	0.25
```
Gaurav \
Academic Staff Member \
Bioinformatics \
Institute for Biochemistry and Biology \
University of Potsdam \
Potsdam,Germany 

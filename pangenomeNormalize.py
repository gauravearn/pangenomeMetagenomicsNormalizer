def pangenomeMetagenomicsNormalize(pangenome_file):
    """
    a pangenome metagenomics normalizer, given a
    gene ontology based presence and absence and
    a species file, it first summarizes the count
    across the species and then takes the count
    of the gene ontologies and present a ratio 
    The higher the ratio the more presence of 
    that ontology across the species. 
    """
    pangenome = pangenome_file
    read_pangenome = pd.read_csv(pangenome, sep = ",")
    drop_pangenome = read_pangenome.dropna()
    total_presence_absence = drop_pangenome.iloc[::,3:].sum(axis = 1).to_list()
    total_go_count = drop_pangenome.iloc[::,[0,1]]["go"].\
                                   apply(lambda n: len(n.split(";"))).to_list()
    drop_pangenome_names = drop_pangenome.iloc[::,0].to_list()                            
    drop_pangenome_normalization = [round((i/j),2) for i, j in\
                                       zip(total_presence_absence, total_go_count)]
    final_pangenome = pd.DataFrame([(i,j) for i,j in \
                                zip(drop_pangenome_names,drop_pangenome_normalization)]).\
                                       rename(columns = {0: "go_category",\
                                                              1: "effectsize"})
    return final_pangenome

                                  

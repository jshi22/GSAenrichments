
class BACKGROUND:
    def __init__(self, gene_set, filename=None):
        self._background_genes=[]

        if filename==None:
            self._background_genes=list(gene_set)
        else:
            matfile = open(filename)
            for line in matfile:
                tok = line.strip().split('\t')
                self._background_genes.append(tok[0])
    @property
    def background_genes(self):
        return self._background_genes

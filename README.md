## GEMINI
GEMINI is a **ge**nome **mini**ng tool, which detects regions of atypical nucleotide composition. It delineates compositional core (native) and accessory (alien) genome.

### Usage
```
python gemini.py genome.gbk output.txt
```
### Input
GEMINI takes following two command-line arguments
1. Genome file in GenBank(full) format.
2. Name of Output file

### Output
GEMINI outputs a space separated file with six columns.

Column 1- GI-> Genomic island id

Column 2- Start-> Start co-ordinate of genomic island

Column 3- End-> End co-ordinate of genomic island

Column 4- Length-> Length of the genomic island

Column 5- Mosaic-> If a genomic island is mosaic (i.e. composed of more than one cluster) it is shown as 'M'.

Column 6- #genes-> Number of genes harbored on genomic island

### Reference
Jani, Mehul, Kalai Mathee, and Rajeev K. Azad. "Identification of novel genomic islands in Liverpool epidemic strain of Pseudomonas aeruginosa using segmentation and clustering." Frontiers in microbiology 7 (2016).

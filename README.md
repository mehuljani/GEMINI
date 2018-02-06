## GEMINI
GEMINI is a **ge**nome **mini**ng tool, which detects regions of atypical nucleotide composition. It delineates compositional core (native) and accessory (alien) genome.

### Usage
First set the permissions for the files
```
sudo chmod 775 gemini
sudo chmod 775 gemini.out
```
Program can now be run as
```
./gemini [options] genome.gbk output.txt
```

### Add to Path
Add the following line to your $HOME/.bashrc file to make it available to all users:
```
export PATH=$PATH:'Path/to/GEMINI'
```
GEMINI can now be used from any folder as
```
gemini [options] genome.gbk output.txt
```

### Input
##### Required input
GEMINI takes following two command-line arguments
1. Genome file in GenBank(full) format.
2. Name of Output file
##### Optional input
Following options can be used with the program

  -h, --help          shows help message and exit
  
  -cite               shows publication reference and exit
  
  -info               shows information about program and exit
  
  -debug              Keeps Temporary files
  
  -verbose            Prints on screen
  
  -seg SEG            Provide segmentation threshold in range 0-1
  
  -clus1 CLUS1        Provide contiguous clustering threshold in range 0-1
  
  -clus2 CLUS2        Provide non-contiguous clustering threshold in range 0-1


### Output
GEMINI outputs a space separated file with six columns.

Column 1- GI-> Genomic island id

Column 2- Start-> Start co-ordinate of genomic island

Column 3- End-> End co-ordinate of genomic island

Column 4- Length-> Length of the genomic island

Column 5- Mosaic-> If a genomic island is mosaic (i.e. composed of more than one cluster) it is shown as 'M'.

Column 6- #genes-> Number of genes harbored on genomic island

### Example
```
./gemini -debug -verbose -seg 0.999999999 -clus1 0.999999999999 -clus2 0.999999999999 example.gbk example_output.txt
```

### Reference
[GEMINI](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4971588/pdf/fmicb-07-01210.pdf)

Jani, Mehul, Kalai Mathee, and Rajeev K. Azad. "Identification of novel genomic islands in Liverpool epidemic strain of Pseudomonas aeruginosa using segmentation and clustering." Frontiers in microbiology 7 (2016).

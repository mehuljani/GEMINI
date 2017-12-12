#!/usr/bin/python

import sys
import os
import heapq
from Bio import SeqIO

f=sys.argv[1]

try:
	f=open(sys.argv[1], "r")
except:
	print "File does not exist"
	sys.exit()

output=open(sys.argv[2], 'w')

outname=sys.argv[1]+'_GEMINI'
out=open(outname, 'w')

start_col, end_col, rna_start, rna_end=[],[],[],[]

for gb_record in SeqIO.parse(f, "genbank"):
	out.write("%s" % (gb_record.seq))
	seq=gb_record.seq
	for feature in gb_record.features:
		if feature.type == "CDS":
			location1=feature.location
			start=location1.start
			end=location1.end
			start_col.append(start)
			end_col.append(end)
		if feature.type == "rRNA":
			location1=feature.location
			start=location1.start
			end=location1.end
			rna_start.append(start)
			rna_end.append(end)		


length=len(seq)
#print "length is", str(length)
os.system("./gemini.out %s" %outname)

f=open("temp", "r")
col1, col2, col3=[],[],[]
for line in f:
	line=line.strip()
	a=int(line.split('\t')[0])
	b=int(line.split('\t')[1])
	c=int(line.split('\t')[2])
	col1.append(a)
	col2.append(b)
	col3.append(c)

size=[0]*(max(col3)+1)
distribution=[0]*(max(col3)+1)
for clusterid in range(1,max(col3)+1):
	aa, totaa=0, 0
	for i in range (len(col3)):
		if i == 0:
			if (col3[i]==clusterid):
				totaa+=1
				if col3[i+1]==clusterid:
					aa+=1
		elif i == (len (col3)-1):
			if (col3[i]==clusterid):
				totaa+=1
				if col3[i-1]==clusterid:
					aa+=1
		else:
			if (col3[i]==clusterid):
				totaa+=1
				if col3[i+1]==clusterid or col3[i-1] == clusterid:
					aa+=1
		if col3[i] == clusterid:
			size[clusterid]+=(col2[i]-col1[i])
			
	distribution[clusterid]=aa/float(totaa)
	#print clusterid, totaa, aa, aa/float(totaa), size[clusterid]/float(length)


max_clus=heapq.nlargest(3, xrange(len(size)), size.__getitem__) #Return index of three largest values

nat_clus=size.index(max(size))

#print max_clus
maxd=1

for clusters in max_clus:
	if distribution[clusters]<maxd:
		maxd=distribution[clusters]
		sec_nat=clusters

if size[sec_nat]>=20:
	#print "native cluster are", str(nat_clus), "and", str(sec_nat)
	for i in range(len(col3)):
		if col3[i]==sec_nat:
			col3[i]=nat_clus

cond1,cond2,cond3=[],[],[]	
for i in range (len(col3)-1):
	#print col1[i], col2[i], col3[i]
	if (col3[i] == nat_clus):
		if (col3[i]==col3[i+1]):
			col1[i+1]=col1[i]
		else:
			cond1.append(col1[i])
			cond2.append(col2[i])
			cond3.append(col3[i])
			if i == (len(col3)-2):
				cond1.append(col1[i+1])
				cond2.append(col2[i+1])
				cond3.append(col3[i+1])


	else:
		if (col3[i]==col3[i+1]):
			col1[i+1]=col1[i]
		elif (col3[i+1]!=nat_clus):
			col1[i+1]=col1[i]
			col3[i+1]='M' #Mosaic			

		else:
			cond1.append(col1[i])
			cond2.append(col2[i])
			cond3.append(col3[i])
			if i == (len(col3)-2):
				cond1.append(col1[i+1])
				cond2.append(col2[i+1])
				cond3.append(col3[i+1])

all_atyp_start, all_atyp_end, all_atyp_clus=[],[],[]
put_gi_s, put_gi_e, put_gi_c, put_gi_g=[],[],[],[]

for i in range (len(cond1)):
	if cond3[i]!=nat_clus:
		all_atyp_start.append(cond1[i])
		all_atyp_end.append(cond2[i])
		all_atyp_clus.append(cond3[i])

for i in range (len(all_atyp_start)):
	gene_counter=0
	for j in range (len(start_col)):
		if ((all_atyp_start[i]-50)<=start_col[j] and (all_atyp_end[i]+50)>=end_col[j]):
			gene_counter+=1
			#print all_atyp_start[i], all_atyp_end[i], start_col[j], end_col[j]
	if gene_counter>=8 :
		put_gi_s.append(all_atyp_start[i])
		put_gi_e.append(all_atyp_end[i])
		put_gi_c.append(all_atyp_clus[i])
		put_gi_g.append(gene_counter)		
		#print all_atyp_start[i], all_atyp_end[i], all_atyp_clus[i], gene_counter


#print (("GI\tstart\tend\tlength\tMosaic\tno. of genes") file=output)
print >>output, "GI start end length Mosaic #genes"
counter=0

for i in range (len(put_gi_s)):
	for j in range (len(rna_start)):
		if ((put_gi_s[i]-50)<=rna_start[j] and (put_gi_e[i]+50)>=rna_end[j]):
			break
	else:
		if put_gi_c[i] is not 'M':
			put_gi_c[i]='-'
		counter+=1
		#print (("%i\t%i\t%i\t%i\t%i\t%s\t%i" %(counter, put_gi_s[i], put_gi_e[i], put_gi_e[i], put_gi_s[i], put_gi_c[i], put_gi_g[i])), file=output)
		print >>output, counter, put_gi_s[i], put_gi_e[i], put_gi_e[i]-put_gi_s[i], put_gi_c[i], put_gi_g[i]

os.system("rm %s" %outname)
os.system("rm temp")






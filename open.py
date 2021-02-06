import pandas as pd

x = True
geneList = []
#holds user inputted genes
while (x):
    gene = input("Input a differently expressed gene. Type 'n' when you are finished. : ")
    if gene=='n':
        x= False
    else:
        geneList.append(gene)

genes1 = pd.read_csv(r'C:\Users\Shriya\Downloads\Book1.csv', usecols=['Genes']).T.values.tolist()[0]
#genes1 stores the genes in the heatmap
#print(genes1)

genes2 = {}
#genes2 will hold the genes that the user input and are also in the first heatmap and holds how many rows to skip when reading csv file
genes3 = []
#genes3 holds the names of the genes that are in heatmap and user input again. Genes 3 will be modified though
for x in geneList:
    for y in genes1:
        if x==y:
            genes2[x]=genes1.index(x)
            genes3.append(x)


Geld =  pd.read_csv(r'C:\Users\Shriya\Downloads\Book1.csv', usecols=['Geldanamycin']).T.values.tolist()[0]

GeldScore=0
a=0
while a<len(genes3):
    if Geld[genes2.get(genes3[a])] == "X":
        GeldScore = GeldScore + 1
        genes3.remove(genes3[a])
    else:
        a=a+1

CGP =  pd.read_csv(r'C:\Users\Shriya\Downloads\Book1.csv', usecols=['CGP-60474']).T.values.tolist()[0]
CGPScore=0

b=0
while b<len(genes3):
    if CGP[genes2.get(genes3[b])] == "X":
        CGPScore = CGPScore + 1
        genes3.remove(genes3[b])
    else:
        b=b+1

Cel =  pd.read_csv(r'C:\Users\Shriya\Downloads\Book1.csv', usecols=['Celastrol']).T.values.tolist()[0]
CelScore=0

c=0
while c<len(genes3):
    if Cel[genes2.get(genes3[c])] == "X":
        CelScore = CelScore + 1
        genes3.remove(genes3[c])
    else:
        c=c+1

recDrug = ""


if GeldScore>0:
    recDrug+= "Geldanamycin, "

if CGPScore>0:
    recDrug+= "CGP-60474, "

if CelScore>0:
    recDrug+= "Celastrol, "
if recDrug != "":
    print(recDrug + " is recommended to downregulate/upregulate the following genes: ")
for key in genes2:
    print(key)


genes4 = pd.read_csv(r'C:\Users\Shriya\Downloads\COVID_BALF_Mild_vs_Healthy.csv', usecols=['Genes']).T.values.tolist()[0]

genes41 = []
#This will hold genes that are in genes4 and in userinput
for d in geneList:
    for e in genes4:
        if d==e:
            genes41.append(d)

if len(genes41)>0:
    print ("The patient is suffering from a mild case of COVID. The following genes are correlated with COVID according to our data.")
    for gene in genes41:
        print(gene)

genes5 = pd.read_csv(r'C:\Users\Shriya\Downloads\COVID_BALF_SEVERE.csv', usecols=['Genes']).T.values.tolist()[0]

genes51 = []
#This will hold genes that are in genes5 and in userinput
for f in geneList:
    for g in genes5:
        if f==g:
            genes51.append(f)

if len(genes51) > 0:
    print(
        "The patient is suffering from a severe case of COVID. The following genes are correlated with COVID according to our data.")
    for gene in genes51:
        print(gene)

genes6 = pd.read_csv(r'C:\Users\Shriya\Downloads\COVID_PBMC_Mild_vs_Healthy.csv', usecols=['Genes']).T.values.tolist()[0]

genes61 = []
#This will hold genes that are in genes6 and in userinput
for h in geneList:
    for i in genes6:
        if h==i:
            genes61.append(h)

if len(genes61) > 0:
    print(
        "The patient is suffering from a mild case of COVID. The following genes are correlated with COVID according to our data.")
    for gene in genes61:
        print(gene)

genes7 = pd.read_csv(r'C:\Users\Shriya\Downloads\COVID_PBMC_Severe.csv', usecols=['Genes']).T.values.tolist()[0]

genes71 = []
#This will hold genes that are in genes7 and in userinput
for j in geneList:
    for k in genes7:
        if j==k:
            genes71.append(j)

if len(genes71)> 0:
    print(
        "The patient is suffering from a severe case of COVID. The following genes are correlated with COVID according to our data." )
    for gene in genes71:
        print(gene)

genes8 = pd.read_excel(r'C:\Users\Shriya\Downloads\pnas.xlsx', sheet_name= 'pnas', usecols=['Symbol'], skipfooter=722).T.values.tolist()[0]


genes81 = []
#genes both in pmas and input(genesList)
genes82 = []
#holds index position of genes in genes81 and basically the row in the CSV file
for l in geneList:
    for m in genes8:
        if l==m:
            genes81.append(l)
            genes82.append(genes8.index(m));



genes83 = pd.read_excel(r'C:\Users\Shriya\Downloads\pnas.xlsx', sheet_name= 'pnas', usecols=['Name'], skipfooter=722).T.values.tolist()[0]
#holds name of each gene
n = 0
#The following function puts the gene in each category (category is based on what the gene does) Then it finds the name of the gene
while n<len(genes81):
    if genes82[n] <= 12:
        print("The name of the gene, " + genes81[n] + ", is " + genes83[genes82[n]] + ". It is an antigen processing and presentation gene. ")
    elif genes82[n] <=74:
        print("The name of the gene, " + genes81[n] + ", is " + genes83[genes82[n]] + ". It is an antimicrobial gene. ")
    elif genes82[n] <=76:
        print("The name of the gene, " + genes81[n] + ", is " + genes83[genes82[n]] + ". This gene is an antimicrobial and part of the BCR Signaling Pathway and TCR Signal Pathway. ")
    elif genes82[n] <=79:
        print("The name of the gene, " + genes81[n] + ", is " + genes83[genes82[n]] + ". It is an antimicobial gene and controls chemokine receptors and cytokine receptors. ")
    elif genes82[n] <=101:
        print("The name of the gene, " + genes81[n] + ", is " + genes83[genes82[n]] + ". This gene deals with antimicrobials, chemokines and cytokines. ")
    elif genes82[n] <=104:
        print("The name of the gene, " + genes81[n] + ", is " + genes83[genes82[n]] + ". This gene deals with antimicrobials and cytokine receptors. ")
    elif genes82[n] <=108:
        print("The name of the gene, " + genes81[n] + ", is " + genes83[genes82[n]] + ". It deals with antimicrobials and cytokines. ")
    elif genes82[n] <=111:
        print("The name of the gene, " + genes81[n] + ", is " + genes83[genes82[n]] + ". This gene deals with antimicrobials, cytokines and interleukins")
    elif genes82[n] <=113:
        print("The name of the gene, " + genes81[n] + ", is " + genes83[genes82[n]] + ". This gene deals with antimicrobials, cytokines and TCR signaling pathway. ")
    elif genes82[n] <=115:
        print("The name of the gene, " + genes81[n] + ", is " + genes83[genes82[n]] + ". This gene deals with antimicrobials and cytokines. It is a TGFb_Family_Member ")
    elif genes82[n] <=117:
        print("The name of the gene, " + genes81[n] + ", is " + genes83[genes82[n]] + ". This gene deals with antimicrobials and cytokines. It is a TNF family member")
    elif genes82[n] <=136:
        print("The name of the gene, " + genes81[n] + ", is " + genes83[genes82[n]] + ". This gene deals with the BCR Signaling Pathway. ")
    elif genes82[n] <=138:
        print("The name of the gene, " + genes81[n] + ", is " + genes83[genes82[n]] + ". This gene deals with the BCR Signaling Pathway, Natural Killer Cell Cytotoxity and the TCR signaling pathway. ")
    elif genes82[n] <=141:
        print("The name of the gene, " + genes81[n] + ", is " + genes83[genes82[n]] + ". This gene deals with the BCR Signaling pathway and TCR signaling pathway")
    elif genes82[n] <=149:
        print("The name of the gene, " + genes81[n] + ", is " + genes83[genes82[n]] + ". This gene deals with chemokine receptors and cytokine receptors.")
    elif genes82[n] <=165:
        print("The name of the gene, " + genes81[n] + ", is " + genes83[genes82[n]] + ". This gene deals with chemokines and cytokines")
    elif genes82[n] <=199:
        print("The name of the gene, " + genes81[n] + ", is " + genes83[genes82[n]] + ". This gene deals with cytokine receptors. ")
    elif genes82[n] <=201:
        print("The name of the gene, " + genes81[n] + ", is " + genes83[genes82[n]] + ". This gene deals with cytokine receptors, interferon receptors and natural killer cell cytotoxicity ")
    elif genes82[n] <=213:
        print("The name of the gene, " + genes81[n] + ", is " + genes83[genes82[n]] + ". This gene deals with cytokine receptors and interleukins receptors")
    elif genes82[n] <=215:
        print("The name of the gene, " + genes81[n] + ", is " + genes83[genes82[n]] + ". This gene deals with cytokine receptors and TGFb family member receptor ")
    elif genes82[n] <=218:
        print("The name of the gene, " + genes81[n] + ", is " + genes83[genes82[n]] + ". This gene deals with cytokine receptors and TNF family member receptors ")
    elif genes82[n] <=245:
        print("The name of the gene, " + genes81[n] + ", is " + genes83[genes82[n]] + ". This gene deals with cytokines ")
    elif genes82[n] <=248:
        print("The name of the gene, " + genes81[n] + ", is " + genes83[genes82[n]] + ". This gene deals with cytokines and interleukins. ")
    elif genes82[n] <=258:
        print("The name of the gene, " + genes81[n] + ", is " + genes83[genes82[n]] + ". This gene deals with cytokines and is a TGFb Family member ")
    elif genes82[n] <=261:
        print("The name of the gene, " + genes81[n] + ", is " + genes83[genes82[n]] + ". This gene deals with cytokines and is a TNF family member")
    elif genes82[n] <=267:
        print("The name of the gene, " + genes81[n] + ", is " + genes83[genes82[n]] + ". This gene deals with  Natural Killer Cell Cytotoxicity ")
    elif genes82[n] <=278:
        print("The name of the gene, " + genes81[n] + ", is " + genes83[genes82[n]] + ". This gene deals with the TCR Signaling pathway ")
    n=n+1
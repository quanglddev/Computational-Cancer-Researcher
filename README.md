# Computational Cancer Researcher
A simple program counting SNPs and small indels

# Dependencies
You need Python 3 since this program uses vcfpy which is only available in Python 3.
``` bash
pip3 install vcfpy
pip3 install pysam
```

# How to use
Simply call the main.py using python module on your machine (mine is python3) and it will run on the sample .VCF file (project.NIST.hc.snps.indels.vcf)
``` bash
python3 main.py
```

# How did I approach the problem?
1.	What is .VCF file? - [Variant Call Format](https://en.wikipedia.org/wiki/Variant_Call_Format)
2.	How can I open .VCF file programmatically? – I found a library written in Python called vcfpy which does exactly what I need [vcfpy](https://pypi.org/project/vcfpy/)
3.	What information does .VCF contain? I found a good documentation explain in details every aspect of .vcf file and what’s the meaning of each keyword in the file [VCF v4.2 Specs](https://samtools.github.io/hts-specs/VCFv4.2.pdf)
4.	After hours of reading the specifications of .VCF file, I finally came to realize that there’s a simple way that can help me count:
a.	SNP: When there is a single base substitutions and there are only two alleles. (can be done using simple if statements)
b.	Indels: Total number of insertions and deletions (special case is when a record belongs to mix type, containing both insertion and deletion). (this can easily be solved by going through all alternate bases (if there are more than two))
c.	Insertions: The reference base is replace with the reference base plus extra bases. (can be easily calculated using len() function)
d.	Deletions: The reference base is replace with the reference base plus extra bases. (can be easily calculated using len() function)
5.	Read documentations and codebase of the library [vcf GitHub](https://github.com/bihealth/vcfpy) and I came up with a simple counting program which is available in this GitHub link: [https://github.com/quanglddev/Computational-Cancer-Researcher](https://github.com/quanglddev/Computational-Cancer-Researcher)


> This is used as an application for employment (Computational Cancer Researcher role at Drexel and Fox Chase Cancer Center.)
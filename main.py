import vcfpy

# Open input, add FILTER header, and open output file
reader = vcfpy.Reader.from_path('./project.NIST.hc.snps.indels.vcf')

count_SNPs = 0
count_indels = 0
count_deletions = 0
count_insertions = 0

for record in reader:
    # Check if record is about single nucleotide variant allele
    # if not record.is_snv():
    #     continue

    reference_base = record.REF
    alternate_bases = [alt.value for alt in record.ALT]

    # The record is SNP when a nucleotide is replaced with a different one
    if len(alternate_bases[0]) == 1:
        if (len(reference_base) == 1):
            if reference_base != alternate_bases[0]:
                count_SNPs += 1

    # The record is insertion/deletion when the base is kept and having extra/missing nucleotide(s) on the alternate bases
    # Go through every alternate bases because the record can be a mixed type
    for alternate_base in alternate_bases:
        # Checking if the base is matching
        if reference_base[0] == alternate_base[0]:
            if len(reference_base) > len(alternate_base):
                # This is a deletion
                count_deletions += 1
            elif len(reference_base) < len(alternate_base):
                # This is an insertion
                count_insertions += 1 

# Indels are the total number of insertions and deletions in the genome
count_indels = count_deletions + count_insertions

print("SNPs: %d" % count_SNPs)
print("Indels: %d" % count_indels)
print("Deletions: %d" % count_deletions)

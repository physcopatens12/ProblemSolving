def dna(s):
    """Counting DNA Nucleotides"""
    return "%s %s %s %s" %(
        s.count('A'), s.count('C'), s.count('G'), s.count('T'))

def rna(t):
    """Transcribing DNA into RNA"""
    return t.replace('T', 'U')

def revc(s):
    """Complementing a Strand of DNA"""
    sc = ""
    for nt in s:
        if nt == 'A': sc += 'T'
        elif nt == 'T': sc += 'A'
        elif nt == 'C': sc += 'G'
        elif nt == 'G': sc += 'C'
    return sc[::-1]

def fib(n, k):
    """Rabbits and Recurrence Relations"""
    reproductive, mate, born = 0, 0, 1
    for _month in range(n-1):
        reproductive += mate
        mate = born
        born = reproductive * k
        total = reproductive + mate + born
    return total

def parse_fasta(fasta):
    """Parsing fasta file into dictionary. From gc"""
    strings = {}
    with open(fasta, 'r') as fr:
        for string in fr.read().strip().split('>')[1:]:
            strings[string.split('\n')[0]] = ''.join(string.split('\n')[1:])
    return strings    

def gc(fasta):
    """Computing GC Content"""
    strings = parse_fasta(fasta)
    gc_contents = {}
    for name in strings.keys():
        sequence = strings[name]
        gc_contents[name] = \
            (sequence.count('G') + sequence.count('C')) / len(sequence)
    return max(gc_contents.keys(), key = lambda k: gc_contents[k]), \
        round(max(gc_contents.values())*100, 6)

def hamm(s, t):
    """Counting Point Mutations"""
    hamming_distance = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            hamming_distance += 1
    return hamming_distance

def iprb(k, m, n):
    """Mendel's First Law"""
    p = k + m + n
    return round(k/p + m/p * (k/(p-1) + (m-1)/(p-1)*(3/4) + n/(p-1)*(1/2))
        + n/p * (k/(p-1) + m/(p-1)*(1/2)), 5)

def prot(s):
    """Translating RNA into Protein"""
    codon_table = {
        "UUU":'F',"CUU":'L',"AUU":'I',"GUU":'V',
        "UUC":'F',"CUC":'L',"AUC":'I',"GUC":'V',
        "UUA":'L',"CUA":'L',"AUA":'I',"GUA":'V',
        "UUG":'L',"CUG":'L',"AUG":'M',"GUG":'V',
        "UCU":'S',"CCU":'P',"ACU":'T',"GCU":'A',
        "UCC":'S',"CCC":'P',"ACC":'T',"GCC":'A',
        "UCA":'S',"CCA":'P',"ACA":'T',"GCA":'A',
        "UCG":'S',"CCG":'P',"ACG":'T',"GCG":'A',
        "UAU":'Y',"CAU":'H',"AAU":'N',"GAU":'D',
        "UAC":'Y',"CAC":'H',"AAC":'N',"GAC":'D',
        "UAA":'Stop',"CAA":'Q',"AAA":'K',"GAA":'E',
        "UAG":'Stop',"CAG":'Q',"AAG":'K',"GAG":'E',
        "UGU":'C',"CGU":'R',"AGU":'S',"GGU":'G',
        "UGC":'C',"CGC":'R',"AGC":'S',"GGC":'G',
        "UGA":'Stop',"CGA":'R',"AGA":'R',"GGA":'G',
        "UGG":'W',"CGG":'R',"AGG":'R',"GGG":'G'
    }
    protein = ""
    for i in range(len(s))[::3]:
        aa = codon_table[s[i:i+3]]
        if aa != 'Stop':
            protein += aa
    return protein

def subs(s, t):
    """Finding a Motif in DNA"""
    subs_loc = []
    for i in range(len(s)-len(t)+1):
        if s[i:i+len(t)] == t:
            subs_loc.append(i+1)
    return ' '.join(map(str, subs_loc))

def cons(fasta):
    """Consensus and Profile"""
    sequences = list(parse_fasta(fasta).values())
    seq_range = range(len(sequences[0]))
    profile_matrix = {
        'A': [0 for t in seq_range], 'C': [0 for t in seq_range],
        'G': [0 for t in seq_range], 'T': [0 for t in seq_range]
    }
    for i in seq_range:
        for sequence in sequences:
            profile_matrix[sequence[i]][i] += 1
    consensus_string = ""
    for nt_counts in zip(*list(profile_matrix.values())):
        consensus_string += ['A','C','G','T'][nt_counts.index(max(nt_counts))]
    return consensus_string, \
        "A: %s C: %s G: %s T: %s" %(
            ' '.join(map(str, profile_matrix['A'])),
            ' '.join(map(str, profile_matrix['C'])),
            ' '.join(map(str, profile_matrix['G'])),
            ' '.join(map(str, profile_matrix['T']))
        )
    
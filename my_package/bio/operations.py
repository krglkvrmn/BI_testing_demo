from my_package.bio.codons import codon_table
from my_package.bio.utils import validate_sequence


def reverse_complement(seq: str, seq_type: str = 'DNA') -> str:
    if not validate_sequence(seq, seq_type):
        raise ValueError("Invalid sequence")

    seq = seq.upper()
    complement_bases = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    if seq_type == 'RNA':
        complement_bases = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}

    return "".join(complement_bases[base] for base in reversed(seq))


def transcribe(dna_seq: str) -> str:
    if not validate_sequence(dna_seq, seq_type='DNA'):
        raise ValueError("Invalid DNA sequence")

    dna_seq = dna_seq.upper()
    return dna_seq.replace('T', 'U')


def translate(rna_seq: str) -> str:
    if not validate_sequence(rna_seq, seq_type='RNA'):
        raise ValueError("Invalid RNA sequence")
    rna_seq = rna_seq.upper()
    protein_seq = []

    # Check that the RNA sequence length is divisible by 3
    if len(rna_seq) % 3 != 0:
        raise ValueError("RNA sequence length must be divisible by 3")

    for i in range(0, len(rna_seq), 3):
        codon = rna_seq[i:i + 3]
        amino_acid = codon_table[codon]
        protein_seq.append(amino_acid)

    return "".join(protein_seq)

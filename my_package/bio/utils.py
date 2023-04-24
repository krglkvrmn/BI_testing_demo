def validate_sequence(seq: str, seq_type: str = 'DNA') -> bool:
    valid_bases = {'DNA': 'ATCG', 'RNA': 'AUCG'}
    seq = seq.upper()
    for base in seq:
        if base not in valid_bases[seq_type]:
            return False
    return True


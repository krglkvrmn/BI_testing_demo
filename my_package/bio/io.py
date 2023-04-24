from typing import Tuple


def write_fasta(seq: str, id: str, description: str, file_path: str):
    with open(file_path, "w") as file:
        fasta_string = f">{id} {description}\n{seq}"
        file.write(fasta_string)


def read_fasta(file_path: str) -> Tuple[str, str, str]:
    with open(file_path, "r") as file:
        id_, description = file.readline().strip(">\n").split(maxsplit=1)
        sequence = "".join(file.readlines())
    return id_, description, sequence

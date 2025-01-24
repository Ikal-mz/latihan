"""Type hints untuk fungsi"""

"""## studi kasus
def fungsi(paraneter) :
    hasil = paraneter ** 2
    print(hasil)

fungsi(2)
fungsi(False)
fungsi("budi")"""

# penggunaan type hints
import string

def fungsi_dengan_hints(argument:int) -> int :
    """FUNGSI DENGAN HINTS"""
    output = 10 ** argument
    return output

HASIL = fungsi_dengan_hints(2)
print(HASIL)

def display(argument:string) :
    print(argument)

display("budi")

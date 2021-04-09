def checkDNA(txt):
    if all(c in "ACGT" for c in txt):
        txt = reverse(dna)
        txt = complement(txt)
        return txt
    else:
        return "Not a valid DNA String"

def reverse(dna):
    # txt = dna[::-1]
    txt = ''
    for i in dna:           #using for loop
        txt = i + txt
    return txt

def complement(dna):
    txt = ''
    for x in dna:
        if x == 'A':
            txt = txt + 'T'
        elif x == 'T':
            txt = txt + 'A'
        elif x == 'C':
            txt = txt + 'G'
        elif x == 'G':
            txt = txt + 'C'

    return txt

dna = input("Enter a valid DNA string: ")
print(checkDNA(dna))

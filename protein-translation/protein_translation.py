def proteins(strand):
    num_of_proteins = 3
    list_of_aminos = [strand[i:i + num_of_proteins] for i in range(0, len(strand), num_of_proteins)]
    dict_of_proteins = {'AUG':	'Methionine',
                        'UUU':	'Phenylalanine',
                        'UUC':	'Phenylalanine',
                        'UUA':	'Leucine',
                        'UUG':  'Leucine',
                        'UCU':  'Serine',
                        'UCC':  'Serine',
                        'UCA':  'Serine',
                        'UCG':  'Serine',
                        'UAU':  'Tyrosine',
                        'UAC':  'Tyrosine',
                        'UGU':  'Cysteine',
                        'UGC':  'Cysteine',
                        'UGG':  'Tryptophan',
                        }
    list_of_proteins = []
    for amino in list_of_aminos:
        if amino in dict_of_proteins.keys():
            list_of_proteins.append(dict_of_proteins[amino])
        else:
            return list_of_proteins
    return list_of_proteins

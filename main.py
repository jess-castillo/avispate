import pickle

with open('original_concepts.pkl', 'rb') as f:
    original = pickle.load(f)

# print("La cantidad de figuras del Agilizate original son:")
# print(len(original.keys()))

# print('Las repeticiones de cada figura son:')
def unique(list1):
    list_set = set(list1)
    unique_list = (list(list_set))
    for x in unique_list:
        print(x)
        
# unique(original.values())


new_concepts = [
'alejota', 
'moharry',
'mandalo_monda',
'yilber_cancelado',
'comentarios_chimbos_jess',
'disponible_spotify',
'buenos_diaaaas',
'virgen_caloto',
'ala_medica',
'pollo_frito',
'shakira',
'gata_miona',
'mochi_triste',
'titan_hembra',
'gorgojos',
'bruja_myle',
'mermelada_pan_maleja',
'jess_lavaloza',
'multas_excel',
'marrano_ahorrador',
'vino_aleja',
'ajiaco',
'mundial_cubiertos',
'pollito_radiactivo',
'las_lindas',
'dos_torres_sauron', 
'chisme',
'cara_juliana_confusion',
'tsunami_canela',
'checoslovaquia'
] 

# print(f"Vamos {len(new_concepts)} conceptos para nuestro agilízate.")


def incidence_matrix(p = 7): # p can be any prime

    # Generate all p^3 - 1 points in affine space, minus the origin:
    points = [(a,b,c) for a in range(p) for b in range(p) for c in range(p)][1::]

    # Quotient by the equivalence relation to give the projective plane points:
    scale = lambda t, k : tuple([((k * v) % p) for v in t])
    canonise = lambda t : (sorted([scale(t, k) for k in range(1, p)])[0])
    points = list(set(map(canonise, points)))

    # We identify each point with its dual line by taking orthogonal complements.
    # A line is incident with a point if the pole of the line is orthogonal to
    # the point, which can be evaluated straightforwardly:
    innerprod = lambda x, y : (sum([a*b for (a, b) in zip(x, y)]) % p)
    imatrix = [[1 if (innerprod(x, y) == 0) else 0 for x in points] for y in points]

    # Output the incidence matrix:
    return imatrix

incidence_matrix = incidence_matrix()

symbols = sorted(new_concepts, key = str.lower)

cards = [
    [symbol for symbol, use_it in zip (symbols, row) if use_it]
    for row in sorted(incidence_matrix)
]

# print(len(cards))
comparison = cards

def test_veracity(cards):
    check = 0
    for card in cards:
        for aux in comparison:
            if card != aux:
                common = set(card).intersection(aux)
                if len(common) != 1:
                    print("There isn't a common element between these two cards:")
                    print(card)
                    print(aux)
                    check += 1

    print(f'Done! There was {check} errors to check.')

# test_veracity(cards)
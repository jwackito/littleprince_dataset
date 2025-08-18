import pandas as pd

def load_littleprince(lang='spanish', count=2314, remove_empty_lines=True, remove_trainling_whitespace=True):
    lines = []
    with open(f'{lang}/data.txt', 'r') as f:
        alllines = f.readlines()[:count]
    if remove_trainling_whitespace:
        alllines = [line.replace(' \n', '\n') for line in alllines]
    if remove_empty_lines:
        lines = [line for line in alllines if (line != '\n' and not line.startswith('____') and not line.startswith('-----'))]
    return lines

languages = { lang: [] for lang in ['english', 'spanish', 'french', 'portuguese']}

for lang in languages:
    lines = load_littleprince(lang=lang)
    languages[lang] = lines

assert len(languages['english']) == len(languages['spanish']), "Las lineas no coinciden entre idiomas eng - esp"
assert len(languages['spanish']) == len(languages['french']), "Las lineas no coinciden entre idiomas esp - fre"
assert len(languages['french']) == len(languages['portuguese']), "Las lineas no coinciden entre idiomas fre - por"

pd.DataFrame(languages).to_csv('little_prince_dataset.csv.gz', index=False)
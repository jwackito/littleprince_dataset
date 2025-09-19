# Aligned Multilingual "The Little Prince" Dataset

This repository provides a trilingual aligned version of *The Little Prince* (*Le Petit Prince*) by Antoine de Saint-Exupéry. It is intended for use in research and applications involving machine translation, parallel corpora, and cross-lingual language modeling.

## Dataset Structure

The dataset is organized into three folders, one for each language:
```
├── english/
│ └── thelittleprince.txt
│ └── data.txt ⬏
├── spanish/
│ └── elprincipito.txt
│ └── data.txt ⬏
├── french/
│ └── lepetitprince.txt
│ └── data.txt ⬏
├── portuguese/
│ └── opequenoprincipe.txt
│ └── data.txt ⬏
```
Each file contains the full text of *The Little Prince* in its respective language. The files are **line-aligned**, meaning that:
- Line *n* in the English file corresponds to line *n* in the Spanish and French files.

This alignment enables straightforward use in multilingual NLP tasks.

## Example

| English                          | Spanish                           | French                          |
|----------------------------------|------------------------------------|----------------------------------|
| Once when I was six years old... | Cuando tenía seis años...          | Lorsque j'avais six ans...       |
| I saw a magnificent image...   | Vi una magnífica imagen...         | J'ai vu une magnifique image...  |

## Usage

You are welcome to use this dataset for academic and research purposes. Please cite the dataset as described below if you use it in your work.

## License

MIT License

## Citation
If you use this dataset, please cite it using the metadata below.
```bibtex
@software{Bogado_Aligned_Multilingual_The_2025,
        author = {Bogado, Joaquin and Giuliodoro, Germán and da Silva Santana Lopes, Barbara},
        license = {MIT License},
        month = jun,
        title = {{Aligned Multilingual 'The Little Prince' Dataset}},
        url = {https://github.com/jwackito/littleprince_dataset},
        version = {1.0.0},
        year = {2025}
}
```

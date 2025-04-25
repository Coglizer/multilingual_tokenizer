# Multi-Language Tokenizer Suite

A command-line toolkit for processing texts in **Aramaic**, **Hebrew**, **Greek**, **Latin**, **German**, and **English**. It supports:

- **Unicode-based tokenization** into `.tokens` files.
- **Vocabulary building** (per-language or combined) into JSON dictionaries.
- **Dictionary-based tokenization** mapping words to integer IDs (`.ids` files).

---

## Project Structure

```
tokenizer_project/
├── tokenizers/                 # Language-specific tokenizer classes
│   ├── base_tokenizer.py       # Shared I/O and tokenization logic
│   ├── aramaic_tokenizer.py    # Aramaic regex
│   ├── hebrew_tokenizer.py     # Hebrew regex
│   ├── greek_tokenizer.py      # Greek regex
│   ├── latin_tokenizer.py      # Latin regex
│   ├── german_tokenizer.py     # German regex
│   └── english_tokenizer.py    # English regex
├── main.py                     # Orchestrates tokenization (creates .tokens)
├── vocabulary_builder.py       # Builds per-language or combined JSON vocab
├── dict_tokenizer.py           # Converts text → ID sequences (single vocab)
├── multi_dict_tokenizer.py     # Batch runs dict_tokenizer for all languages
├── requirements.txt            # External dependencies (regex)
├── .gitignore                  # Excludes bytecode & cache files
└── README.md                   # This documentation
```

---

## Requirements

- **Python 3.7** or higher
- [regex](https://pypi.org/project/regex/) module (for full Unicode support)

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## Usage

### 1. Tokenization into `.tokens`

Use `main.py` to tokenize raw `.txt` files by language.

```bash
python main.py \
  --aramaic  texts/aramaic \
  --hebrew   texts/hebrew  \
  --greek    texts/greek   \
  --latin    texts/latin   \
  --german   texts/german  \
  --english  texts/english \
  --out      tokenized_output
```

Each folder’s `.txt` files become `.tokens` in `tokenized_output/<language>/`.

### 2. Building Vocabularies

#### Separate per-language

```bash
python vocabulary_builder.py \
  --input  tokenized_output \
  --output vocabularies
```

Generates one JSON file per language: `vocabularies/<language>_vocab.json`.

#### Combined single dictionary

```bash
python vocabulary_builder.py \
  --input          tokenized_output \
  --output         vocabularies \
  --combined       \
  --combined-name  combined_vocab.json
```

Produces `vocabularies/combined_vocab.json` with all tokens.

### 3. Dictionary-based Tokenization to `.ids`

Use `multi_dict_tokenizer.py` to convert raw text directly into ID sequences.

#### Separate mode (per-language vocabs)

```bash
python multi_dict_tokenizer.py \
  --mode       separate \
  --vocab-dir  vocabularies \
  --input-dir  raw_texts     \
  --output-dir encoded_ids   \
  --unk        0
```

#### Combined mode (shared vocab)

```bash
python multi_dict_tokenizer.py \
  --mode           combined \
  --vocab-dir      vocabularies        \
  --combined-vocab vocabularies/combined_vocab.json \
  --input-dir      raw_texts           \
  --output-dir     encoded_ids         \
  --unk            0
```

This writes `.ids` files (space-separated IDs) into `encoded_ids/<language>/`.

---

## Git Configuration

Add to your `.gitignore`:

```
__pycache__/
*.py[cod]
```

This prevents committing compiled bytecode and cache folders.

---

## Extending the Toolkit

- **Add new languages**: create a `YourLangTokenizer` in `tokenizers/` with a Unicode regex, then register it in `main.py` and the vocab builder.
- **Customize tokenization**: override `BaseTokenizer.tokenize_text()` for special rules or preprocessing.
- **Alternate outputs**: modify writers to export CSV, XML, or database inserts.

---

## License

This project is released under the **MIT License**. Feel free to adapt and extend!


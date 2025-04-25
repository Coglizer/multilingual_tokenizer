# Multilingual Text Dictionary Builder

A simple, modular Python CLI to build word–ID dictionaries from text files in multiple languages (Aramaic, Hebrew, Greek, Latin, German, and English). Supports exporting individual language dictionaries or a single combined dictionary with sequential IDs.

## Features

- **Language-specific cleaning**: Strips diacritics, normalizes umlauts, removes punctuation per language.
- **Separate or combined output**: Choose to export one JSON per language or a unified JSON mapping all words to unique IDs.
- **Order of parsing**: Processes languages in the order Aramaic → Hebrew → Greek → Latin → German → English.
- **Zero dependencies**: Pure Python3 using only standard library modules (`argparse`, `os`, `json`, `unicodedata`).

## Directory Structure

```
multilingual_tokenizer/
├── cli.py                # Command-line interface
├── base_dict.py          # Base class for dictionary building
├── aramaic_dict.py       # Aramaic-specific cleaning
├── hebrew_dict.py        # Hebrew-specific cleaning
├── greek_dict.py         # Greek-specific cleaning
├── latin_dict.py         # Latin-specific cleaning
├── german_dict.py        # German-specific cleaning
├── english_dict.py       # English-specific cleaning
└── utils.py              # Helper to instantiate in parse order
```

## Installation

1. Clone or download this repository:
   ```bash
   git clone https://github.com/yourusername/multilingual_tokenizer.git
   cd multilingual_tokenizer
   ```
2. Ensure you have Python 3.6+ installed.

## Usage

From the project root, run `cli.py` with the language flags pointing at folders containing `.txt` files.

### Export a combined dictionary (default)

```bash
python cli.py \
  --aramaic /path/to/aramaic_folder \
  --hebrew  /path/to/hebrew_folder \
  --greek   /path/to/greek_folder \
  --latin   /path/to/latin_folder \
  --german  /path/to/german_folder \
  --english /path/to/english_folder \
  -o combined_dict.json
```

This creates `combined_dict.json` mapping every unique word (across all languages) to a unique integer ID.

### Export separate dictionaries per language

```bash
python cli.py --separate \
  --hebrew  /path/to/hebrew_folder \
  --english /path/to/english_folder \
  -o ./output_folder
```

Creates one JSON file per language in `./output_folder` (e.g. `hebrew_dict.json`, `english_dict.json`).

> **PowerShell users**: to avoid flag parsing issues, prepend `--%` to the CLI:
> ```powershell
> python cli.py --% --hebrew "C:\path\to\hebrew_folder" --english "C:\path\to\english_folder" -o combined.json
> ```

## Examples

- **Combine Hebrew, Greek, English**
  ```bash
  python cli.py --hebrew "C:\...\leningrad_codex-uxlc-2.2" \
                --greek  "C:\...\sblgnt-1.2" \
                --english "C:\...\translations\english" \
                -o bible_dict.json
  ```

- **Separate only English and German**
  ```bash
  python cli.py --separate \
                --english /data/eng_texts \
                --german  /data/de_texts \
                -o ./lang_dicts
  ```

## Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

## License

MIT License


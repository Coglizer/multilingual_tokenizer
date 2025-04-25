### cli.py

import argparse
import os
import json
from utils import get_ordered_dicts


def main():
    parser = argparse.ArgumentParser(
        description='Build multilingual dictionaries (separate or combined).'
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--separate', action='store_true',
                       help='Export separate JSON per language')
    group.add_argument('--combined', action='store_true',
                       help='Export one combined JSON (default)')
    parser.add_argument('--aramaic', help='Aramaic .txt folder')
    parser.add_argument('--hebrew', help='Hebrew .txt folder')
    parser.add_argument('--greek', help='Greek .txt folder')
    parser.add_argument('--latin', help='Latin .txt folder')
    parser.add_argument('--german', help='German .txt folder')
    parser.add_argument('--english', help='English .txt folder')
    parser.add_argument('-o', '--output', required=True,
                        help=('If combined: output JSON filename. '
                              'If separate: output folder.'))
    args = parser.parse_args()

    paths = {lang: getattr(args, lang) for lang in
             ['aramaic','hebrew','greek','latin','german','english']
             if getattr(args, lang)}
    dicts = get_ordered_dicts(paths)

    if args.separate:
        os.makedirs(args.output, exist_ok=True)
        for d in dicts:
            word_map = d.build_dictionary()
            lang = d.__class__.__name__.replace('Dictionary','').lower()
            out_file = os.path.join(args.output, f"{lang}_dict.json")
            d.export_json(out_file)
            print(f"Exported: {out_file}")
    else:
        combined = {}
        next_id = 1
        for d in dicts:
            for w in d.build_dictionary().keys():
                if w not in combined:
                    combined[w] = next_id
                    next_id += 1
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(combined, f, ensure_ascii=False, indent=2)
        print(f"Combined dict written to: {args.output}")


if __name__ == '__main__':
    main()
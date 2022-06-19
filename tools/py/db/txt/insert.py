#! python3

import sys
import pathlib

if __name__ == "__main__" and __package__ is None:
    sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))
    __package__ = "db.txt"

from . import trie

def main(args) -> None:
    print("Insert file "+args.file.name+" into "+args.db)
    if not pathlib.Path(args.db).is_dir():
        print(args.db + " is not directory")
        exit(1)
    print(trie.str2path("hi_abc de   kl"))
    print(trie.name2path("hi_abc de", "kl"))
    print(trie.name2path("hi__abc  de", ["kl", "mk"]))
    print(trie.filename("hi__abc  de", ["kl", "mk"]))

import argparse

def parse_argv(argv: list[str]):
    parser = argparse.ArgumentParser(description='Insert YAML file into DB.')
    parser.add_argument('-f', '--force',
                        action = 'store_true', default = False,
                        help = "force overwriting existing file"
                       )
    parser.add_argument('file',
                        type=argparse.FileType('r', encoding='UTF-8'),
                        help = "YAML file"
                       )
    parser.add_argument('db',
                        help = "Path to DB"
                       )
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_argv(sys.argv)
    main(args)
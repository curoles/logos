# YAML syntax spec: https://yaml.org/spec/1.2.2/

import os
import pathlib
import ruamel.yaml as yaml # pip3 install ruamel.yaml
from . import trie

def load(fname: str) -> dict:
    data = None
    with open(fname, "r") as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    return data

def save(fname: pathlib.Path, data: dict, force=False):
    print(fname)
    os.makedirs(name=fname.parent, exist_ok=force)
    with open(fname, "w") as stream:
        try:
            data = yaml.safe_dump(data, stream)
        except yaml.YAMLError as exc:
            print(exc)

def insert(fname: str, dbpath: str, force=False) -> None:
    data = load(fname)
    for key,val in data.items():
        domain = val['domain']
        db_fname = trie.filename(key, domain)
        fpath = pathlib.Path(dbpath) / db_fname
        save(fpath, {key: val}, force)
import pathlib
import re

def fixname(name: str) -> str:
    return re.sub('\_+', '_', name.replace(' ', '_'))

def str2pathlist(name: str) -> list[str]:
    """Name to Trie path list"""
    return list(name.replace(' ', '_'))

def str2path(name: str) -> pathlib.Path:
    return pathlib.Path(*str2pathlist(name))

def name2str(name: str, domains: str | list) -> str:
    if isinstance(domains, list):
        domain = '_'.join(domains)
    else:
        domain = domains
    name = fixname(name)
    domain = fixname(domain)
    return name + '__' + domain

def name2path(name: str, domains: str | list) -> pathlib.Path:
    return str2path(name2str(name, domains))

def filename(name: str, domains: str | list) -> pathlib.Path:
    fname = fixname(name) + '.yml'
    return pathlib.Path(name2path(name, domains), fname)
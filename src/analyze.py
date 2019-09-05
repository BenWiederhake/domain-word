#!/usr/bin/env python3

from collections import defaultdict
import os.path

MAX_SUFFIX_TREE_NODESIZE = 100
EXPLOSIONS_MUT = 0

class SuffixTree:
    def __init__(self):
        self.simple = True
        self.storage = defaultdict(set)
        self.empty_values = set()

    def add(self, word, source):
        assert source is not None
        if word == '':
            self.empty_values.add(source)
        elif self.simple:
            self.storage[word].add(source)
            if len(self.storage) > MAX_SUFFIX_TREE_NODESIZE:
                self.do_explode()
        else:
            self.storage[word[-1]].add(word[:-1], source)

    def get_suffixes_of(self, word):
        results = set(self.empty_values)
        if word == '':
            return results

        if self.simple:
            for suffix, values in self.storage.items():
                if not word.endswith(suffix):
                    continue
                results.update(values)
            return results
        else:
            results.update(self.storage[word[-1]].get_suffixes_of(word[:-1]))
            return results

    def do_explode(self):
        assert self.simple
        global EXPLOSIONS_MUT
        EXPLOSIONS_MUT += 1
        old_storage = self.storage
        self.storage = defaultdict(SuffixTree)
        self.simple = False
        for word, sources in old_storage.items():
            substore = self.storage[word[-1]]
            for source in sources:
                substore.add(word[:-1], source)


def simplify(line):
    line = line.replace('á', 'a')
    line = line.replace('â', 'a')
    line = line.replace('å', 'a')
    line = line.replace('ä', 'a')
    line = line.replace('ç', 'c')
    line = line.replace('é', 'e')
    line = line.replace('è', 'e')
    line = line.replace('ê', 'e')
    line = line.replace('í', 'i')
    line = line.replace('ñ', 'n')
    line = line.replace('ó', 'o')
    line = line.replace('ô', 'o')
    line = line.replace('ö', 'o')
    line = line.replace('û', 'u')
    line = line.replace('ü', 'u')
    line = line.replace('ü', 'u')
    return line


def parse_pubsub(filename, into_tree):
    with open(filename, 'r') as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            line = line.strip().lower()
            if not line or line.startswith('//') or line.startswith('!') or line.startswith('#'):
                continue
            if line.startswith('*.'):
                line = line[2:]
            source = line
            line = line.replace('*', '')
            line = line.replace('.', '')
            line = line.replace('_', '')
            line = line.replace('-', '')
            into_tree.add(line.lower(), source)
            try:
                line = line.encode('idna').decode('idna')  # Ugly hack
            except UnicodeError:
                pass
            into_tree.add(line.lower(), source)
            line = simplify(line)
            into_tree.add(line.lower(), source)


def find_words(filename, in_tree):
    all_results = dict()
    with open(filename, 'r') as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            line = line.strip().lower()
            if line.startswith('//') or line.startswith('!') or line.startswith('#'):
                continue
            # "'áâåäçéèêíñóôöûü"
            results = set()
            line = line.replace("'", '')
            raw_line = line
            results.update(in_tree.get_suffixes_of(line.lower()))
            line = simplify(line)
            results.update(in_tree.get_suffixes_of(line.lower()))
            if results:
                results = list(results)
                results.sort(key=len, reverse=True)
                all_results[raw_line] = results
    return all_results


def print_results(all_results):
    for word, suffixes in all_results.items():
        print('{}: {}'.format(word, suffixes))


def run_in_dir(dirname):
    suffix_tree = SuffixTree()
    parse_pubsub(os.path.join(dirname, 'public_suffix_list.dat'), suffix_tree)
    parse_pubsub(os.path.join(dirname, 'tlds-alpha-by-domain.txt'), suffix_tree)
    results = find_words(os.path.join(dirname, 'american-english'), suffix_tree)
    # results = find_words(os.path.join(dirname, 'few-words.txt'), suffix_tree)
    print_results(results)


if __name__ == '__main__':
    run_in_dir(os.path.dirname(__file__))

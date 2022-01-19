#!/usr/bin/env python3

import sys, argparse, numpy as np
from tagreader import ResultParser

parser = argparse.ArgumentParser()
parser.add_argument("expected")
parser.add_argument("actual")
args = parser.parse_args(sys.argv[1:])

atol = 1.0e-7

with open(args.expected) as f:
    expected = {entry.name: np.array(entry.value) for entry in ResultParser(f).entries}

with open(args.actual) as f:
    actual = {entry.name: np.array(entry.value) for entry in ResultParser(f).entries}

for entry in expected.keys():
    assert entry in actual, f"Required '{entry}' is missing in actual data"
    assert np.allclose(actual[entry], expected[entry], atol=atol), \
        f"Missmatch for entry '{entry}'\n" \
        f"    expected: {expected[entry].__repr__()}\n" \
        f"    but got:  {actual[entry].__repr__()}"

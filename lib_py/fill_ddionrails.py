import os, sys
import pandas as pd

sys.path.append(os.path.expanduser("~/github/ddi.py/"))

from ddi.onrails.repos import merge_instruments, dor1, copy, convert_r2ddi

def main():
    copy.study()
    dor1.variables()
    copy.f("datasets.csv")
    merge_instruments.main()
    convert_r2ddi.Parser(version="v1").write_json()

if __name__ == "__main__":
    main()

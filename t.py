#!/usr/bin/env python
import pandas as pd
import sys


def main():
    path = sys.argv[1]
    x = pd.read_excel(path)
    breakpoint()


if __name__ == "__main__":
    main()

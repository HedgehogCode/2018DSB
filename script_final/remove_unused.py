#!/usr/bin/env python

import os
import sys
import tempfile
from urllib import request
import shutil

import pandas as pd


def main():
    # Create temp dir
    tempdir_obj = tempfile.TemporaryDirectory()
    tempdir = tempdir_obj.name

    # Load the ground truth for the test set
    csv_file = os.path.join(tempdir, 'stage2_solution_final.csv')
    request.urlretrieve(
        'https://data.broadinstitute.org/bbbc/BBBC038/stage2_solution_final.csv',
        csv_file)
    solution_df = pd.read_csv(csv_file)

    # Find the ignored files
    ignored_df = solution_df[solution_df['Usage'] == 'Ignored']

    # List the image directories
    ignored_dirs = [os.path.join('../input/stage2_test_final', idx)
                    for idx in ignored_df['ImageId'].unique()]

    for ignored_dir in ignored_dirs:
        shutil.rmtree(ignored_dir)


if __name__ == '__main__':
    sys.exit(main())

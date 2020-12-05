# -*- coding: utf-8 -*-
#
#
# Project: HORAE
# Author: Amir HAZEM
# Created: 24/09/2019
# Updated: 02/12/2020
#
#
# Role:
# Preprocesses raw books of hours and generate train/test data
# This script generates train and test csv files:
# train --> "../data/train/csv/hier/"
# test  --> "../data/train/csv/flat/"
# flat: do not consider hierarchie between sections of levels 1 to 3
# hier: considers hierarchie in the tagset
#       level2 for instance is the concatenation of
#       tagset of level1 and level2 and is represented as level12
# For segmentation, we also generate


# Libraries
from __future__ import division
import sys
import horae as ho


if __name__ == '__main__':

    # Inputs
    path_in_train_raw = "../data/train/raw/"
    path_in_test_raw = "../data/test/raw/"

    # Outputs
    path_out_train_csv_hier = "../data/train/csv/hier/"
    path_out_train_csv_flat = "../data/train/csv/flat/"

    # Hierarchical classes are:
    # level1 level12 level123 level23
    path_out_test_csv_hier = "../data/test/csv/hier/"

    # Flat classes are:
    # level1 level2 level3
    path_out_test_csv_flat = "../data/test/csv/flat/"

    # choi format
    path_out_flat_choi = "../data/test/choiformat/flat/"
    path_out_hier_choi = "../data/test/choiformat/hier/"
    path_out_textonly = "../data/test/txt/"

    try:
        ho.generate_choi_txt(path_in_test_raw, path_out_flat_choi,
                             path_out_hier_choi, path_out_textonly)

        print("Generate flat and hierarchical training data...")
        ho.generate_ML_transcriptions(path_in_train_raw,
                                      path_out_train_csv_flat,
                                      path_out_train_csv_hier)

        print("Generate flat and hierarchical test data...")
        ho.generate_ML_transcriptions(path_in_test_raw,
                                      path_out_test_csv_flat,
                                      path_out_test_csv_hier)
    except Exception as exp:

        print("Unexpected error ", sys.exc_info()[0])
        print(str(exp))

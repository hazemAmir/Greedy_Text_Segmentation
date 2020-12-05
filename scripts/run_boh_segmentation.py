# -*- coding: utf-8 -*-
#
#
# Project: HORAE
# Author: Amir HAZEM
# Created: 24/09/2019
# Updated: 02/12/2020
#
#
# Role: text segmentation
#


# Libraries
from __future__ import division
import sys
import horae as ho

if __name__ == '__main__':

    try:
        # Inputs
        corpus_train = sys.argv[1]  # All or corpus name in  data/train/csv/
        corpus_test = sys.argv[2]  # Arsenal637/Beaune055/Caen273/Zurich169
        tagset_type = sys.argv[3]  # hier / flat
        level = sys.argv[4]  # level1 / level2 / level3 (hierarchical 1+2+3)
        relaxation = int(sys.argv[5])  # 50 / 100 / ...
        classifier = sys.argv[6]  # svm / BERT / BERT*

        path_train = "../data/train/csv/" + tagset_type + "/" +\
                     corpus_train + ".csv"
        path_pred = "../data/test/pred/" + corpus_test + "_" + level +\
                    ".pred_" + classifier
        path_seg_pred = "../data/test/seg/" + corpus_test + "_" +\
                        level + ".pred_" + classifier

        labels = ho.load_ref_labels(path_train, level)
        ho.segmentation(path_pred, path_seg_pred, labels, relaxation)

    except Exception as exp:

        print("Unexpected error ", sys.exc_info()[0])
        print(str(exp))

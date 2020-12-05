# -*- coding: utf-8 -*-
#
#
# Project: HORAE
# Author: Amir HAZEM
# Created: 24/09/2019
# Updated: 02/12/2020
#
#
# Role: Evaluation of several machine learning classifiers
# (SVM, Logit, naive_bayes, Decision Tree, etc.)
#

# Libraries
from __future__ import division
import sys
import horae as ho


if __name__ == '__main__':

    try:
        # Inputs
        corpus_train = sys.argv[1]  # All / or corpus name in data/train/csv/
        # Arsenal651 for instance
        corpus_test = sys.argv[2]  # Arsenal637/Beaune055/Caen273/Zurich169
        data_type = sys.argv[3]  # flat / hier
        classifier = sys.argv[4]  # svm/logit/gnb/rf/dt/ada/mlp/xgb
        level = sys.argv[5]  # level1 / level2 / level3 (hierarchical 1+2+3)

        path_train = "../data/train/csv/" + str(data_type) +\
                     "/" + corpus_train + ".csv"
        path_test = "../data/test/csv/" + str(data_type) +\
                    "/" + corpus_test + ".csv"

        # save model
        model_name = classifier + "_" + corpus_train + "_" + level
        path_save_model = "../data/train/ML_models/" + model_name + '.sav'

        (tfidf, model, id_to_category) = ho.train(path_train, path_save_model,
                                                  level, classifier)

        (y_pred, labels_test, id_to_category2) = ho.test(path_test, tfidf,
                                                         model, level)

        ho.eval(y_pred, labels_test, id_to_category, id_to_category2)

    except Exception as exp:

        print("Unexpected error ", sys.exc_info()[0])
        print(str(exp))

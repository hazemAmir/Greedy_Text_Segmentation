# -*- coding: utf-8 -*-
#
#
# Project: HORAE
# Author: Amir HAZEM
# Created: 24/09/2019
# Updated: 02/12/2020
#
#
# Role: Line classification (ML)
#
# Generates line predictions of a given machine learning classifier
# that is: SVM, Logit, naive_bayes...)


# Libraries
from __future__ import division
import codecs
import sys
import horae as ho


if __name__ == '__main__':

    # Inputs
    corpus_train = sys.argv[1]  # All / or corpus name in data/train/csv/...
    # Arsenal651 for instance
    corpus_test = sys.argv[2]  # Arsenal637 / Beaune055 / Caen273 / Zurich169
    data_type = sys.argv[3]  # flat / hier
    classifier = sys.argv[4]  # svm / logit / gnb / rf / dt / ada / mlp / xgb
    level = sys.argv[5]  # level1 / level2 / level3 (hierarchical 1 + 2 + 3)
    bool_train = eval(sys.argv[6]) 
    # bool_train = False

    path_train = "../data/train/csv/" + str(data_type) +\
                 "/" + corpus_train + ".csv"
    path_test = "../data/test/csv/" + str(data_type) +\
                "/" + corpus_test + ".csv"

    path_pred = "../data/test/pred/" + corpus_test + "_" + level + ".pred_" +\
                classifier 
    # save model
    model_name = classifier + "_" + corpus_train + "_" + level
    path_save_model = "../data/train/ML_models/" + model_name + '.sav'

    
    
    # MAIN
    if bool_train:

        (tfidf, model, id_to_category) = ho.train(path_train, path_save_model,
                                                  level, classifier)
    else:
        # Load model ...
        print("Load saved model... ")
        (tfidf, model, id_to_category) = ho.load_model(path_train,
                                                       path_save_model,
                                                       level, classifier)

    (y_pred, labels_test, id_to_category2) = ho.test(path_test, tfidf,
                                                     model, level)

    ho.eval(y_pred, labels_test, id_to_category, id_to_category2)

    tab_pred = {}
    cpt = 0
    for i in range(len(labels_test)):

        tab_pred[cpt] = id_to_category[y_pred[i]]
        cpt += 1

    ho.generate_predictions(path_test, path_pred, tab_pred)

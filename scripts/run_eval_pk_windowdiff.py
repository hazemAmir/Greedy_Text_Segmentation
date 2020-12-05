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
from operator import itemgetter, attrgetter
import sys
from nltk.metrics.segmentation import pk, windowdiff
import segeval as se
import horae as ho
import codecs


if __name__ == '__main__':

    test = sys.argv[1]
    classifier = sys.argv[2]
    type_ = sys.argv[3]
    level = sys.argv[4]

    path_pred = "../data/test/seg/" + test + "_" + level + ".pred_" +\
                classifier
    path_ref = "../data/test/choiformat/" + type_ + "/" + test + "_" +\
               level + ".ref"

    ref, nbref1, refs = ho.load_text(path_ref)
    pred, nbpred1, preds = ho.load_text(path_pred)

    d = {"stargazer": {"1": refs, "2": preds}}

    seg1 = d['stargazer']['1']
    seg2 = d['stargazer']['2']
    segs1 = se.convert_positions_to_masses(seg1)
    segs2 = se.convert_positions_to_masses(seg2)
    print("pk\tWindowdiff: \n")
    print(str(round(se.pk(segs2, segs1), 4)) + "\t" +
          str(round(se.window_diff(segs2, segs1), 4)))

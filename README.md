# Greedy_Text_Segmentation
# Requirements:
- python3.5
  see requirements.txt file

# Execution
- git clone https://github.com/hazemAmir/Greedy_Text_Segmentation.git
- cd Greedy_Text_Segmentation
- virtualenv -p python ENV
- source ENV/bin/activate 
- pip3 install -r requirements.txt

# Quick run

## Segmentation of the  Arsenal 637 bokk of hours using SVM classifier:

- python3 run_preprocessing.py
- python3 run_gen_predictions_ML_classifiers.py All Arsenal637 hier svm level1 True
- python3 run_boh_segmentation.py All Arsenal637 hier level1 50 svm
- python3 run_eval_pk_windowdiff.py Arsenal637 svm hier level1

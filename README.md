# Greedy_Text_Segmentation

When citing **The Greedy Text Segmentation approach** in academic papers and theses, please use the following BibTeX entry:
```
@inproceedings{hazem-etal-2020-hierarchical,
    title = "Hierarchical Text Segmentation for Medieval Manuscripts",
    author = "Hazem, Amir  and
      Daille, Beatrice  and
      Stutzmann, Dominique  and
      Chevalier, Louis and
      Kermorvant, Christopher"
    booktitle = "Proceedings of the 28th International Conference on Computational Linguistics",
    month = dec,
    year = "2020",
    address = "Barcelona, Spain (Online)",
    publisher = "International Committee on Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.coling-main.549",
    pages = "6240--6251"
}
```


# Requirements:
- python3.5
  see requirements.txt file

# Execution
- git clone https://github.com/hazemAmir/Greedy_Text_Segmentation.git
- cd Greedy_Text_Segmentation
- virtualenv -p python ENV
- source ENV/bin/activate 
- pip3 install -r requirements.txt

## Quick run

### Segmentation of the Arsenal 637 book of hours using SVM classifier

- python3 run_preprocessing.py
- python3 run_gen_predictions_ML_classifiers.py All Arsenal637 hier svm level1 True
- python3 run_boh_segmentation.py All Arsenal637 hier level1 50 svm
- python3 run_eval_pk_windowdiff.py Arsenal637 svm hier level1


## I) Preprocessing:
    --------------
    - Generates train/test files for both line classification and text segmentation
    - Training texts should be put in "../data/train/raw/" and test files in "../data/test/raw/"
    - Outputs are generated as flat or hierarchical tag sets in "../data/train/csv/hier/" and "../data/train/csv/flat/" for training.
    - Similarily, test files are generated in "../data/test/csv/hier/" and "../data/test/csv/flat/" for testing.
	
    --> Command line:  python3 run_preprocessing.py

## II) Classification:

    		
###    1) Evaluation can be done using the "run_eval_ML_classifiers.py" script  	
        
       --> Command line: python3 run_eval_ML_classifiers.py train test tagset_type classifier class_level
    
       --> Parameters: 
                      - train         # All or corpus name in  data/train/csv/...
                      - test          # Arsenal637 / Beaune055 / Caen273 / Zurich169
                      - tagset_type   # flat / hier
                      - classifier    # svm / logit / gnb / rf / dt / ada / mlp / xgb
                      - class_level   # level1 / level2 / level3 / level12 / level123 (hierarchical 1 + 2 + 3)			 	
				
       --> Example:   python3 run_eval_ML_classifiers.py All Arsenal637 hier svm level1

### 2) Generation of class' line predictions 	
	
       --> Command line: python3 run_gen_predictions_ML_classifiers.py train test tagset_type classifier class_level train_or_not

       --> Parameters:   same as the evaluation script parameters with the additional parameter: train_or_not 
			 train_or_not # True if training a classifer  
                  	
       --> Example:      python3 run_gen_predictions_ML_classifiers.py All Arsenal637 hier svm level1 True 
	

## II) Segmentation:

###    II-1) SVM classifier:

    1) Test segmentaion:
	
       --> Command line: python3 run_boh_segmentation.py train test tagset_type level relaxation classifier

       --> Parameters: 
                      - train         # All or corpus name : serves only to load labels (classes per level)
                      - test          # Arsenal637 / Beaune055 / Caen273 / Zurich169
                      - level         # level1 / level12 / level123 (if  hier) / level1 / level2 / level3 (if flat)
                      - relaxation    # 5 10 50 100 (number of misclassified lines = tolerance factor)
                      - classifier    # svm / logit / gnb / rf / dt / ada / mlp / xgb / fastText / BERT / BERT* 
 			  	
       --> Example:      python3 run_boh_segmentation.py All Arsenal637 hier level1 50 svm
       
      II-1) BERT classifier:
            coming soon
##    III) Evaluation

       --> Command line: python3 run_eval_pk_windowdiff.py test classifier tagset_type level

       --> Parameters: 
                      - test          # Arsenal637 / Beaune055 / Caen273 / Zurich169
                      - classifier    # svm / logit / gnb / rf / dt / ada / mlp / xgb / BERT / BERT*       		  	 
                      - tagset_type   # flat / hier
                      - level         # level1 / level12 / level123 (if  hier) / level1 / level2 / level3 (if flat)

       --> Example:   python3 run_eval_pk_windowdiff.py Arsenal637 svm hier level1
       

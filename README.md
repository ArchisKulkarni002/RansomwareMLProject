# **RansomwareMLProject**: Ransomware Detection and Network Traffic Analysis Using Machine Learning
*By
Archis K, M B Ashish, Nitin R*

> [RansomwareMLProject Github Link](https://github.com/ArchisKulkarni002/RansomwareMLProject) (Repo might be private)

## 1. Abstract
Ransomware is a form of malware that restricts access to a victim’s data until a ransom is paid, on Android devices ransomware can manifest in various forms, from locking the device to encrypting personal files, rendering them inaccessible. The increasing prevalence of Android ransomware highlights the need for effective detection methods that can identify such threats before they cause significant damage. 

Ransomware, in its operation, often generates distinctive patterns of network activity. This includes communication with command and control (C2) servers for instructions or data exfiltration, as well as unusual data transfers or requests that may signal malicious behavior.

This project focuses on examining the network traffic characteristics, such as the Flow IAT(Inter-arrival Time), duration, size, and packets/s using various Machine Learning techniques such as k-NN, Decision Tree, Random Forest, ANN/MLP so as to identify, if it is normal(benign) network pattern or classify the ransomware using the unique network signature.

## 3. Dataset

> [Android Ransomware Detection](https://www.kaggle.com/datasets/subhajournal/android-ransomware-detection)

The dataset comprises network monitoring records of Android devices aimed at identifying ransomware types and benign traffic present in user networks. It contains a total of 392,034 rows and 85 columns. The dataset includes 10 distinct types of Android ransomware, alongside benign traffic. The ransomware types are as follows: *SVpeng, PornDroid, Koler, RansomBO, Charger, Simplocker, WannaLocker, Jisut, Lockerpin, and Pletor*.

The distribution of data labels is summarized in the table below:

| **Label**   | **Record Count** |
| ----------- | ---------------- |
| SVpeng      | 54,161           |
| PornDroid   | 46,082           |
| Koler       | 44,555           |
| Benign      | 43,091           |
| RansomBO    | 39,859           |
| Charger     | 39,551           |
| Simplocker  | 36,340           |
| WannaLocker | 32,701           |
| Jisut       | 25,672           |
| Lockerpin   | 25,307           |
| Pletor      | 4,715            |

This dataset serves as a robust foundation for analyzing network traffic patterns and classifying various ransomware types.


## 5. Approaches

### 5.2 Naive Multiclass Classification
Here is the naive section content:
The first attempt was to make use of a decision tree classifier to predict the labels of all ransomwares using the entire dataset after encoding and preprocessing.

This attempt yielded extremely high accuracy figures as described in Results, but the result was dependent almost entirely on two columns, namely Flow ID and Timestamp.

Relying on these two parameters causes a serious shortcoming in the analysis, which is explained in the following section.

### 5.3 The Misapplication of Network Identifiers in Classification

The studies have trained models using network identifiers like Timestamp, Flow ID (Source IP + Destination IP), and Source IP. Due to the way the data is captured, the Ransomware labels become linearly separable along these identifiers, leading to high accuracy (93.53% and 95.20%) when classifying ransomware using these features individually. However, when these features are excluded, the accuracy drops significantly, indicating the model hasn't learned the deeper network patterns associated with ransomware.

Using Timestamp, Flow ID, and Source IP directly for classification provides limited insight into the actual traffic behavior. These identifiers offer little information about the network's content or malicious activity. Instead, classification should focus on dynamic traffic patterns, such as flow characteristics, packet sizes, and protocol behavior, which better reflect network activity and allow for more accurate, robust, and adaptable models.

### 5.4 PCA Multiclass Classification
We used the dataset, consisting of 20 standardized features derived from a larger set of 75 columns using PCA for multiclass classification with 11 label classes, including one benign class and multiple virus categories. One-hot encoding was applied to the labels. Several machine learning models were utilized, including an *Artificial Neural Network (ANN)*, *Logistic Regression* for binary classification, and a *Random Forest classifier*.

### 5.5 Feature Selection Multiclass Classification
A dataset consisting of 20 most relevant features, identified through feature selection, was utilized for direct multiclass classification. The three features with the highest variance were excluded. The selected features were cleaned, standardized, and encoded as needed. This dataset was used for direct multiclass classification. Several machine learning models were applied, including _Artificial Neural Network (ANN)_, _K-Nearest Neighbors (KNN)_, and _Random Forest_.

### 5.6 Feature Selection Binary Classification
The dataset comprising 20 most relevant features from feature selection was used. The classification involved determining whether a sample was benign or ransomware, with further classification applied for ransomware samples. Several machine learning models were employed, including _Artificial Neural Network (ANN)_, _Random Forest_, and _Decision Tree_.

### 5.7 Ensemble Multiclass Classification
Ensemble multiclass classification is a technique where individual models are constructed to perform binary classification over each ransomware class.

Binary classification is done by setting label as 1 for a certain ransomware class, and 0 for all others. 0-labelled data is randomly selected to be equal in volume to 1-labelled data. This makes for 50:50 distribution of 1/0 data.

Steps are as follows
1. Encode and balance dataset for binary classification, i.e. _whether or not it belongs to the ransomware class_.
2. Train a classifier model (in this case, random forest).
3. Repeat step 1 and 2 for 11 all ransomware classes, including benign.
4. Save the row-wise prediction data of each model in a separate column. Concatenate the actual label too.
5. Use the new prediction data for multiclass classification.

## Conclusion
The dataset used in this study contains a total of 85 features, with `Source IP`, `Flow ID`, and `Timestamp` accounting for a significant portion of the variance. However, these features are not suitable for determining ransomware labels due to their nature as metadata. **They are not directly relevant to the network traffic characteristics, lack generalizability, and are subject to frequent changes, making them unreliable indicators for classification.**

Excluding these features leaves the remaining usable features with insufficient variance to effectively distinguish between different types of ransomware. Consequently, the models trained on this dataset fail to achieve high classification accuracy for ransomware detection and type determination.

Interestingly, the high accuracy results observed in some studies cited in the literature review can be attributed to the inclusion of one or more of these metadata features. While such an approach may yield impressive results, it does not provide a robust or generalizable solution for ransomware detection, as these features cannot reliably capture the intrinsic patterns of network traffic associated with ransomware activity.

This highlights a key challenge in developing accurate and scalable models for ransomware detection: the need for meaningful feature engineering and the identification of traffic-specific features that can better represent the underlying patterns without relying on volatile metadata.

## References
1. Bergsma, Wicher (2013). "A bias correction for Cramér's V and Tschuprow's T". Journal of the Korean Statistical Society. 42 (3): 323–328. doi:10.1016/j.jkss.2012.10.002.
2. https://online.stat.psu.edu/stat200/book/export/html/230
2. G. Saporta, Simultaneous Analysis of Qualitative and Quantitative Data (1990), Societa Italiana di Statistica. XXXV riunione scientifica, Padova, Italy. pp.62–72. Ffhal-02513970f.
3. J. Pagès, Analyse factorielle de données mixtes (2004), Revue de statistique appliquée, tome 52, no 4 (2004), p. 93–111

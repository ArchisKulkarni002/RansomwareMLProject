# **RansomwareMLProject**: Ransomware Detection and Network Traffic Analysis Using Machine Learning
*By 
Archis K, M B Ashish, Nitin R*

## Project Overview
This project focuses on the detection and analysis of ransomware within network traffic data sourced from Android devices. With a dataset containing 84 input features and thousands of rows of traffic information, our goal is to classify network activity as either ransomware-related or benign, further categorizing the type of ransomware when present. Given the high dimensionality and complexity of network traffic data, we aim to develop insights into the unique patterns associated with ransomware and identify indicators that can support early threat detection.

In addition to classification, our analysis encompasses understanding the impact of ransomware on network performance, analyzing traffic patterns for potential Command and Control (C2) communication, and identifying significant traffic features that are indicative of ransomware. This project is structured to facilitate effective detection, streamline threat hunting for analysts, and provide an in-depth analysis of how ransomware behaves within a network.

## Dataset Details
Our dataset consists of network traffic data collected from Android devices, with 84 features characterizing various aspects of traffic flow, such as latency, bandwidth usage, packet size, and frequency of connections. A label column classifies each entry detailing the type of ransomware. This dataset enables us to examine network traffic attributes comprehensively and isolate patterns unique to ransomware activity.

>[Dataset: Android Ransomware Detection](https://www.kaggle.com/datasets/subhajournal/android-ransomware-detection)

## Project Objectives and Tasks
The primary objectives of this project are broken down into the following tasks, each aimed at addressing a distinct aspect of ransomware detection and network analysis:

1. **Preprocessing and Exploratory Data Analysis (EDA)**
   - **Goal**: Prepare the dataset for analysis by cleaning and standardizing data, conducting exploratory data analysis to identify key trends, and applying feature selection methods if necessary to improve computational efficiency.

2. **Ransomware Classification Based on Input Data**
   - **Goal**: Classify network traffic data as ransomware or non-ransomware, followed by the identification of specific ransomware types, thereby creating a two-step classification model for precise threat categorization.

3. **Network Traffic Pattern Visualization and Dimensionality Reduction for Threat Hunting**
   - **Goal**: Reduce the dataset’s dimensionality, retaining essential traffic patterns. Visualization techniques and dimensionality reduction (e.g., PCA) will make it easier for analysts to identify and hunt threats by simplifying complex traffic patterns.

4. **Impact Analysis of Ransomware on Network Performance**
   - **Goal**: Analyze how ransomware impacts network performance by measuring factors like increased latency, bandwidth consumption, and packet loss. This analysis will quantify ransomware’s disruptive effects on network efficiency.

5. **Feature Importance for Ransomware Detection**
   - **Goal**: Identify the most significant traffic features that signal ransomware activity. By determining key indicators, we can improve the speed and accuracy of ransomware detection processes.

6. **Traffic Pattern Analysis to Identify Command and Control (C2) Communication**
   - **Goal**: Detect suspicious traffic patterns that suggest communication with a Command and Control (C2) server. Identifying C2 communication patterns is critical for early detection of ransomware activity and can offer insights into the ransomware lifecycle.

7. **Anomaly Detection for Early Ransomware Detection** *(subject to revision)*
   - **Goal**: Implement anomaly detection techniques to identify unusual network traffic patterns that could signify emerging ransomware threats, regardless of whether they are known ransomware types.
## Usable Models
**Classification**
 - Naive Bayes
 - Logistic Regression
 - SVM

**Clustering**
 - K-means/ GMM
 
 **Regression**
 - Random Forest
 - ANN/ MLP
## Expected Outcomes

By the end of this project, we aim to achieve the following:

- **Improved Ransomware Detection**: Enhanced accuracy and efficiency in identifying ransomware traffic using a reduced feature set.
- **Actionable Insights**: Understanding of which network traffic features are most indicative of ransomware activity.
- **Efficient Threat Hunting**: Simplified visualization and analysis through dimensionality reduction, enabling faster and more accurate threat identification.
- **Anomaly Detection Framework**(*subject to revision*): A framework to detect potential ransomware threats based on unusual traffic patterns, aiding in proactive cybersecurity measures.

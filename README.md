# Predicting the NBA Most Valuable Player (MVP)

This project applies machine learning techniques to predict the NBA's Most Valuable Player (MVP). Using various neural network models, the project explores how data-driven approaches can accurately predict MVP outcomes.

## Table of Contents

1. [Introduction](#introduction)
2. [Data Collection](#data-collection)
3. [Data Pre-Processing](#data-pre-processing)
4. [Feature Analysis](#feature-analysis)
5. [Machine Learning Models](#machine-learning-models)
    - [Feedforward Neural Networks (FNN)](#feedforward-neural-networks-fnn)
    - [Convolutional Neural Networks (CNN)](#convolutional-neural-networks-cnn)
    - [Linear Neural Networks (LNN)](#linear-neural-networks-lnn)
    - [Multilayer Perceptrons (MLP)](#multilayer-perceptrons-mlp)
6. [Experiment Design and Evaluation](#experiment-design-and-evaluation)
7. [Results](#results)
8. [Conclusion](#conclusion)
9. [References](#references)

## Introduction

The aim of this project is to determine the most effective machine learning model for predicting the NBA MVP. The models were evaluated on their ability to generalise across unseen data and their overall accuracy, precision, recall, and F1 score.

## Data Collection

Data was collected through manual scraping from [Basketball Reference](https://www.basketball-reference.com). The dataset includes player statistics, team performance, and MVP voting data. The data was processed into CSV files and merged for model training.

## Data Pre-Processing

The dataset was cleaned and formatted to ensure consistency:
- Unnecessary columns and punctuation were removed.
- Duplicate player entries were corrected.
- Datasets were merged to form a single training dataset.

## Feature Analysis

Feature analysis was conducted using:
1. Correlation analysis to identify significant relationships between features.
2. Manual feature selection to reduce complexity and improve performance.
3. Data visualisation for detecting patterns and outliers.

## Machine Learning Models

### Feedforward Neural Networks (FNN)
- Performed well after fine-tuning.
- **Key Metrics:**
  - **Mean Test Loss:** 0.003
  - **Accuracy:** 99.7%

### Convolutional Neural Networks (CNN)
- Data reshaped into a 3D tensor for compatibility.
- Showed satisfactory performance but with signs of overfitting.

### Linear Neural Networks (LNN)
- Limited to modelling linear relationships.
- Unsuitable for this task due to low performance.

### Multilayer Perceptrons (MLP)
- Similar structure to FNNs with more flexibility.
- **Key Metrics:**
  - **Mean Test Loss:** 0.014
  - **Accuracy:** 99.2%

## Experiment Design and Evaluation

Models were trained using cross-validation (5 folds) with evaluation metrics including:
- **Accuracy**
- **Precision**
- **Recall**
- **F1 Score**

Batch sizes and epochs were adjusted to optimise performance.

## Results

- **FNN:** Best overall performance with low loss and high accuracy.
- **CNN:** High accuracy but struggled with generalisation.
- **LNN:** Poor performance, limited flexibility.
- **MLP:** Strong performance, comparable to FNN.

## Conclusion

The Feedforward Neural Network demonstrated the best balance of accuracy, loss, and generalisation, making it the optimal choice for this task.

## References

1. [Basketball Reference](https://www.basketball-reference.com)
2. Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press.
3. Additional references from the project documentation.

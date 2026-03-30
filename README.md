# 🤖 CS50 AI: Artificial Intelligence with Python
> **An Engineering deep-dive into Logic, Probability, and Neural Networks.**

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E9433F?style=for-the-badge&logo=ubuntu&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

---

## 📌 Overview
This repository documents my implementation of Harvard's **CS50 Introduction to Artificial Intelligence**. Developed entirely on **Ubuntu Linux**, these projects transition from classical search heuristics to modern deep learning and natural language processing.

---

## 🏛️ Project Roadmap & Technical Breakdown

### 🔎 0. Search & Heuristics
* **Degrees:** BFS implementation to find shortest paths in large social graphs.
* **Tic-Tac-Toe:** Unbeatable adversarial AI using **Minimax with Alpha-Beta Pruning**.

### 🧠 1. Knowledge Representation
* **Knights & Knaves:** Solving logical puzzles via **Propositional Logic** and model checking.
* **Minesweeper:** A knowledge-based agent that performs **Inference** to make safe moves under constraints.

### 🎲 2. Uncertainty & Probability
* **PageRank:** Ranking web pages using **Markov Chain Monte Carlo** sampling and iterative algebraic methods.
* **Heredity:** Probabilistic inference in **Bayesian Networks** to model genetic trait inheritance.

### ⚙️ 3. Optimization
* **Crossword:** Solving crosswords as a **Constraint Satisfaction Problem (CSP)** using **AC-3 (Arc Consistency)** and backtracking search.

### 📈 4. Machine Learning
* **Shopping:** A **k-Nearest Neighbor (k-NN)** classifier predicting consumer behavior with focus on sensitivity/specificity metrics.
* **Nim:** An AI that masters gameplay through **Reinforcement Learning** (Q-Learning).

### 🖼️ 5. Neural Networks
* **Traffic:** A **Convolutional Neural Network (CNN)** built with **TensorFlow** to classify 43 road sign categories. 
    * *Architecture:* 2D Convolution, Max-Pooling, Flattening, and Dropout for regularization.

### 🗣️ 6. Language (NLP)
* **Parser:** A Natural Language Processor that parses sentences and extracts noun phrases using **Context-Free Grammar (CFG)**.
* **Questions:** An AI that answers questions by performing **TF-IDF (Term Frequency-Inverse Document Frequency)** ranking and document retrieval.

---

## 🐧 Ubuntu / Linux Setup
Optimized for **Ubuntu 22.04/24.04 LTS**.

### 🛠️ Environment Configuration
```bash
# Update system and install Python pip
sudo apt update && sudo apt install python3-pip -y

# Clone the repo
git clone [https://github.com/IfBilal06/cs50ai-problem-sets.git](https://github.com/IfBilal06/cs50ai-problem-sets.git)
cd cs50ai-problem-sets

# Install requirements (TensorFlow, NLTK, OpenCV, etc.)
pip install -r requirements.txt

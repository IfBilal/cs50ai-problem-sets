# 🤖 CS50 AI: Artificial Intelligence with Python
> **From Search Heuristics to Transformer-based Attention Mechanisms.**

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E9433F?style=for-the-badge&logo=ubuntu&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

---

## 📌 Overview
This repository documents my implementations of the **Harvard CS50 AI** curriculum. Developed and tested on **Ubuntu Linux**, these projects cover the full spectrum of AI—from classical search and logical inference to deep learning and modern **Natural Language Processing (NLP)**.

---

## 🏛️ Technical Roadmap

### 🔎 0. Search & Logic
* **Degrees:** Shortest pathfinding in actor social graphs using **BFS**.
* **Tic-Tac-Toe:** Unbeatable AI using **Minimax with Alpha-Beta Pruning**.
* **Minesweeper:** A knowledge-based agent performing **Logical Inference** to clear cells safely.

### 🎲 1. Uncertainty & Optimization
* **PageRank:** Markov Chain Monte Carlo (MCMC) sampling for webpage importance.
* **Heredity:** Probabilistic inference in **Bayesian Networks**.
* **Crossword:** Solving crosswords as a **Constraint Satisfaction Problem (CSP)** using **AC-3 (Arc Consistency)**.

### 📈 2. Learning & Neural Networks
* **Shopping:** **k-Nearest Neighbor (k-NN)** classification for consumer behavior.
* **Nim:** Mastering gameplay through **Reinforcement Learning (Q-Learning)**.
* **Traffic:** A **Convolutional Neural Network (CNN)** built with TensorFlow to classify road signs from images.

### 🗣️ 3. Natural Language Processing (NLP)
* **Parser:** A syntactic analyzer that extracts noun phrases using **Context-Free Grammar (CFG)** and the `nltk` library.
* **Attention:** A deep-dive into the **Transformer Architecture**. This project implements an AI that masks words in a sentence and uses **Attention Weights** to predict the missing words, visualizing how the model "attends" to different parts of the input.

---

## 🐧 Ubuntu / Linux Environment
Optimized for **Ubuntu 22.04/24.04 LTS** on **Lenovo V14 Hardware**.

### 🛠️ System Configuration
```bash
# Ensure your Ubuntu environment is up to date
sudo apt update && sudo apt install python3-pip python3-venv -y

# Clone the repo and enter directory
git clone [https://github.com/IfBilal06/cs50ai-problem-sets.git](https://github.com/IfBilal06/cs50ai-problem-sets.git)
cd cs50ai-problem-sets

# Install dependencies (NLTK, TensorFlow, etc.)
pip install -r requirements.txt

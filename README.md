# 🖼️ Image Classification with Deep Learning

This project applies **deep learning** techniques to classify images from the **CIFAR-10** dataset into 10 categories (e.g., airplane, car, bird, cat).

## 🚀 Project Overview

The goal is to demonstrate **versatility in computer vision** using both **TensorFlow/Keras** and **PyTorch**, including:

- Exploratory Data Analysis (EDA) and data augmentation.
- Model building: baseline CNNs, regularization techniques, and advanced architectures.
- Transfer learning with pre-trained models (VGG, ResNet).
- Model interpretability (Grad-CAM).
- Deployment via **Streamlit**/**Gradio**.

## 📂 Dataset

The project uses the **CIFAR-10** dataset:

- 60,000 color images (32x32 pixels).
- 10 classes: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck.

The dataset is **not stored as .jpg/.png files**, but as binary batches:

- **Keras**: Loaded into memory and saved as `.npy` arrays.
- **PyTorch**: Downloaded as binary batches in `data/raw/cifar-10-batches-py/`.

## 🛠️ Tools and Libraries

- **R**: EDA and data augmentation (`keras`, `ggplot2`).
- **TensorFlow/Keras**: Prototyping and baseline models.
- **PyTorch**: Custom training loops and deeper control.
- **Albumentations**: Advanced data augmentation (PyTorch).
- **Streamlit/Gradio**: Model deployment.
- **Grad-CAM**: Model interpretability.

## 📅 Project Phases

1. **EDA & Data Augmentation** (R + Python)
2. **Modeling with TensorFlow/Keras**
3. **Modeling with PyTorch**
4. **Model Comparison & Interpretability**
5. **Deployment**

---

_This project is part of my data science portfolio. Check out more at [alexmatiasas.github.io](https://alexmatiasas.github.io)._
# CIFAR-10 loads as numpy arrays (Keras) or binary batches (PyTorch).
# The dataset is not distributed as .jpg/.png files.
from tensorflow.keras.datasets import cifar10
import numpy as np
import os

# Define storage path
output_dir = os.path.join(os.path.dirname(__file__), 'raw')
os.makedirs(output_dir, exist_ok=True)

# Load CIFAR-10 dataset
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Save as .npy files
np.save(os.path.join(output_dir, 'x_train.npy'), x_train)
np.save(os.path.join(output_dir, 'y_train.npy'), y_train)
np.save(os.path.join(output_dir, 'x_test.npy'), x_test)
np.save(os.path.join(output_dir, 'y_test.npy'), y_test)

print("CIFAR-10 downloaded and saved in 'data/raw/'")
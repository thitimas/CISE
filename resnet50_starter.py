"""
ResNet50 Starter Template - CISE Workshop
The tutorial content is provided by Hanzhi Yan and Dr. Yu.

Goal: Write a Python program that uses a pre-trained ResNet50 model
to classify an image using ImageNet labels.

Fill in each function below. Don't peek at the solution until you've tried!
"""

import numpy as np
import torch
import torchvision.models as models
from torchvision import transforms
from PIL import Image


# ──────────────────────────────────────────────
# Step 2: Load the pre-trained model
# ──────────────────────────────────────────────
# Create a function load_resnet50() that:
#   1. Loads models.resnet50(...) with ImageNet pre-trained weights
#   2. Sets the model to evaluation mode using model.eval()
#   3. Returns the model

def load_resnet50():
    pass  # Your code here


# ──────────────────────────────────────────────
# Step 3: Define image preprocessing
# ──────────────────────────────────────────────
# Create a function get_transform() using transforms.Compose with:
#   Resize(256)
#   CenterCrop(224)
#   ToTensor()
#   Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

def get_transform():
    pass  # Your code here


# ──────────────────────────────────────────────
# Step 4: Load an image
# ──────────────────────────────────────────────
# Create a function load_image(img_path=None).
#   - If img_path is None, generate a random 224x224 placeholder image
#   - If img_path is provided, open with Image.open(img_path).convert("RGB")

def load_image(img_path=None):
    pass  # Your code here


# ──────────────────────────────────────────────
# Step 5: Run prediction
# ──────────────────────────────────────────────
# Create a function predict(model, transform, image, top_k=5) that:
#   1. Applies the transform to the image
#   2. Adds a batch dimension using .unsqueeze(0)
#   3. Runs the model inside torch.no_grad()
#   4. Converts logits to probabilities using torch.softmax
#   5. Uses torch.topk to get the top predictions
#   6. Returns a list of (class_index, probability) pairs

def predict(model, transform, image, top_k=5):
    pass  # Your code here


# ──────────────────────────────────────────────
# Step 6: Load ImageNet labels
# ──────────────────────────────────────────────
# Create a function load_imagenet_labels(labels_path=None).
#   - If a file path is provided, read labels from the file (one per line)
#   - Otherwise, use: models.ResNet50_Weights.IMAGENET1K_V1.meta["categories"]
# Return a dict mapping int index -> str label

def load_imagenet_labels(labels_path=None):
    pass  # Your code here


# ──────────────────────────────────────────────
# Step 7: Put it all together
# ──────────────────────────────────────────────
# Complete main() to:
#   1. Load the model, transform, and labels
#   2. Load an image (set img_path = None for a random placeholder,
#      or provide a real path e.g. "dog.jpg")
#   3. Run prediction
#   4. Print the top-5 results in this format:
#
#      Loading ResNet50...
#      Image size: ...
#      Running inference...
#
#      Top-5 predictions:
#      1. [class index] label   probability
#      2. [class index] label   probability
#      ...

def main():
    img_path = None  # Replace with a real image path to use your own image
    pass  # Your code here


if __name__ == "__main__":
    main()

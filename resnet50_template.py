"""
ResNet50 Template - Basic ImageNet Classification
"""
import numpy as np
import torch
import torchvision.models as models
from torchvision import transforms
from PIL import Image


# ──────────────────────────────────────────────
# 1. Load pre-trained ResNet50
# ──────────────────────────────────────────────

def load_resnet50():
    """Load ImageNet pre-trained ResNet50 and set to eval mode."""
    model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V1)
    model.eval()
    return model


# ──────────────────────────────────────────────
# 2. Standard ImageNet preprocessing pipeline
# ──────────────────────────────────────────────

def get_transform():
    """Return the standard ImageNet preprocessing transform."""
    return transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225],
        ),
    ])


# ──────────────────────────────────────────────
# 3. Load an image
# ──────────────────────────────────────────────

def load_image(img_path=None):
    """
    Load an RGB image.

    Args:
        img_path: Path to an image file.  If None, a random 224×224
                  placeholder is returned instead (for quick testing).

    Returns:
        PIL.Image in RGB mode.
    """
    if img_path is None:
        # Random placeholder — useful for smoke-testing without real data
        random_array = (np.random.rand(224, 224, 3) * 255).astype(np.uint8)
        return Image.fromarray(random_array)
    return Image.open(img_path).convert("RGB")


# ──────────────────────────────────────────────
# 4. Run inference
# ──────────────────────────────────────────────

def predict(model, transform, image, top_k=5):
    """
    Run a forward pass and return the top-k predictions.

    Args:
        model:     ResNet50 (eval mode).
        transform: Preprocessing transform from get_transform().
        image:     PIL.Image (RGB).
        top_k:     Number of top predictions to return.

    Returns:
        List of (class_index, probability) tuples, highest-prob first.
    """
    tensor = transform(image).unsqueeze(0)   # (1, 3, 224, 224)

    with torch.no_grad():
        logits = model(tensor)               # (1, 1000)

    probs = torch.softmax(logits, dim=1)[0]
    top_probs, top_indices = torch.topk(probs, top_k)

    return [(idx.item(), prob.item()) for idx, prob in zip(top_indices, top_probs)]


# ──────────────────────────────────────────────
# 5. (Optional) Map class index → human-readable label
# ──────────────────────────────────────────────

def load_imagenet_labels(labels_path=None):
    """
    Load ImageNet class labels.

    Args:
        labels_path: Path to a text file with 1000 class names (one per line).
                     If None, falls back to torchvision's built-in mapping.

    Returns:
        dict mapping int index → str label.
    """
    if labels_path is not None:
        with open(labels_path) as f:
            labels = [line.strip() for line in f]
        return {i: label for i, label in enumerate(labels)}

    # Built-in fallback via torchvision meta
    meta = models.ResNet50_Weights.IMAGENET1K_V1.meta
    return {i: name for i, name in enumerate(meta["categories"])}


# ──────────────────────────────────────────────
# 6. Main — put it all together
# ──────────────────────────────────────────────

def main():
    print("Loading ResNet50 (ImageNet pre-trained)...")
    model = load_resnet50()
    transform = get_transform()
    labels = load_imagenet_labels()

    # ── Replace None with a real path, e.g. "dog.jpg", to use your own image ──
    img_path = None
    image = load_image(img_path)
    print(f"Image size: {image.size}  (using {'random placeholder' if img_path is None else img_path})")

    print("\nRunning inference...")
    predictions = predict(model, transform, image, top_k=5)

    print("\nTop-5 predictions:")
    for rank, (class_idx, prob) in enumerate(predictions, start=1):
        label = labels.get(class_idx, f"class_{class_idx}")
        print(f"  {rank}. [{class_idx:4d}] {label:<40s}  {prob*100:.2f}%")


if __name__ == "__main__":
    main()

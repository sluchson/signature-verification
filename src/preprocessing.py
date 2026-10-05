import numpy as np
import cv2
from PIL import Image

INPUT_SIZE = (128, 256)
INK_TARGET = 100


def load_gray(path):
    return np.array(Image.open(path).convert("L"))


def remove_background(img):
    threshold, _ = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    result = img.copy()
    result[img > threshold] = 255
    return result, threshold


def crop_to_signature(img):
    mask = img < 255
    if not mask.any():
        return img
    rows = np.where(mask.any(axis=1))[0]
    cols = np.where(mask.any(axis=0))[0]
    return img[rows[0]:rows[-1] + 1, cols[0]:cols[-1] + 1]


def normalize_ink(img, target=INK_TARGET):
    mask = img < 255
    if not mask.any():
        return img
    darkness = 255.0 - img.astype(np.float32)
    current = np.median(darkness[mask])
    darkness = darkness * ((255.0 - target) / current)
    result = 255.0 - darkness
    return np.clip(result, 0, 255).astype(np.uint8)


def fit_to_size(img, size=INPUT_SIZE):
    target_h, target_w = size
    h, w = img.shape
    scale = min(target_h / h, target_w / w)
    new_h = max(1, round(h * scale))
    new_w = max(1, round(w * scale))
    interpolation = cv2.INTER_AREA if scale < 1 else cv2.INTER_LINEAR
    resized = cv2.resize(img, (new_w, new_h), interpolation=interpolation)
    canvas = np.full((target_h, target_w), 255, dtype=np.uint8)
    top = (target_h - new_h) // 2
    left = (target_w - new_w) // 2
    canvas[top:top + new_h, left:left + new_w] = resized
    return canvas


def preprocess(path, size=INPUT_SIZE):
    img = load_gray(path)
    img, _ = remove_background(img)
    img = crop_to_signature(img)
    img = normalize_ink(img)
    return fit_to_size(img, size)
import cv2
import json
import numpy as np
import sys

TOLERANCES = {
    "blur": 0.7,        # 70% of reference allowed
    "color": 80.0,      # Euclidean RGB distance
    "centroid": 12.0    # pixels
}

def extract_features(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # --- Blur ---
    blur = cv2.Laplacian(gray, cv2.CV_64F).var()

    # --- Color ---
    color = image.mean(axis=(0, 1))

    # --- Layout (TEXT REGION ONLY) ---
    h, w = gray.shape

    # Region where text exists (tuned for your design)
    roi = gray[int(0.15*h):int(0.45*h), int(0.05*w):int(0.6*w)]

    edges = cv2.Canny(roi, 100, 200)
    ys, xs = np.where(edges > 0)

    if len(xs) == 0:
        centroid = np.array([0, 0])
    else:
        centroid = np.array([xs.mean(), ys.mean()])

    return blur, color, centroid



with open("reference/reference.json") as f:
    ref = json.load(f)

ref_blur = ref["blur"]
ref_color = np.array(ref["color"])
ref_centroid = np.array(ref["centroid"])

image_path = sys.argv[1]
img = cv2.imread(image_path)

blur, color, centroid = extract_features(img)

if blur < ref_blur * TOLERANCES["blur"]:
    print("COUNTERFEIT: Low print quality")
    exit()

if np.linalg.norm(color - ref_color) > TOLERANCES["color"]:
    print("COUNTERFEIT: Ink / color mismatch")
    exit()

if np.linalg.norm(centroid - ref_centroid) > TOLERANCES["centroid"]:
    print("COUNTERFEIT: Layout deviation")
    exit()

print("PASSED AI VERIFICATION → Send to blockchain")

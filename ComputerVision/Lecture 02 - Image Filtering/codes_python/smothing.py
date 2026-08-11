import cv2
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------
# 1. Load image
# -------------------------------------------------------
img = cv2.imread("blur.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# -------------------------------------------------------
# 2. Add the SAME Gaussian noise
# -------------------------------------------------------
np.random.seed(42)

sigma_noise = 25
noise = np.random.normal(0, sigma_noise, img.shape).astype(np.float32)

noisy = img.astype(np.float32) + noise
noisy = np.clip(noisy, 0, 255).astype(np.uint8)

# -------------------------------------------------------
# 3. Apply smoothing filters to the SAME noisy image
# -------------------------------------------------------

# Mean filter
mean_filtered = cv2.blur(noisy, (7, 7))

# Gaussian filter
gaussian_filtered = cv2.GaussianBlur(
    noisy,
    (7, 7),
    sigmaX=1.5
)

# Median filter
median_filtered = cv2.medianBlur(noisy, 7)

# Bilateral filter
bilateral_filtered = cv2.bilateralFilter(
    noisy,
    d=9,
    sigmaColor=50,
    sigmaSpace=50
)

# -------------------------------------------------------
# 4. Organize data for plotting
# -------------------------------------------------------
filters = [
    ("Mean Filter", mean_filtered),
    ("Gaussian Filter", gaussian_filtered),
    ("Median Filter", median_filtered),
    ("Bilateral Filter", bilateral_filtered),
]

# -------------------------------------------------------
# 5. Plot: Original -> Same Noisy Image -> Filtered Result
# -------------------------------------------------------
fig, axes = plt.subplots(
    nrows=4,
    ncols=3,
    figsize=(16, 16)
)

for row, (filter_name, filtered) in enumerate(filters):

    axes[row, 0].imshow(img)
    axes[row, 0].set_title("Original Image", fontsize=14, fontweight="bold")
    axes[row, 0].axis("off")

    axes[row, 1].imshow(noisy)
    axes[row, 1].set_title("Noisy Image (Gaussian Noise)",
                           fontsize=14,
                           fontweight="bold")
    axes[row, 1].axis("off")

    axes[row, 2].imshow(filtered)
    axes[row, 2].set_title(filter_name,
                           fontsize=14,
                           fontweight="bold")
    axes[row, 2].axis("off")

plt.suptitle(
    "Smoothing Filters — Same Input, Same Noise",
    fontsize=22,
    fontweight="bold",
    y=0.995
)

plt.tight_layout()

# Full HD output
plt.savefig(
    "smoothing_filters_comparison.png",
    dpi=150,
    bbox_inches="tight"
)

plt.savefig("/home/aghochuli/Desktop/smoothing_filters_comparison.png", dpi=150)

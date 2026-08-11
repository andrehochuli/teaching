import cv2
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------
# 1. Load image
# -------------------------------------------------------
img = cv2.imread("blur.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# -------------------------------------------------------
# 2. EDGE DETECTION
#    Sobel gradient magnitude
# -------------------------------------------------------
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

edge = np.sqrt(sobel_x**2 + sobel_y**2)
edge = cv2.normalize(edge, None, 0, 255, cv2.NORM_MINMAX)
edge = edge.astype(np.uint8)

# -------------------------------------------------------
# 3. SHARPENING
#    Unsharp masking
# -------------------------------------------------------
blurred = cv2.GaussianBlur(img, (0, 0), sigmaX=2)

sharpened = cv2.addWeighted(
    img,      1.8,     # original image
    blurred, -0.8,     # subtract blurred component
    0
)

# -------------------------------------------------------
# 4. Display side by side
# -------------------------------------------------------
fig, axes = plt.subplots(1, 4, figsize=(20, 8))

axes[0].imshow(img)
axes[0].set_title("Original Image", fontsize=15, fontweight="bold")
axes[0].axis("off")

axes[1].imshow(edge, cmap="gray")
axes[1].set_title("Edge Detection (Sobel)", fontsize=15, fontweight="bold")
axes[1].axis("off")

axes[2].imshow(sharpened)
axes[2].set_title("Sharpening (Unsharp Masking)", fontsize=15, fontweight="bold")
axes[2].axis("off")

plt.tight_layout()
plt.savefig("sharpen.png")


gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# -------------------------------------------------------
# 2. SOBEL
# -------------------------------------------------------
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

sobel = np.sqrt(sobel_x**2 + sobel_y**2)
sobel = cv2.normalize(sobel, None, 0, 255, cv2.NORM_MINMAX)
sobel = sobel.astype(np.uint8)

# -------------------------------------------------------
# 3. PREWITT
# -------------------------------------------------------
kernel_x = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
], dtype=np.float32)

kernel_y = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
], dtype=np.float32)

prewitt_x = cv2.filter2D(gray, cv2.CV_32F, kernel_x)
prewitt_y = cv2.filter2D(gray, cv2.CV_32F, kernel_y)

prewitt = np.sqrt(prewitt_x**2 + prewitt_y**2)
prewitt = cv2.normalize(prewitt, None, 0, 255, cv2.NORM_MINMAX)
prewitt = prewitt.astype(np.uint8)

# -------------------------------------------------------
# 4. LAPLACIAN
# -------------------------------------------------------
laplacian = cv2.Laplacian(gray, cv2.CV_64F, ksize=3)

# Take magnitude to visualize both positive and negative responses
laplacian = np.abs(laplacian)
laplacian = cv2.normalize(
    laplacian, None, 0, 255, cv2.NORM_MINMAX
)
laplacian = laplacian.astype(np.uint8)

# -------------------------------------------------------
# 5. Display
# -------------------------------------------------------
fig, axes = plt.subplots(1, 4, figsize=(18, 5))

axes[0].imshow(gray, cmap="gray")
axes[0].set_title("Original Image", fontsize=14, fontweight="bold")
axes[0].axis("off")

axes[1].imshow(sobel, cmap="gray")
axes[1].set_title("Sobel", fontsize=14, fontweight="bold")
axes[1].axis("off")

axes[2].imshow(prewitt, cmap="gray")
axes[2].set_title("Prewitt", fontsize=14, fontweight="bold")
axes[2].axis("off")

axes[3].imshow(laplacian, cmap="gray")
axes[3].set_title("Laplacian", fontsize=14, fontweight="bold")
axes[3].axis("off")

plt.tight_layout()
plt.savefig("edges.png")
import os, cv2
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from sklearn.metrics.pairwise import cosine_similarity
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing import image

# ==========================================
# 1️⃣  SET YOUR DATASET PATH
# ==========================================
DATASET_PATH = r"data"  # 🔹 Folder name for dataset

# ==========================================
# 2️⃣  LOAD MODEL (lightweight for laptops)
# ==========================================
model = MobileNetV2(weights="imagenet", include_top=False, pooling='avg')

# ==========================================
# 3️⃣  EXTRACT FEATURES (only once)
# ==========================================
features_file = "fashion_features.npy"
filenames_file = "fashion_filenames.npy"

if not os.path.exists(features_file):
    print("⏳ Extracting features... please wait")
    features = []
    filenames = []

    for file in tqdm(os.listdir(DATASET_PATH)):
        if file.lower().endswith(('.jpg', '.png', '.jpeg')):
            img_path = os.path.join(DATASET_PATH, file)
            img = image.load_img(img_path, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = preprocess_input(img_array)

            feature = model.predict(img_array, verbose=0)
            features.append(feature.flatten())
            filenames.append(img_path)

    features = np.array(features)
    np.save(features_file, features)
    np.save(filenames_file, filenames)
    print("✅ Features extracted and saved successfully!")
else:
    print("📂 Loading pre-saved features...")
    features = np.load(features_file)
    filenames = np.load(filenames_file, allow_pickle=True)

# ==========================================
# 4️⃣  FIND & DISPLAY SIMILAR IMAGES
# ==========================================
def show_similar_images(img_path, top_n=5):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    feature = model.predict(img_array, verbose=0).flatten()

    similarities = cosine_similarity([feature], features)[0]
    indices = np.argsort(similarities)[::-1][:top_n]

    plt.figure(figsize=(15, 5))
    plt.subplot(1, top_n + 1, 1)
    plt.imshow(image.load_img(img_path))
    plt.title("Input Image")
    plt.axis('off')

    for i, idx in enumerate(indices):
        plt.subplot(1, top_n + 1, i + 2)
        plt.imshow(image.load_img(filenames[idx]))
        plt.title(f"Similar {i+1}")
        plt.axis('off')

    plt.show()

# ==========================================
# 5️⃣  USER INPUT AT RUNTIME
# ==========================================
print("\n🧥 Welcome to the Fashion Recommendation System 🧥")


user_input = input("👉 Enter the image number: ").strip()
test_img = os.path.join(DATASET_PATH, user_input)

if os.path.exists(test_img):
    print(f"🎯 Finding similar images for: {test_img}")
    show_similar_images(test_img, top_n=5)
else:
    print("❌ File not found! Please check the filename and try again.")

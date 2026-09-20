import os
import shutil
import random

# ✅ FIXED HERE
original_dataset = "datasets"
base_dir = "processed_dataset"

train_ratio = 0.8

classes = ["normal", "glaucoma", "diabetic_retinopathy", "cataract"]

for cls in classes:
    os.makedirs(os.path.join(base_dir, "train", cls), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "test", cls), exist_ok=True)

    images = os.listdir(os.path.join(original_dataset, cls))
    random.shuffle(images)

    split_index = int(len(images) * train_ratio)

    train_images = images[:split_index]
    test_images = images[split_index:]

    for img in train_images:
        src = os.path.join(original_dataset, cls, img)
        dst = os.path.join(base_dir, "train", cls, img)
        shutil.copyfile(src, dst)

    for img in test_images:
        src = os.path.join(original_dataset, cls, img)
        dst = os.path.join(base_dir, "test", cls, img)
        shutil.copyfile(src, dst)

print("Dataset Split Completed!")
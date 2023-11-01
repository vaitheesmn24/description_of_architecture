import os
import numpy as np
import tensorflow as tf
import pandas as pd
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from sklearn.metrics.pairwise import cosine_similarity

def load_and_preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

def extract_image_features(image_path, model):
    img_array = load_and_preprocess_image(image_path)
    features = model.predict(img_array)
    return features.flatten()

def compute_cosine_similarity(vector1, vector2):
    return cosine_similarity([vector1], [vector2])[0][0]

def main(database_path,query_image_path):
    # Load the pre-trained ResNet50 model
    model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

    # Directory path where the database of images is stored
    # database_path = "D:\CV\Flowchart\Icons/"

    # Path to the query image
    # query_image_path = r"D:\CV\Flowchart\test\active directory (2).jpg"

    # Load and extract features from the query image
    query_features = extract_image_features(query_image_path, model)

    # Initialize lists to store image filenames and similarity scores
    filenames = []
    similarities = []

    # Loop through the images in the database directory and compute similarities
    for filename in os.listdir(database_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(database_path, filename)
            features = extract_image_features(image_path, model)
            similarity = compute_cosine_similarity(query_features, features)
            filenames.append(filename)
            similarities.append(similarity)

    # Create a DataFrame to store the results
    data = {
        "Services": filenames,
        "Similarity": similarities
    }
    df = pd.DataFrame(data)

    # Sort the DataFrame based on similarity in descending order
    df = df.sort_values(by="Similarity", ascending=False)

    # Keep only the top 5 images with highest similarities
    top10_df = df.head(10)

    # Reset the index of the DataFrame for a cleaner display
    top10_df = top10_df.reset_index(drop=True)

    # Print the DataFrame with top 10 similar images
    print(top10_df)

# Extract the filename with the highest similarity and its score
    top_match_filename = df.iloc[0]["Services"]
    top_match_score = df.iloc[0]["Similarity"]


    # Print the filename with the highest similarity and its score
    top_service = top_match_filename.split(".")[0]
    return f"{top_service}"
    
    




from sklearn.ensemble import RandomForestClassifier
import pickle

def generate_skincare_routine(user_data):
    # Dummy model for skincare routine generation
    # In a real-world scenario, the model would be trained on skincare datasets
    model = RandomForestClassifier()
    # Assume the model has been trained and saved, here we're loading it for predictions
    with open('ml/skincare_model.pkl', 'rb') as f:
        model = pickle.load(f)

    # Creating a feature vector based on user input (this should be improved)
    feature_vector = [user_data.age, user_data.skin_type, user_data.concerns, user_data.lifestyle, user_data.allergies]
    
    prediction = model.predict([feature_vector])
    return prediction

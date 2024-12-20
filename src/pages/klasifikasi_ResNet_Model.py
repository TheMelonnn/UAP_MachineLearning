import streamlit as st
import tensorflow as tf
from pathlib import Path
import numpy as np

if st.button("Back to Home"):
    st.session_state.predictions = None
    st.switch_page("landingpage.py")

st.title("Its your tomato healthy? :tomato: (Using ResNet Model)")
upload = st.file_uploader(
    'Upload your tomato leaf image here', 
    type=['png','jpg'])

if "predictions" not in st.session_state:
    st.session_state.predictions = None

def predict():
    class_names = ['Tomato___Bacterial_spot',
                    'Tomato___Early_blight',
                    'Tomato___Late_blight',
                    'Tomato___Leaf_Mold',
                    'Tomato___Septoria_leaf_spot',
                    'Tomato___Spider_mites Two-spotted_spider_mite',
                    'Tomato___Target_Spot',
                    'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
                    'Tomato___Tomato_mosaic_virus',
                    'Tomato___healthy']

    img = tf.keras.utils.load_img(upload, target_size=(256, 256, 3))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    
    model = tf.keras.models.load_model(Path(__file__).parent / 
    "model/Res_Net_tomatoleaf.h5")
    output = model.predict(img_array)
    score = tf.nn.softmax(output[0])
    print(score)
    return class_names[np.argmax(score)]

if st.button('Predict'):
    if upload is not None:
        st.image(upload)
        st.subheader('Predictions:')
        with st.spinner('Predicting...'):
            st.session_state.predictions = predict()
        st.write(st.session_state.predictions)
        st.write(" ")
        st.write("Is it correct? Please let us know by clicking the feedback below.")

    else:
        st.write('Please upload an image')

if st.session_state.predictions is not None:
    sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
    selected = st.feedback("thumbs")
    if selected is not None:
        if selected == 0:
            st.write("Sorry to hear that! We will improve our model.")
            st.session_state.predictions = None

        if selected == 1:
            st.write("Thank you for your feedback! Have a nice day :D")
            st.session_state.predictions = None
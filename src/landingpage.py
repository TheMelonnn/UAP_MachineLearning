import streamlit as st
import numpy as np

st.title("Its your Tomato :tomato: Healthy?")

st.write("Check your tomato :tomato: healthiness in our web based app now!")
st.image("https://www.southernliving.com/thmb/_W9FrEAhu1Hw_vfWniE0ACUerrQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/tomato-garden-2000-d3de7267d65c442b987c67c6e43e5e1e.jpg")
st.write(" ")

st.subheader("About our app :tomato:")
st.write("Healtiness of tomato is important to gardener that has started to plant tomato recently. Sometimes, they don't know how to check the healthiness of the tomato. So, we provide this app to help gardener to check the healthiness of the tomato. Just upload the image of your tomato and we will classify it for you!",)
st.write(" ")

st.subheader("About Our Model :eye:")
st.write("Our model is using Convolutional Neural Network (CNN) technology to classify the healthiness of the tomato. We use pretrained model from TensorFlow called DenseNet121 and ResNet101 to make sure the accuracy of the model. The model has been trained using 11.000 images of tomato with 10 different classes from kaustubhb999 tomatoleaf datasets. You can learn more about the model and the dataset by clicking button below.")

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.link_button(url="https://www.tensorflow.org/api_docs/python/tf/keras/applications/DenseNet121", label="DenseNet121")
with col2:
    st.link_button(url="https://www.tensorflow.org/api_docs/python/tf/keras/applications/ResNet101", label="ResNet101")
st.write(" ")

st.subheader("DenseNet121 vs Resnet101 :bar_chart:")
st.write("DenseNet121 and ResNet101 are both pretrained model from TensorFlow that can be used for image classification. Both models have their own advantages and disadvantages. From our research, this is the performance different between DenseNet121 and ResNet101:")
col1, col2 = st.columns(2)
with col1:
    st.image("assets/Densenet_Accuracy.png", caption="DenseNet121 Accuracy")
with col2:
    st.image("assets/Resnet_Accuracy.png", caption="ResNet101 Accuracy")

col1, col2 = st.columns(2)
with col1:
    st.image("assets/Densenet_Loss.png", caption="DenseNet121 Loss")
with col2:
    st.image("assets/Resnet_Loss.png", caption="ResNet101 Loss")

st.write("From the image above, we can see that DenseNet121 has better accuracy and performance than ResNet101. But, ResNet101 isn't bad either. It still need some improvement to make it better. You can try both models in our app to see the difference between them.")
st.write(" ")

st.subheader("About the Dataset :file_folder:")

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.image('https://www.tomatobible.com/wp-content/uploads/2022/03/pruning-tomatoes-peppers-6174-1.jpg.webp')
with col2:
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQoqI0OQvi3XIzjqXnABcPlFtuyAFWt6agCrw&s')
with col3:
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScw6wfwywY_XvF2WU8waJyqd6J57W97VSWDA&s')
with col4:
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTiGXm5JN8Tb7-Nh-Q644x56eH_Q4ui9yvgOg&s')
with col5:
    st.image('https://cdn.mos.cms.futurecdn.net/HUNQy44pDSpeJQ9jaTKdLK.jpg')

st.write("The dataset contains 10 classes of tomato leaf diseases and healthy leaves. The dataset contains 11.000 images of tomato leaves with 10 different classes. The dataset is divided into 10000 training and 1000 testing. The dataset classes are listed below:")
st.markdown("1. Tomato_Mosaic_Virus")
st.markdown("2. Target_Spot")
st.markdown("3. Bacterial_Spot")
st.markdown("4. Tomato_Yellow_Leaf_Curl_Virus")
st.markdown("5. Late_Blight")
st.markdown("6. Leaf_Mold")
st.markdown("7. Early_Blight")
st.markdown("8. Spider_Mites Two-Spotted Spider Mite")
st.markdown("9. Tomato___Healthy")
st.markdown("10. Septoria_Leaf_Spot")
st.write("The dataset is available on Kaggle and you can download it by clicking the button below.")
st.link_button(url="https://www.kaggle.com/kaustubhb999/tomatoleaf", label="Download Dataset")
st.write(" ")

st.subheader("Want to Classify Your Tomato Healtiness? :tomato:")
st.write("Click the button below to classify your tomato healthiness yourself!")
if st.button("DenseNet121"):
    st.switch_page("pages/klasifikasi_DenseNet_Model.py")
if st.button("ResNet101"):
    st.switch_page("pages/klasifikasi_ResNet_Model.py")
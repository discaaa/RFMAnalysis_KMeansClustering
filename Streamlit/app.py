# import streamlit as st
# import pandas as pd
# import pickle
# import matplotlib.pyplot as plt
# from pages import homepage, edapage, inputpage, modelpage, evaluationpage, resultpage

# # Sidebar Menu
# menu = st.sidebar.selectbox(
#     "Menu", ["Home", "Exploratory Data Analysis", "Input Data", "Model", "Evaluation", "Result"]
# )


# # Home Page
# if menu == "Home":
#     homepage.show()

# # EDA Page
# elif menu == "Exploratory Data Analysis":
#     edapage.show()

# # Input Data Page
# elif menu == "Input Data":
#     inputpage.show()

# # Model Page
# elif menu == "Model":
#     modelpage.show()

# # Evaluation Page
# elif menu == "Evaluation":
#     evaluationpage.show()

# # Result Page
# elif menu == "Result":
#     resultpage.show()

# # st.set_page_config(page_title="Basic Inputs", page_icon='😊')

# # st.title("Basic Inputs")
# # st.header("Text Input")
# # text1 = st.text_input("Input your name: ")
# # st.write(f'Name: {text1}')

# # st.header("Number Input")
# # number1 = st.number_input("Input your age: ")
# # st.write(f'Age: {number1}')

# # st.header("Select Box")
# # model_choice = st.selectbox(
# #     "Select the Model Type",
# #     ['Linear Regression', 'Decision Tree', 'Random Forest']
# # )
# # st.write(f'Model Choice: {model_choice}')
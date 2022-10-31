from git import Head
import streamlit as st
import pandas as pd
import altair as alt


# Import ML Libraries & Packages
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error






header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()


#Needs to be updated, but I think it's something that I want to  keep
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )


with header:
    st.title('Laney Media Analytics Dashboard')

    uploaded_file = st.file_uploader("Upload Analytics from Content Plan")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df.head())
    

with dataset:
    st.header('Dashboard')
    st.text(' test test test')

    col1, col2 = st.columns(2)
with col1:
    ticker_dx = st.slider(
        "Video Views", min_value=0, max_value=10000000, step=1, value=0
    )
with col2:
    ticker_dy = st.slider(
        "Watch Time Percentage", min_value=0, max_value=100, step=1, value=-10
    )

    #video_views = df[['POST DATE & TIME','VIEWS AFTER 48 HRS']]
    #video_views = pd.DataFrame(df['VIEWS AFTER 48 HRS(number)']).head(10)
    #st.bar_chart(video_views)
    #st.line_chart(data=None, *, x=None, y=None, width=0, height=0, use_container_width=True)

    #clickup_data = pd.read_csv('')

    

with features:
    st.header('Best Preforming Content')

    tab1, tab2, tab3 = st.tabs(["TikTok:Kenda.Laney", "TikTok:SMM", "Youtube"])

    with tab1:
        st.header("TikTok: kenda.laney")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

    with tab2:
        st.header("TikTok: SMM")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

    with tab3:
        st.header("Youtube: Kenda Laney")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)





with model_training:
    st.header('Predicting Views')
    st.text('In this section you can select the hyperparameters!')

    selection_col, display_col = st.beta_columns(2)

    max_depth = selection_col.slider('What should be the max_depth of the model?', 
    min_value=10, 
    max_value=100, 
    value=20, 
    step=10)

    number_of_trees = selection_col.selectbox('How many trees should there be?', 
    options=[100,200,300,'No limit'], 
    index=0)

    selection_col.text('Here is a list of features: ')
    selection_col.write(df.columns)
    input_feature = selection_col.text_input
    ('Which feature would you like to input to the model?', 
    'PULocationID')

     

    

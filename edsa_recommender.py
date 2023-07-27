"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px 

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model
import base64
from pathlib import Path

st.session_state.model = 'SVD'

# styling
app_style = """
<style>

</style>

"""

st.markdown(app_style, unsafe_allow_html=True)

# convert image to text readable
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
def img_to_html(img_path):
    img_html = "<img src='data:image/png;base64,{}' class='img-fluid' style='border-radius: 50%; width: 100%'>".format(
      img_to_bytes(img_path)
    )
    return img_html

# set app background
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
        <style>
            .stApp {{
                background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
                background-size: cover
            }}
        </style>
    """,
    unsafe_allow_html=True
    )

#add_bg_from_local('resources/imgs/moviebg.jpg')

# Data Loading
title_list = load_movie_titles('/home/explore-student/unsupervised_data/edsa-movie-recommendation-predict/movies.csv')
hist_data = pd.read_csv('/home/explore-student/unsupervised_data/edsa-movie-recommendation-predict/train.csv')
# title_list = load_movie_titles('movies.csv')
# hist_data = pd.read_csv('train.csv')
df_ratings = pd.read_csv('resources/data/df_ratings.csv', encoding = "latin_1")
df_genre_freq = pd.read_csv("resources/data/PieChartData.csv")
df_genre_rating = pd.read_csv("resources/data/df_genres_average_ratings.csv")
actors_df = pd.read_csv("resources/data/actor_ratings_to_plot.csv", encoding = "latin_1")


# App declaration
def main():
#     import sys
    
#     sys.path.append("some_path")
#     st.write(sys.executable)
#     st.write(sys.path)
#     st.write(1)
    
    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Solution Overview","Recommender Settings","Analytics","About Us","App Feedback"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[:])
        movie_2 = st.selectbox('Second Option',title_list[:])
        movie_3 = st.selectbox('Third Option',title_list[:])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                #try:
                with st.spinner('Crunching the numbers...'):
                    top_recommendations = content_model(movie_list=fav_movies,
                                                        top_n=10)
                st.title("We think you'll like:")
                for i,j in enumerate(top_recommendations):
                    st.subheader(str(i+1)+'. '+j)
#                 except:
#                     st.error("Oops! Looks like this algorithm does't work.\
#                               We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                #try:
                with st.spinner('Crunching the numbers...'):
                    top_recommendations = collab_model(movie_list=fav_movies,
                                                       top_n=10)
                st.title("We think you'll like:")
                for i,j in enumerate(top_recommendations):
                    st.subheader(str(i+1)+'. '+j)
                #except:
                #    st.error("Oops! Looks like this algorithm does't work.\
                #              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        #st.title("Solution Overview")
        #st.write("Describe your winning approach on this page")
        
        #st.title("ReelGenius")
        #st.header('This is a header')
        st.image('resources/imgs/2.png')
        st.header('Problem Statement')
        st. write('''Recommender systems have become crucial in today's technology-driven world, enabling individuals to make informed choices about the content they engage with regularly. Movie content recommendations are particularly important in this regard, as intelligent algorithms can assist viewers in discovering great titles from a vast selection of options.''')
        
        with st.expander("**Business Value**"):
            st.write('**Enhanced User Experience:**')
            st.write('''Recommender systems enhance the user experience by providing personalized recommendations tailored to individual preferences. By suggesting relevant and interesting movies, users are more likely to engage with the platform and discover content they enjoy. This leads to increased user satisfaction and a higher likelihood of repeat visits.''')
            st.divider()
            st.write('**Increased User Engagement:**')
            st.write('''A well-designed recommender system increases user engagement by capturing and understanding user preferences. By analyzing historical data, the system can identify patterns, preferences, and user behavior, thereby presenting users with movies that align with their interests. Increased user engagement translates to longer session durations, more frequent visits, and higher user retention rates.''')
            st.divider()
            st.write('**Improved Customer Satisfaction:**')
            st.write('''Recommender systems help users discover movies they are likely to enjoy but might have otherwise missed. By providing accurate and relevant recommendations, users feel satisfied and perceive the platform as valuable. This satisfaction leads to positive word-of-mouth recommendations, increased customer loyalty, and reduced churn rates.''')
            st.divider()
            st.write('**Revenue Generation:**')
            st.write('''A well-executed recommender system can have a significant impact on revenue generation. By showcasing relevant movie recommendations, users are more likely to engage with the platform, leading to increased content consumption and potential revenue streams such as subscriptions, rentals, or advertising. Additionally, recommender systems can leverage personalized recommendations to upsell or cross-sell related products or services, further increasing revenue opportunities.''')
            st.divider()
            st.write('**Data-Driven Decision Making:**')
            st.write('''Building a recommender system requires collecting and analyzing vast amounts of user data. This data can provide valuable insights into user preferences, trends, and behavior, enabling data-driven decision making for content acquisition, production, and marketing strategies. By leveraging the knowledge gained from the recommender system, platforms can make informed decisions to optimize their movie catalog and marketing efforts.''')
            st.divider()
            st.write('**Competitive Advantage:**')
            st.write('''In today's competitive landscape, a well-implemented recommender system can serve as a differentiating factor for platforms. By providing accurate and personalized recommendations, platforms can attract new users and retain existing ones, positioning themselves as leaders in the industry. This competitive advantage can result in increased market share, brand recognition, and growth opportunities.''')
        st.header('Solution')
        st.write('''The ReelDeal: Your Ultimate Movie Recommender App!

Are you tired of endlessly scrolling through streaming platforms, trying to find the perfect movie to watch? Look no further! The ReelDeal is here to revolutionize your movie-watching experience with its advanced recommendation system that caters for collaborative and content filtering techniques.''')
        
        tab1, tab2 = st.tabs(["Content Filtering", "Colaborative Filtering"])

        with tab1:
            st.header("Content Filtering")
            st.write('''The app utilizes content filtering, which focuses on the characteristics and attributes of movies themselves. By analyzing the content, genre, actors, directors, and other metadata associated with movies, the app can provide recommendations based on your personal preferences and interests. Whether you're a fan of action-packed blockbusters, romantic comedies, or indie dramas, The app will suggest movies that align with your specific tastes.''')
            st.image('resources/imgs/Content.png',use_column_width=True)
            with st.expander("**Advantages/Disadvantages**"):
                st.write('''**Advantages:**''')
                st.write('''1. The model's recommendations are personalized to each user, eliminating the need for data on other users. This enables easy scalability to a large user base.''')
                st.write('''2. By capturing the specific interests of users, the model can suggest niche items that appeal to a small subset of users, resulting in more tailored recommendations.''')
                st.divider()
                st.write('''**Disadvantages:**''')
                st.write('''1. This technique relies on hand-engineered feature representations for items, requiring substantial domain knowledge. Consequently, the effectiveness of the model is limited by the quality of these engineered features.''')
                st.write('''2. The model's recommendations are confined to the user's existing interests, lacking the capability to explore and expand upon new areas of interest.''')

        with tab2:
            st.header("Colaborative Filtering")
            st.write('''But that's not all! Collaborative filtering is a powerful algorithm that analyzes user behavior and preferences to find similarities among users. By considering the preferences of users who have similar tastes as you, the app can suggest movies that you're likely to enjoy. It takes into account various factors, such as ratings, watch history, and movie preferences of like-minded users, to generate accurate recommendations tailored just for you.''')
            st.image('resources/imgs/Collaborative.png',use_column_width=True)
            st.write('''Memory-based approaches, also known as neighborhood collaborative filtering, predict ratings for user-item combinations based on the neighborhoods they belong to. User-based collaborative filtering recommends items by identifying like-minded users who provide strong and similar recommendations. Item-based collaborative filtering, on the other hand, suggests items based on the similarity calculated from user ratings of those items.''')
            with st.expander("**Advantages/Disadvantages**"):
                st.write('''**Advantages:**''')
                st.write('''1. Collaborative filtering models are relatively simple to implement and offer broad coverage.
    They can capture subtle characteristics.''')
                st.write('''2. These models do not require an understanding of the item content.''')
                st.divider()
                st.write('''**Disadvantages:**''')
                st.write('''1. Collaborative filtering models face challenges when recommending new items, as they lack user-item interactions, resulting in the "cold start problem."''')
                st.write('''2. Memory-based algorithms tend to perform poorly on highly sparse datasets, where data points are limited or missing.''')        
        
        st.write('''The ReelDeal's app is the ultimate movie companion that brings the power of collaborative filtering and content filtering together, ensuring that you never run out of fantastic movies to watch. Say goodbye to endless scrolling and start enjoying personalized movie recommendations today!''')


    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    
    if page_selection == "About Us":
        st.markdown("<div style='background-color: rgba(246, 246, 246, 1); padding: 20px; margin: 0px 0px 25px 0px; border-radius: 10px; text-align:justify'><p>Welcome to NM4 Consulting, your ultimate destination for personalized movie recommender systems! We are a cutting-edge technology company dedicated to revolutionizing the way you discover and enjoy movies. Our team of experts is passionate about film and committed to helping you find your next cinematic gem.<br><br>At NM4 Consulting, we understand that the world of movies can be overwhelming. With thousands of films released each year across various genres and platforms, it can be challenging to navigate through the vast sea of choices. That's where we come in. We have developed state-of-the-art custom movie recommender systems that take into account your unique tastes, preferences, and viewing history to deliver highly tailored recommendations just for you.<br><br>Our sophisticated algorithms analyze an extensive database of movies, considering factors such as genre, director, actors, and user reviews. By understanding your individual cinematic preferences and patterns, we curate a selection of films that align with your interests, ensuring that every movie you watch is a perfect match.<br><br>So, why settle for generic movie suggestions when you can have a tailored cinematic experience with NM4 Consulting? Join our community of movie enthusiasts today and unlock a world of captivating stories, unforgettable characters, and boundless entertainment. Let us be your trusted companion in the realm of movies, guiding you towards the films that will truly speak to you. Get ready to discover, be inspired, and embark on a thrilling reel journey with NM4 Consulting!</div>", unsafe_allow_html=True)
        
        st.markdown("<div style='background-color: transparent; margin: 40px 0 20px 0'><h2 style='text-align:center'>Our Creative Team</h2></div>", unsafe_allow_html=True)
        col_team_1, col_team_2, col_team_3, col_team_4 = st.columns(4)
        with col_team_1:
            st.markdown(img_to_html('resources/imgs/Kobus.jpg'), unsafe_allow_html=True)
            st.markdown("<div style='background-color: transparent; margin-top: 10px'><p style='text-align:center'><b>Kobus Le Roux</b><br>Chairman</p></div>", unsafe_allow_html=True)
        with col_team_2:
            st.markdown(img_to_html('resources/imgs/Cara.jpg'), unsafe_allow_html=True)
            st.markdown("<div style='background-color: transparent; margin-top: 10px'><p style='text-align:center'><b>Cara Brits</b><br>Design Director</p></div>", unsafe_allow_html=True)
        with col_team_3:
            st.markdown(img_to_html('resources/imgs/Koketso.jpg'), unsafe_allow_html=True)
            st.markdown("<div style='background-color: transparent; margin-top: 10px'><p style='text-align:center'><b>Koketso Maraba</b><br>Data Scientist</p></div>", unsafe_allow_html=True)
        with col_team_4:
            st.markdown(img_to_html('resources/imgs/Mxolisi.jpg'), unsafe_allow_html=True)
            st.markdown("<div style='background-color: transparent; margin-top: 10px'><p style='text-align:center'><b>Mxolisi Zulu</b><br>Data Analyst</p></div>", unsafe_allow_html=True)
            
        col_team_5, col_team_6, col_team_7, col_team_8, col_team_9 = st.columns([0.125,0.25,0.25,0.25,0.125])
        with col_team_6:
            st.markdown(img_to_html('resources/imgs/Devon.jpg'), unsafe_allow_html=True)
            st.markdown("<div style='background-color: transparent; margin-top: 10px'><p style='text-align:center'><b>Devon Woodman</b><br>Technical Director</p></div>", unsafe_allow_html=True)
        with col_team_7:
            st.markdown(img_to_html('resources/imgs/Nhlanhla.jpg'), unsafe_allow_html=True)
            st.markdown("<div style='background-color: transparent; margin-top: 10px'><p style='text-align:center'><b>Nhlanhla Mthembu</b><br>Senior Developer</p></div>", unsafe_allow_html=True)
        with col_team_8:
            st.markdown(img_to_html('resources/imgs/Tebogo.jpg'), unsafe_allow_html=True)
            st.markdown("<div style='background-color: transparent; margin-top: 10px'><p style='text-align:center'><b>Tebogo Khoza</b><br>Junior Developer</p></div>", unsafe_allow_html=True)
        
        with st.form("feedback_form"):
            col_contact_1, col_contact_2 = st.columns(2)
            with col_contact_1:
                st.header("Let's Work Together")
                st.header("Do a Great Project")

                st.write('**Contact number**')
                st.write('+27 87 623 2732')

                st.write('**Contact address**')
                st.write('187 Long St, Cape Town City Centre, Cape Town, 8001')

                st.write('**Contact email**')
                st.write('info@thereeldeel.co.za')
                
            with col_contact_2:
                
                c_contact = st.container()
                with c_contact:
                    text_input = st.text_input("", label_visibility='hidden', placeholder='What should we call you?')
                    text_input = st.text_input("", label_visibility='hidden', placeholder='Please enter your email')
                    text_input = st.text_area("", label_visibility='hidden', placeholder='Please describe your problem')
                    
                submit_contact = st.form_submit_button("Submit")
                
            df = pd.DataFrame(
                [[-33.924852, 18.416760]],
                columns=['lat', 'lon'])

            st.map(df, zoom=13)
            
    if page_selection == "App Feedback":
        st.title("App Feedback")
        st.write("We appreciate your valuable feedback on our app! Your insights and suggestions are crucial in helping us improve and provide you with an exceptional user experience. Please take a few moments to share your thoughts by completing this feedback form. Your input will assist us in understanding what aspects of the app are working well and where we can make enhancements or address any issues you may have encountered.")
        
        with st.form("feedback_form"):
            c_feedback = st.container()

            with c_feedback:
                col_feedback_1, col_feedback_2 = st.columns(2)
                with col_feedback_1:
                    feedback_name = st.text_input(
                        "Name",
                        placeholder='Enter',
                    )
                with col_feedback_2:
                    feedback_email = st.text_input(
                        "Email",
                        placeholder='Enter',
                    )
                col_feedback_3, col_feedback_4 = st.columns(2)
                with col_feedback_3:
                    feedback_type = st.selectbox(
                    'Category',
                    ('Defect', 'Bug', 'Feature'))
                with col_feedback_4:
                    feedback_subject = st.text_input(
                        "Subject",
                        placeholder='Enter',
                    )
                col_feedback_5, col_feedback_6 = st.columns(2)
                with col_feedback_5:
                    feedback_description = st.text_area('Description', '''''', height=400)
                with col_feedback_6:
                    tab_low, tab_medium, tab_high = st.tabs(["Low", "Medium", "High"])
                    with tab_low:
                        feedback_priority = 0
                    with tab_medium:
                        feedback_priority = 1
                    with tab_high:
                        feedback_priority = 2

                    feedback_satisfaction = st.radio(
                    "Satisfaction",
                    ('Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied'))

                    st.write('Additional Features')
                    feedback_additional_1 = st.checkbox('UI/UX')
                    feedback_additional_2 = st.checkbox('Performance')
                    feedback_additional_3 = st.checkbox('Functionality')
                    feedback_additional_4 = st.checkbox('Other')
            submit_feedback = st.form_submit_button("Submit Feedback")

    if page_selection == "Analytics":
        st.title("Uncovering Data Insights")
        #Movie ratings Histogram
        st.markdown("""<h4 style="text-align: center;">Movie Ratings Distribution</h4><p style="text-align: center;"></p>""", unsafe_allow_html=True)
        
        fig, ax = plt.subplots()
        ax.hist(hist_data['rating'],rwidth=0.99,color = "Purple")
        st.pyplot(fig)
        
        st.subheader("Most Rated Overall Movies")
        top_movies = df_ratings.head(25)
        bottom_movies = df_ratings.tail(25)

        st.markdown("""<h4 style="text-align: center;">25 Most Rated Movies</h4><p style="text-align: center;"></p>""", unsafe_allow_html=True)
        fig_top_movies=px.bar(top_movies,x='Reviews',y='Title', orientation='h')
        fig_top_movies.update_traces(marker_color='gold',  # Change the bar color
                      textfont_color='black',  # Change the label text color
                      hovertemplate='<b>Title: %{y}</b><br><b>Review Count: %{x}</b>',  # Change the tooltip text
                      selector=dict(type='bar'))  # Select only the bar traces
        st.write(fig_top_movies)

        st.subheader("Genre Distribution and Average ratings")
        #Donut Chart
        st.markdown("""<h4 style="text-align: center;">Genre Distribution</h4><p style="text-align: center;"></p>""", unsafe_allow_html=True)
        labels = df_genre_freq["Genres"]
        sizes = df_genre_freq["Frequency"]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%0.1f%%',
                shadow=False, startangle=0,labeldistance = 1.05,pctdistance = 0.67,textprops={'fontsize': 5.9})
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        circle = plt.Circle( (0,0), 0.75, color='white')
        p=plt.gcf()
        p.gca().add_artist(circle)
        plt.gca().set_aspect('equal')
        plt.subplots_adjust(left=0.1, bottom=0.1, right=0.75)
        st.pyplot(fig1)
        #Ratings bar chart
        st.markdown("""<h4 style="text-align: center;">Average Rating of Genres</h4><p style="text-align: center;"></p>""", unsafe_allow_html=True)
        fig=px.bar(df_genre_rating,x='Rating',y='Genres', orientation='h')
        fig.update_traces(marker_color='deepskyblue',  # Change the bar color
                      textfont_color='black',  # Change the label text color
                      hovertemplate='<b>Genre: %{y}</b><br><b>Rating: %{x}</b>',  # Change the tooltip text
                      selector=dict(type='bar'))  # Select only the bar traces
        st.write(fig)
        #Directors
        #directors data frame
        directors = pd.read_csv("resources/data/df_top_directors.csv", encoding = "latin_1")
        st.subheader("Best and worst performing directors")
        #Best Directors
        st.markdown("""<h4 style="text-align: center;">Best Rated Directors</h4><p style="text-align: center;"></p>""", unsafe_allow_html=True)
        fig_top_directors=px.bar(directors.head(25),x='Rating',y='Director', orientation='h')
        fig_top_directors.update_traces(marker_color='yellowgreen',  # Change the bar color
                      textfont_color='black',  # Change the label text color
                      hovertemplate='<b>Director Name: %{y}</b><br><b>Rating: %{x}</b>',  # Change the tooltip text
                      selector=dict(type='bar'))  # Select only the bar traces
        st.write(fig_top_directors)
        #Worst Directors

        st.markdown("""<h4 style="text-align: center;">Worst Rated Directors</h4><p style="text-align: center;"></p>""", unsafe_allow_html=True)
        fig_worst_directors=px.bar(directors.tail(25),x='Rating',y='Director', orientation='h')
        fig_worst_directors.update_traces(marker_color='lightcoral',  # Change the bar color
                      textfont_color='black',  # Change the label text color
                      hovertemplate='<b>Director Name: %{y}</b><br><b>Rating: %{x}</b>',  # Change the tooltip text
                      selector=dict(type='bar'))  # Select only the bar traces
        st.write(fig_worst_directors)



        #Actors
        
        st.subheader("Best and worst performing actors")
        best_actors = actors_df.head(30)
        worst_actors = actors_df.tail(30)
        
        st.markdown("""<h4 style="text-align: center;">Best Perfoming Actors</h4><p style="text-align: center;"></p>""", unsafe_allow_html=True)
        fig_top_actors=px.bar(best_actors,x='Average Actor Rating',y='Actor', orientation='h')
        fig_top_actors.update_traces(marker_color='green',  # Change the bar color
                      textfont_color='black',  # Change the label text color
                      hovertemplate='<b>Actor Name: %{y}</b><br><b>Rating: %{x}</b>',  # Change the tooltip text
                      selector=dict(type='bar'))  # Select only the bar traces
        st.write(fig_top_actors)


        st.markdown("""<h4 style="text-align: center;">Worst Perfoming Actors</h4><p style="text-align: center;"></p>""", unsafe_allow_html=True)
        fig_worst_actors=px.bar(worst_actors,x='Average Actor Rating',y='Actor', orientation='h')
        fig_worst_actors.update_traces(marker_color='red',  # Change the bar color
                      textfont_color='black',  # Change the label text color
                      hovertemplate='<b>Actor Name: %{y}</b><br><b>Rating: %{x}</b>',  # Change the tooltip text
                      selector=dict(type='bar'))  # Select only the bar traces
        st.write(fig_worst_actors)

    if page_selection == "Recommender Settings":
        st.title('Settings')
        if 'model' not in st.session_state:
            st.session_state.search_1 = 'SVD'
            st.session_state['model'] = st.selectbox('Select Recommender Model Type',('SVD', 'NMF', 'CoCluster'), key='search_1')
        else:
            st.session_state['model'] = st.selectbox('Select Recommender Model Type',('SVD', 'NMF', 'CoCluster'), key='search_1')
if __name__ == '__main__':
    main()

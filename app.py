import streamlit as st
import pickle
import pandas as pd

def fetch_poster(movie):
    result = movie_df[movie_df['Series_Title'].str.lower() == movie.lower()]

    # Check if the movie is found
    if not result.empty:
        return result['Poster_Link'].iloc[0]
    else:
        return "Poster link not found for the given movie name."

def recommend(movie):
    movie_index = movies[movies['Series_Title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        #fetch poster
        movie_name = movies.iloc[i[0]].Series_Title
        recommended_movies_poster.append(fetch_poster(movie_name))
        recommended_movies.append(movies.iloc[i[0]].Series_Title)

    return recommended_movies,recommended_movies_poster

movies_dict = pickle.load(open('movie_list.pkl)','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity1.pkl','rb'))
movie_df = pickle.load(open('moviedf.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Enter a movie name",
    movies['Series_Title'].values
)

if st.button("Recommended"):
    recommended_movie, poster = recommend(selected_movie_name)

    # Create a dynamic layout with columns
    cols = st.columns(len(recommended_movie))  # Create as many columns as there are recommendations

    for i, col in enumerate(cols):
        with col:
            #st.text(recommended_movie[i])
            st.image(poster[i],use_container_width=True)  # Display movie poster
            st.write(f"**{recommended_movie[i]}**")  # Display movie title
    # for i in range(len(recommended_movie)):
    #     st.subheader(recommended_movie[i])  # Display the movie title as a subheader
    #     st.image(poster[i], use_column_width=True)  # Full-width poster

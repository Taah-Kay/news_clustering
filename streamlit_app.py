import streamlit as st
import pandas as pd
import pickle

# Method to load the clustered dataframe
def load_clustered_data():
    clustered_df = pd.read_csv('news_clustering_data.csv')
    return clustered_df

# Streamlit app function
def main():

    st.title("News Articles Clusters")

    # Load the clustered dataframe
    data = load_clustered_data()

    # Displaying clusters and related stories
    categories = data['Category'].unique()

    selected_cluster = st.sidebar.selectbox("Select Category", categories)

    st.header(f"Cluster{selected_cluster}")

    cluster_articles = data[data['Cluster'] == selected_cluster]

    for idx, row in cluster_articles.iterrows():
        st.markdown(f"{row['Title']}")
        st.markdown(f"{row['Category']}")
        st.markdown(f"**URL:** {row['Link']}")
        st.markdown("---")

# Running the app
if __name__ == "__main__":
    main()
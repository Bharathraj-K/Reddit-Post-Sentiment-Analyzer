import streamlit as st
import praw
import pandas as pd
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

# Vader Initialization
sia = SentimentIntensityAnalyzer()

# Reddit API 
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR-CLIENT-SECRET",
    user_agent="Sentiment Analyser"
)

# Sentiment function using VADER
def get_vader_sentiment(text):
    score = sia.polarity_scores(text)
    compound = score['compound']
    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Streamlit UI
st.title("💬. Reddit Post Sentiment Analyzer")

subreddit_input = st.text_input("Enter a Subreddit name (without r/):", "Sub Name Goes Here")
limit = st.slider("Number of posts to analyze", min_value=10, max_value=100, value=30)
analyze_comments = st.checkbox("Analyze comments too?", value=False)

if st.button("Analyze"):
    with st.spinner("Fetching data and analyzing..."):
        try:
            subreddit = reddit.subreddit(subreddit_input)

            texts = []
            sentiments = []

            # Analyze posts titles
            for post in subreddit.new(limit=limit):
                texts.append(post.title)
                sentiments.append(get_vader_sentiment(post.title))

                # Optionally analyze comments of this post
                if analyze_comments:
                    post.comments.replace_more(limit=0)
                    for comment in post.comments.list():
                        texts.append(comment.body)
                        sentiments.append(get_vader_sentiment(comment.body))

            df = pd.DataFrame({"Text": texts, "Sentiment": sentiments})

            st.subheader("📃 Sentiment Summary")
            st.dataframe(df)

            st.subheader("📊 Sentiment Distribution (Pie Chart)")
            sentiment_counts = df['Sentiment'].value_counts()

            fig, ax = plt.subplots()
            ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90, colors=['#2ecc71','#e74c3c','#95a5a6'])
            ax.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle.
            st.pyplot(fig)

        except Exception as e:
            st.error(f"An error occurred: {e}")

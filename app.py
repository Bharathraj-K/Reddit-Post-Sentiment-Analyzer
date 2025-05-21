from transformers import pipeline
import praw
import streamlit as st
from transformers import pipeline
import pandas as pd
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk



nltk.download('vader_lexicon')

# Vader Initialization
sia = SentimentIntensityAnalyzer()

# Load summarizer
summarizer = pipeline("summarization", model="t5-small") 

#API Setup
reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent=""
)

# ---------------------- 🔍 Post Summarizer ----------------------
st.title("📰 Reddit Post Summarizer")

with st.expander("🔧 Settings - Summarizer"):
    subreddit_name = st.text_input("Enter subreddit name (without r/):", "")
    postID = st.text_input("Enter Reddit post ID to summarize specific post (optional):", "")
    post_count = st.slider("Number of posts to summarize:", 1, 30, 3)

if st.button("Summarize Posts"):
    with st.spinner("Fetching and summarizing posts..."):
        try:
            if postID.strip():  # Summarize specific post first if provided
                post = reddit.submission(id=postID.strip())
                if post.selftext:
                    body = post.selftext[:1000]
                    summary = summarizer(body, max_length=150, min_length=30, do_sample=False)[0]['summary_text']

                    st.markdown("---")
                    st.markdown(f"### 📝 {post.title}")
                    st.markdown(f"**🔍 Summary:** {summary}")
                    with st.expander("📖 Show original post"):
                        st.write(post.selftext)
                else:
                    st.warning("This post has no body text to summarize.")
            elif subreddit_name.strip():
                subreddit = reddit.subreddit(subreddit_name.strip())
                for post in subreddit.top(limit=post_count, time_filter="day"):
                    if post.selftext:
                        body = post.selftext[:1000]
                        summary = summarizer(body, max_length=150, min_length=30, do_sample=False)[0]['summary_text']

                        st.markdown("---")
                        st.markdown(f"### 📝 {post.title}")
                        st.markdown(f"**🔍 Summary:** {summary}")
                        with st.expander("📖 Show original post"):
                            st.write(post.selftext)
            else:
                st.error("Please provide a subreddit name or post ID.")
        except Exception as e:
            st.error(f"Error: {e}")

# ---------------------- 📊 Sentiment Analyzer ----------------------
st.title("💬 Reddit Sentiment Analyzer")

with st.expander("🔧 Settings - Sentiment"):
    subreddit_input = st.text_input("Enter subreddit name (without r/):", "IndiaTech", key="sentiment_sub")
    limit = st.slider("Number of posts to analyze:", 10, 100, 30)
    analyze_comments = st.checkbox("Include comments in analysis", value=False)

# Function to get sentiment label from VADER
def get_vader_sentiment(text):
    score = sia.polarity_scores(text)
    compound = score['compound']
    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    else:
        return "Neutral"

if st.button("Analyze Sentiment"):
    with st.spinner("Analyzing posts and comments..."):
        try:
            subreddit = reddit.subreddit(subreddit_input)
            texts = []
            sentiments = []

            for post in subreddit.new(limit=limit):
                texts.append(post.title)
                sentiments.append(get_vader_sentiment(post.title))

                if analyze_comments:
                    post.comments.replace_more(limit=0)
                    for comment in post.comments.list():
                        texts.append(comment.body)
                        sentiments.append(get_vader_sentiment(comment.body))

            df = pd.DataFrame({"Text": texts, "Sentiment": sentiments})

            st.subheader("📄 Sentiment Table")
            st.dataframe(df)

            st.subheader("📊 Sentiment Distribution")
            sentiment_counts = df['Sentiment'].value_counts()

            fig, ax = plt.subplots()
            ax.pie(
                sentiment_counts,
                labels=sentiment_counts.index,
                autopct='%1.1f%%',
                startangle=90,
                colors=['#2ecc71', '#e74c3c', '#95a5a6']
            )
            ax.axis('equal')
            st.pyplot(fig)

        except Exception as e:
            st.error(f"An error occurred: {e}")

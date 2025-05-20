# Reddit-Post-Sentiment-Analyzer
Reddit Topic Sentiment Analyzer is a Streamlit app that fetches recent posts and comments from any subreddit using Reddit’s API. It uses VADER to analyze sentiment, showing if the content is positive, neutral, or negative, with results displayed in tables and pie charts for easy insights.


## Features

- Fetches the latest posts from a specified subreddit using Reddit’s API.
- Optionally analyzes comments from each post.
- Performs sentiment analysis on post titles and comments using the VADER sentiment analyzer.
- Displays sentiment results in a table.
- Visualizes overall sentiment distribution with a pie chart.
- Built with Streamlit for an easy-to-use and interactive UI.

---

## Demo

-Enter sub name and select number of posts to analyze and comments if wanted and then click on analyze. 
![image alt](https://github.com/Bharathraj-K/Reddit-Post-Sentiment-Analyzer/blob/f3ac87ed496fb5e7a43bf9defbec4198da824ce6/images/Home.png)





-Results
![image alt](https://github.com/Bharathraj-K/Reddit-Post-Sentiment-Analyzer/blob/bb727bab2802aa389caa25401840bdd7249264b4/images/Screenshot%202025-05-20%20183519.png)








-PieChart
![image alt](https://github.com/Bharathraj-K/Reddit-Post-Sentiment-Analyzer/blob/98ae5d39a988fac495ad0fa99874b49007d6bef5/images/pie.png)


## Installation
1. **Clone the repository**
2. pip install -r requirements.txt
3. python -m nltk.downloader vader_lexicon


   
## 🔑 Getting Reddit API Credentials

To use the Reddit API, you need to create an application on Reddit and obtain your credentials:

1. Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
2. Scroll down and click on **"Create another app"**
3. Fill out the form:
   - **Name**: `Reddit Sentiment Analyzer` (or any name you prefer)
   - **Type**: Select **Script**
   - **Description**: *(Optional)*
   - **About URL**: *(Leave blank)*
   - **Redirect URI**: `http://localhost:8080`
4. Click **Create app**
5. After the app is created, copy the following:
   - **client_id**: This is shown just under the app name
   - **client_secret**: This is shown in the app details

You'll use these in your `app.py` like this:

python
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="Reddit Sentiment Analyzer"
)



# 🚀 Usage

1. Open `app.py` and replace the placeholders with your Reddit API credentials:

    reddit = praw.Reddit(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        user_agent="Reddit Sentiment Analyzer"
    )

2. Run the Streamlit app:

    streamlit run SentimentAnalyser.py

3. In the Streamlit web interface:

    Enter the subreddit name (without r/)
    
    Select the number of posts to analyze
    
    Check the box to include comments in the analysis (optional)
    
    Click the Analyze button


#The app will fetch posts (and optionally comments), perform sentiment analysis using VADER, and display:

A table of text and sentiment labels

A pie chart showing sentiment distribution

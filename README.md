# Reddit-Post-Summarizer-and-Sentiment-Analyzer

🔍 Sentiment Analysis: Uses VADER to classify Reddit post titles and comments as Positive, Neutral, or Negative, displaying results in a table and pie chart.

✂️ Post Summarization: Uses transformers-based models to generate abstractive summaries of Reddit posts, optionally targeting a specific post by ID.


## Features

✅ Sentiment Analyzer
-Fetches latest posts and optionally comments using Reddit’s API.

-Uses VADER for sentiment analysis on text.

-Displays results in a clean table and a pie chart for visual insight.

-Select number of posts and include/exclude comments.

✅ Post Summarizer
-Summarizes top or specific Reddit posts using Hugging Face transformers.

-Uses abstractive models like facebook/bart-large-cnn or google/pegasus-xsum.

-Automatically truncates long content for optimal summarization.

---

## Demo

![image alt](https://github.com/Bharathraj-K/Reddit-Post-Summarizer-and-Sentiment-Analyzer/blob/95a9227ca19698d4c0497ea9bc89d2ac586f8027/images/Screenshot%202025-05-21%20191054.png)

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
   
      
    Enter the subreddit name (without r/) Or Post ID

    To summarize select number of post to summarize

    click the summarize button

    _OR_
   
    Select the number of posts to analyze
    
    Check the box to include comments in the analysis (optional)
    
    Click the Analyze button


NOTE: YOU CAN CHANGE THE MODEL AND MAX TOKEN SIZE IF YOU WANT TO SINCE THE BASE MODEL I USED IS THE FASTEST AND MAY NOT PROVIDE BETTER RESULT FOR SUMMARIZATION

# Twitter_DataAnalytics_MongoDB
Semi-Structured Data Processing with NoSQL Database Server MongoDB, collecting Social Media Data from Twitter Real-time Data Stream and Storing and Retrieving to Process from a Semi-Structured Database Server MongoDB 

The Twitter API allows you to stream public Tweets from the platform in real-time so that you can display them and basic metrics about them.

# STEP 1: Setup and Platform Procedure -
First, define what you want to accomplish and decide on the data you need to meet that objective.
• Staying informed on a topic of interest: For example, you would like to stay current on updates, news, and events about Twitter’s API.
• Detecting current trends: So, I went ahead with choosing topic such as ‘bitcoin’ and tags such as ‘CRYPTO’
## The setup included multiple steps:
 1. Firstly, we must create a Twitter developer account and receive the tokens and keys for fetching the data through these keys from the python script. I have fetched over 7000 tweets relating to ‘bitcoin’, ‘crypto’, ‘NFT’.
 2. Secondly, we have to download and set up MongoDB Server and a Client Mongo shell mongosh or mongo. By using the mongosh shell, I was able to create a NoSQL database (test2) and a collection (tweets) in MongoDB
 3. Secondly, we must connect to a NoSQL database which in this lab is Mongo dB. In the same python script which includes your keys, we have to write a code to connect to Mongo dB, wherein the real-time retrieved tweets will be stored in a NoSQL database inside a collection.
Below is the screenshot which shows the Mongo dB connection and Twitter keys passed:
 4. After setting up Mongo dB, below is the screenshot of the successful database and collection created with the data retrieved.

### CANNOT SHARE THE IMAGE DUE TO PRIVATE INFORMATION!

## The Platform used for this lab:
1. IDE: VS Code, Jupyter notebook
2. Scripting language: Python, MQL
3. NoSQL database: Mongo dB, mongosh shell
4. Other tools: Notepad++ (To view the JSON document)
# STEP 2: Perform analytics to retreieve information below in MongoDB Queries with $Match, Aggregation pipelining, and $Group as below -
4-1. For each “place_type”, Find total favorite_count
4-2. For each "country_code", find total "retweet_count"

![image](https://user-images.githubusercontent.com/89702819/160223921-1f843e19-393e-4fb1-8a32-b852e4279712.png)

## Below is the screenshot of the queries performed to retrieve the aggregation pipelining information:
Aggregation pipelining:
An aggregation pipeline consists of one or more stages that process documents:
• Each stage performs an operation on the input documents. For example, a stage can filter documents, group documents, and calculate values.
• The documents that are output from a stage are passed to the next stage.
• An aggregation pipeline can return results for groups of documents. For example, return the total, average, maximum, and minimum values.
$match:
Filters the documents to pass only the documents that match the specified condition(s) to the next pipeline stage.
$group:
Groups input documents by the specified _id expression and for each distinct grouping outputs a document. The _id field of each output document contains the unique group by value. The output documents can also contain computed fields that hold the values of some accumulator expression.
# STEP 3: In this step I performed text processing step wise to remove stop words as well as using stemming and lemmatization -
1. I have used Jupyter notebook for better ease of viewing and processing the ‘text’. Initially, the ‘tweets.json’ file is converted to a .csv file for better analysis.
2. The various steps in performing text processing includes Removing punctuation, Tokenization, removing stop words, Stemming, Lemmatization, Extracting to a cleaner text.
3. After performing the above procedures, we then extract the ‘clean text’ to a csv file to find out the top 10 most frequent topic words in the text.

![image](https://user-images.githubusercontent.com/89702819/160223909-a1b16a26-8d7e-485b-9c0b-2bdb72a64b38.png)

YOU CAN FIND THE ENTIRE ANALYSIS AND STEPS IN MY FOLDER - “Task5.ipynb”, “Task5.pdf”
# STEP 4: Performing sentiment analysis to find out the tweets are Positive, Neutral or Negative -
1. In this task, I have used a library called ‘vanderSentiment’, which has a builtin function called ‘SentimentIntensityAnalyzer()’. This helps in easing the development process and finding out the sentiment of the data.
2. After retreving the real-time tweets, we can apply this function to be able to anaylze the polarity of the statement whether it is pos, neu, or neg.
3. Below is the screenshot from my ‘Sentiment_Analysis.ipynb’ file, that shows the sentiment analysis done on the tweet text from my data.

![image](https://user-images.githubusercontent.com/89702819/160223891-51b0f390-0520-4860-9578-8d2877f62810.png)

YOU CAN FIND THE ENTIRE ANALYSIS AND STEPS IN MY FOLDER - “Sentiment_Analysis.ipynb”

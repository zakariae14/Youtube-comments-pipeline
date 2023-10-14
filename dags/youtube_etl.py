from googleapiclient.discovery import build
import pandas as pd
from sqlalchemy import create_engine


def youtube_etl_fct():
    # Your API key
    api_key = 'AIzaSyCY1_YA89SH1L7wu6OPUXvEI6B6-r0JoYg'
    # Video ID of the YouTube video
    video_id = 'UIZdjAKadc8'
    # Create a service instance
    youtube = build('youtube', 'v3', developerKey=api_key)
    # Retrieve comments for the video
    comments = []
    like_counts = []
    nextPageToken = None
    d = 1
    while d < 11:
        d = d + 1
        comment_threads = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            textFormat='plainText',
            pageToken=nextPageToken
        ).execute()
        for comment_thread in comment_threads['items']:
            comment = comment_thread['snippet']['topLevelComment']['snippet']['textDisplay']
            like_count = comment_thread['snippet']['topLevelComment']['snippet']['likeCount']
            like_counts.append(like_count)
            comments.append(comment)
        nextPageToken = comment_threads.get('nextPageToken')
        if not nextPageToken:
            break
    df = pd.DataFrame({"comments": comments, 'number_of_likes': like_counts})

    df.to_csv("/home/zakariae/comments.csv")

    engine = create_engine("mysql://airflow:airflow@localhost:3306/airflow")
    df.to_sql("youtube_comments", engine, if_exists="append", index=False)
    engine.dispose()




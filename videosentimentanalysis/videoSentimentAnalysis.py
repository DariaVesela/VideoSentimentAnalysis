import os
from pytube import YouTube
from textblob import TextBlob

def extract_subtitle_from_yt_video(yt_url: str) -> str:
    try:
        yt = YouTube(yt_url)
        yt.bypass_age_gate()
        caption = yt.captions['en']
        subtitles = ""
        
        for sub in caption.json_captions['events']:
            for text in sub['segs']:
                subtitles += text['utf8']
        
        return subtitles
    except Exception as e:
        print(f"Failed to extract subtitles for URL: {yt_url}. Error: {e}")
        return ""

def extract_title_from_yt_video(yt_url: str) -> str:
    try:
        yt = YouTube(yt_url)
        yt.bypass_age_gate()
        return yt.title
    except Exception as e:
        print(f"Failed to extract title for URL: {yt_url}. Error: {e}")
        return "Unknown Title"

def sentiment_analysis(text: str) -> float:
    blob = TextBlob(text)
    return blob.sentiment.polarity

def extract_yt_urls() -> list[str]:
    with open('services/video_urls.txt', 'r') as file:
        # Read all lines from the file
        lines = file.readlines()
    return [line.strip() for line in lines]

if __name__ == "__main__":
    yt_urls = extract_yt_urls()
    for url in yt_urls:
        print(f"Processing URL: {url}")  # Debug print statement before processing each URL
        try:
            title = extract_title_from_yt_video(url)
            subtitle = extract_subtitle_from_yt_video(url)
            sentimental_analysis_score = sentiment_analysis(subtitle)
            print(f"{title} => {sentimental_analysis_score}")
        except Exception as e:
            print(f"Error processing URL: {url}. Error: {e}")

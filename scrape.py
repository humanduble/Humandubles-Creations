import requests
from bs4 import BeautifulSoup
from models import Video, Session

def scrape_pornhub():
    url = "https://www.pornhub.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    videos = []
    for video in soup.find_all('div', class_='videoItem'):
        try:
            title = video.find('a', class_='title').text.strip()
            thumbnail = video.find('img')['src']
            video_url = "https://www.pornhub.com" + video.find('a')['href']
            
            videos.append({
                'title': title,
                'thumbnail': thumbnail,
                'url': video_url
            })
        except Exception as e:
            print(f"Error scraping video from Pornhub: {e}")
    
    return videos

def scrape_xvideos():
    url = "https://www.xvideos.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    videos = []
    for video in soup.find_all('div', class_='thumb-block'):
        try:
            title_tag = video.find('a')
            if not title_tag or not title_tag.has_attr('title'):
                continue
            title = title_tag['title'].strip()
            
            thumbnail_tag = video.find('img')
            if not thumbnail_tag or not thumbnail_tag.has_attr('src'):
                continue
            thumbnail = thumbnail_tag['src']
            
            video_url_tag = video.find('a')
            if not video_url_tag or not video_url_tag.has_attr('href'):
                continue
            video_url = "https://www.xvideos.com" + video_url_tag['href']
            
            videos.append({
                'title': title,
                'thumbnail': thumbnail,
                'url': video_url
            })
        except Exception as e:
            print(f"Error scraping video from XVideos: {e}")
    
    return videos

def save_videos_to_db(videos):
    session = Session()
    for video in videos:
        new_video = Video(title=video['title'], thumbnail=video['thumbnail'], url=video['url'])
        session.add(new_video)
    session.commit()
    session.close()

if __name__ == '__main__':
    pornhub_videos = scrape_pornhub()
    xvideos_videos = scrape_xvideos()
    
    all_videos = pornhub_videos + xvideos_videos
    save_videos_to_db(all_videos)
    
    # Print scraped video data for verification
    for video in all_videos:
        print(video)

from flask import Flask, render_template, request
from models import Video, Session

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    session = Session()
    videos = session.query(Video).all()
    session.close()
    return render_template('index.html', videos=videos)

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    category = request.form.get('category')
    
    session = Session()
    
    if category == 'pornhub':
        filtered_videos = session.query(Video).filter(
            Video.title.like(f'%{query}%'),
            Video.url.contains('pornhub.com')
        ).all()
    elif category == 'xvideos':
        filtered_videos = session.query(Video).filter(
            Video.title.like(f'%{query}%'),
            Video.url.contains('xvideos.com')
        ).all()
    else:
        filtered_videos = session.query(Video).filter(Video.title.like(f'%{query}%')).all()
    
    session.close()
    return render_template('search.html', videos=filtered_videos)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route('/transcript', methods=['GET'])
def transcript():
    video_id = request.args.get('video_id')
    if not video_id:
        return jsonify({'error': 'missing video_id'}), 400

    try:
        yt = YouTubeTranscriptApi()
        transcript_data = yt.fetch(video_id, languages=['en'])
        # Each snippet is a dict with 'start', 'duration', 'text'
        return jsonify(transcript_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

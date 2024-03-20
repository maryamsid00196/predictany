from .models import YouTubeVideo
from datetime import datetime
from django.http import HttpResponse
import feedparser

def pubsubhub_callback(request):
    if request.method == 'GET':
        # Parse the incoming Atom feed notification
        feed_data = request.body
        parsed_feed = feedparser.parse(feed_data)
        '''
        # Process the feed data and save it to the database
        for entry in parsed_feed.entries:
            video_id = entry.get('yt_videoId')
            channel_id = entry.get('yt_channelId')
            title = entry.get('title')
            video_link = entry.get('link')
            channel_title = entry.get('author').get('name')
            published_at = datetime.strptime(entry.get('published'), '%Y-%m-%dT%H:%M:%S+00:00')
            updated_at = datetime.strptime(entry.get('updated'), '%Y-%m-%dT%H:%M:%S+00:00')

            # Save the data to the database
            YouTubeVideo.objects.create(
                video_id=video_id,
                channel_id=channel_id,
                title=title,
                video_link=video_link,
                channel_title=channel_title,
                published_at=published_at,
                updated_at=updated_at
            )
            '''
        # Return a success response
        return HttpResponse(status=200)
    else:
        # Return an error response for non-POST requests
        return HttpResponse(status=405)  # Method Not Allowed


# youtubenotifications/views.py

import requests

def subscribe_to_notifications(request):
    # Send subscription request to Google hub
    callback_url = 'https://yourdomain.com/callback/'  # Replace with your actual callback URL
    topic_url = 'https://www.youtube.com/feeds/videos.xml?channel_id=YOUR_CHANNEL_ID'  # Replace with your actual channel ID

    # Subscription request parameters
    params = {
        'hub.mode': 'subscribe',
        'hub.callback': callback_url,
        'hub.topic': topic_url
    }

    # Make a POST request to subscribe
    response = requests.post('https://pubsubhubbub.appspot.com/subscribe', data=params)

    # Check if subscription was successful
    if response.status_code == 202:
        return JsonResponse({'message': 'Subscribed to YouTube notifications successfully'})
    else:
        return JsonResponse({'message': 'Failed to subscribe to YouTube notifications'}, status=500)

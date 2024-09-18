# VidCaptioner


## Overview
1. Video Upload and Processing: Develop a website that allows users to upload videos, which will be processed in the background. After processing and extracting subtitles from the video, the subtitles should be returned to the frontend, integrated with the video, and displayed as closed captions. Ensure that the logic supports multiple language subtitles.
2. Search Functionality: Implement a search feature on the website that enables users to search for a phrase within the video and retrieve the timestamp of its occurrence. When a user clicks on the timestamp, the video should start playing from that specific point. Ensure that the search functionality is case-insensitive.
3. List View for Uploaded Videos: Implement a list view for uploaded video files. When a video file is selected, it should retrieve the corresponding video and subtitles, and provide all the aforementioned features.


## Available URL route's

1. /upload

    URL route to upload videos.

2. /videos

    URL route to list all videos.    

3. /search

    URL route to search videos by keyword's. 

## Installation with docker
1. Run docker-compose up --build
2. Access https://localhost:8000 on your browser.


## Screenshots
Please check `screenshots` directory.

import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    work_experiences = [
        {
            'job_title': 'Teaching Assistant',
            'company': 'Academy Of Brilliant Children',
            'description': [
                'Conducted tutoring sessions with students, resulting in a remarkable 95% improvement in their comprehension of computer science concepts and problem-solving skills.',
                'Organized and led comprehensive exam review sessions, covering key topics, and addressing student concerns, contributing to improved exam preparation and performance.'
            ],
            'start_date': 'Jan 2022',
            'end_date': 'Dec 2022'
        },
        {
            'job_title': 'VISA Leader',
            'company': 'Georgia State University',
            'description': [
                'Led comprehensive campus orientation tours, acquainting new international students with key academic buildings, libraries, dormitories, dining facilities, and recreational areas.',
                'Created a welcoming and inclusive environment by sharing cultural insights and facilitating open discussions among students from diverse backgrounds. Encouraged a sense of belonging and community among the incoming class.',
                'Tailored campus tours to meet the specific needs and interests of incoming students, addressing questions about academic departments, student organizations, and extracurricular activities.'
            ],
            'start_date': 'Jan 2022',
            'end_date': 'May 2022'
        }
    ]

    educations = [
        {
            'degree': 'Production Engineering Track',
            'institution': 'MLH Fellowship',
            'description': '12-weeks of structured curriculum-based learning covering core Production Engineering topics, supplemented with events/workshops hosted by industry experts.',
            'end_date': 'Sep 2024'
        },
        {
            'degree': 'Bachelor of Science',
            'institution': 'Georgia State University',
            'description': 'Major in Computer Science with a focus on software engineering and data science. Achieved Dean\'s List and President\'s List recognition for academic excellence.',
            'end_date': 'Dec 2024'
        }
    ]


    locations = [
        {"lat": 33.4152, "lon": -111.8315, "title": "Mesa"},
        {"lat": 32.715736, "lon": -117.161087, "title": "San Diego"},
        {"lat": 40.7607, "lon": -111.8939, "title": "Salt Lake City"},
        {"lat": 33.753746, "lon": -84.38633, "title": "Atlanta"},
        {"lat": 35.71453, "lon": -83.51189, "title": "Gatlinburg"},
        {"lat": 35.71453, "lon": -82.5515, "title": "Asheville"},
        {"lat": 27.964157, "lon": -82.4526, "title": "Tampa"},
        {"lat": 15.8801, "lon": 108.3380, "title": "Hoi An"},
        {"lat": 11.0686, "lon": 107.1676, "title": "Dong Nai"},
    ]

    return render_template('home.html', title="MLH Fellow", url=os.getenv("URL"), work_experiences=work_experiences, educations=educations, locations=locations)

@app.route('/hobby')
def hobby():
    hobbies = [
        {
            'title': 'Playing Guitar',
            'description': 'I love the sound of guitar and learning how to play is really rewarding.',
            'image': './static/img/guitar.jpeg'
        },
        {
            'title': 'Hiking',
            'description': ' Exploring new places is my passion. Every journey brings a new adventure.',
            'image': './static/img/hiking.jpeg'
        },
        {
            'title': 'Boba Tea',
            'description': ' I enjoy conversation and experimenting different boba drinks with my friends and family.',
            'image': './static/img/boba.png'
        },
    ]
    return render_template('hobby.html',title="MLH Fellow", hobbies=hobbies)
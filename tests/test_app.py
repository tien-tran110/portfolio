import unittest
import os 
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title> Home </title>" in html
        # TODO: Add more test relating to the home page
        # print(response.data)
        # Test if the image is in the response
        assert b'../static/img/portrait.jpg' in response.data
        
        # Test if map exists on the page
        assert b'http://www.openstreetmap.org/copyright' in response.data
    
    # Test if the timeline page is working
    def test_timeline(self):
        response = self.client.get('/timeline')
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert b'<h2 class="mb-4">Previous Requests</h2>' in html
        
    # Test if the hobby page is working
    def test_hobby(self):
        response = self.client.get('/hobby')
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert 'I love the sound of guitar and learning how to play is really rewarding.' in html
        assert 'Hiking' in html

    def test_timeline(self):
        response = self.client.get('/api/timeline_post')
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        # TODO: Add more test relating to /api/timeline_post GET and POST apis
        # Test POST /api/timeline_post
        post_response = self.client.post('/api/timeline_post', data={
            'name': 'Test User',
            'email': 'test1@example.com',
            'content': 'Hello, world!'
        })
        assert post_response.status_code == 200
        post_json = post_response.get_json()
        assert "id" in post_json
        assert post_json['name'] == 'Test User'
        assert post_json['email'] == 'test1@example.com'
        assert post_json['content'] == 'Hello, world!'

        # Test GET /api/timeline_post after a post
        response = self.client.get('/api/timeline_post')
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 1
        post = json["timeline_posts"][0]
        assert post['name'] == 'Test User'
        assert post['email'] == 'test1@example.com'
        assert post['content'] == 'Hello, world!'
        
        # Test correct order of posts
        post_response = self.client.post('/api/timeline_post', data={
            'name': 'Test User 2',
            'email': 'test2@example.com',
            'content': 'Hello, world 2!'
        })
        assert post_response.status_code == 200
        
        response = self.client.get('/api/timeline_post')
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 2
        post = json["timeline_posts"][0]
        assert post['name'] == 'Test User 2'
        assert post['email'] == 'test2@example.com'
        assert post['content'] == 'Hello, world 2!'
        post = json["timeline_posts"][1]
        assert post['name'] == 'Test User'
        assert post['email'] == 'test1@example.com'
        assert post['content'] == 'Hello, world!'
        
        
        # Test DELETE /delete/<id> with valid id
        post_id = post['id']
        delete_response = self.client.delete(f'/delete/{post_id}')
        assert delete_response.status_code == 200
        assert delete_response.data == b"Post was deleted successfully!"
        
        # Test DELETE /delete/<id> with invalid id
        delete_response = self.client.delete(f'/delete/{post_id}')
        assert delete_response.status_code == 200
        assert delete_response.data == b"Post not found!"

        # Test POST /api/timeline_post with missing fields
        response = self.client.post('/api/timeline_post', data={})
        assert response.status_code == 400  # or appropriate error code
        
        # Test POST /api/timeline_post with invalid email
        response = self.client.post('/api/timeline_post', data={
            'name': 'Test User',
            'email': 'test1@example',
            'content': 'Hello, world!'
        })
        assert response.status_code == 400
        assert response.data == b"Invalid email address!"
        
        # Test POST /api/timeline_post with empty data
        response = self.client.post('/api/timeline_post', data={
            'name': '',
            'email': '',
            'content': ''
        })
        assert response.status_code == 400
        assert response.data == b"Name is required!"

if __name__ == '__main__':
    unittest.main() 
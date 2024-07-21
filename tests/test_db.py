import unittest
from peewee import *
import time
from playhouse.shortcuts import model_to_dict

from app import TimelinePost

MODELS = [TimelinePost]

# use an in-memory SQLite for tests.
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind model classes to test db. Since we have a complete list of
        # all models, we do not need to recursively bind dependencies.
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        # Not strictly necessary since SQLite in-memory databases only live
        # for the duration of the connection, and in the next step we close
        # the connection...but a good practice all the same.
        test_db.drop_tables(MODELS)

        # Close connection to db.
        if not test_db.is_closed():
            test_db.close()

        # If we wanted, we could re-bind the models to their original
        # database here. But for tests this is probably not necessary.
    
    def test_timeline_post(self):
        # Create 2 timeline posts
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello World, I\'m John')
        assert first_post.id == 1
        time.sleep(1)
        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello World, I\'m Jane')
        assert second_post.id == 2
        # TODO: Get timeline posts and assert that they are correct
        timeline_posts = [model_to_dict(post) for post in TimelinePost.select().order_by(TimelinePost.created_at.desc())]
        
        # print(timeline_posts)
        
        # Check if the id is correct
        assert timeline_posts[0]['id'] == 2
        assert timeline_posts[1]['id'] == 1
        
        # Check if the name is correct
        assert timeline_posts[0]['name'] == 'Jane Doe'
        assert timeline_posts[1].get('name') == 'John Doe'
        
        # Check if the email is correct
        assert timeline_posts[1].get('email') == 'john@example.com'
        assert timeline_posts[0].get('email') == 'jane@example.com'
        
        # Check if the content is correct
        assert timeline_posts[0].get('content') == 'Hello World, I\'m Jane'
        assert timeline_posts[1].get('content') == 'Hello World, I\'m John'
        
if __name__ == '__main__':
    unittest.main()
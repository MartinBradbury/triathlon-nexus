from django.contrib.auth.models import User
from.models import Posts 
from rest_framework import status
from rest_framework.test import APITestCase

class PostListViewTests(APITestCase):
    # Method to set up the environment for each test case
    def setUp(self):
        # Create two users for testing purposes
        User.objects.create_user(username='jacob', password='pw')
        User.objects.create_user(username='john', password='secret')
        # Retrieve the 'jacob' user
        self.jacob = User.objects.get(username='jacob')
        # Create a post owned by 'jacob'
        self.post = Posts.objects.create(owner=self.jacob, title='Original Title')


    def test_can_list_posts(self):
        # Create another post by 'jacob' for this test
        Posts.objects.create(owner=self.jacob, title='test title')
        # Send a GET request to the '/posts/'
        response = self.client.get('/posts/')
        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_logged_in_user_can_create_post(self):
        # Log in as 'jacob'
        self.client.login(username='jacob', password='pw')
        # Send a POST request to the '/posts/' with new data
        response = self.client.post('/posts/', {'title': 'test title'})
        # Check if the total number of posts has increased by 1
        count = Posts.objects.count()
        self.assertEqual(count, 2)
        # Assert that the response status code indicates successful creation
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_logged_out_user_cannot_create_posts(self):
        # Attempt to send a POST request to the '/posts/' without logging in
        response = self.client.post('/posts/', {'title': 'test title'})
        # Assert that the response status code is 403 Forbidden
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)



class PostDetailViewTest(APITestCase):
    def setUp(self):
        # Create two users for testing purposes
        User.objects.create_user(username='jacob', password='pw')
        User.objects.create_user(username='john', password='secret')
        # Retrieve the 'jacob' user
        self.jacob = User.objects.get(username='jacob')
        # Create a post owned by 'jacob'
        self.post = Posts.objects.create(owner=self.jacob, title='Original Title')



    def test_can_retrieve_post_using_valid_id(self):
        # Send a GET request to list the first post in the list.
        response = self.client.get('/posts/1/')
        # Assert that the response will return the title of the post
        self.assertEqual(response.data['title'], 'Original Title')
        #Assert that the title matches the assertion.
        self.assertEqual(response.status_code,
        status.HTTP_200_OK)


    def test_cannot_retrieve_not_created_posts(self):
        # Send a GET request to list post 500.
        response = self.client.get('/posts/500/')
        # Assert that post 500 cannot be found.
        self.assertEqual(response.status_code, 
        status.HTTP_404_NOT_FOUND)
        

    def test_logged_in_user_can_edit_own_post(self):
        # Log in as 'jacob'
        self.client.login(username='jacob', password='pw')
        # Send a PUT request to update the title of the post owned by 'jacob'
        response = self.client.put(f'/posts/{self.post.id}/', {'title': 'Updated Title'})
        # Assert that the response status code is 200 OK, indicating successful update
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Refresh the post from the database to get the latest state
        self.post.refresh_from_db() 
        # Assert that the post's title has been updated successfully
        self.assertEqual(self.post.title, 'Updated Title')


    def test_different_user_cannot_edit_others_posts(self):
        # Log in as 'john'
        self.client.login(username='john', password='secret')
        # Attempt to send a PUT request to update the post owned by 'jacob'
        response = self.client.put(f'/posts/{self.post.id}/', {'title': 'Unauthorized Edit'})
        # Assert that the response status code is 403 Forbidden
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_logged_in_user_can_delete_own_post(self):
        # Log in as 'jacob'
        self.client.login(username='jacob', password='pw')
        # Send a DELETE request to remove the post owned by 'jacob'
        response = self.client.delete(f'/posts/{self.post.id}/')
        # Assert that the response status code is 204 No Content, indicating successful deletion
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Assert that the post no longer exists in the database
        self.assertFalse(Posts.objects.filter(id=self.post.id).exists())


    def test_different_user_cannot_delete_others_posts(self):
        # Log in as 'john'
        self.client.login(username='john', password='secret')
        # Attempt to send a DELETE request to remove the post owned by 'jacob'
        response = self.client.delete(f'/posts/{self.post.id}/')
        # Assert that the response status code is 403 Forbidden
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Assert that the post still exists in the database
        self.assertTrue(Posts.objects.filter(id=self.post.id).exists())




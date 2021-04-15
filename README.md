# drf_blog_api
Simple blog api with JWT authentication. Project was made using Django + Django Rest Framework + djangorestframework-simplejwt.

There are some ideas for improvement current version of API, like replacing user activity fields in database with Redis and migrating to PostgreSQL, that i will implement later. 


## How to run test server?
```
git clone https://github.com/unusualjayden/drf_blog_api.git
cd drf_blog_api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Endpoints
```[POST] api/registration/``` - Registration view. Provide username, password and email - get token pair.

```[POST] api/auth/token/``` - Token obtain view. Provide username and email - get token pair.

```[POST] api/auth/refresh/``` - Token refresh view. Provide refresh token - get access token.

```[GET] api/user/<username>/``` - View, that shows all posts made by particular user.

```[GET POST DELETE PUT] api/post/``` -  CRUD view for posts.

```[GET] api/post/<post_id>/``` - Retrieve one post by <post_id>.

```[POST] api/post/<post_id>/like/``` - Like/unlike post by <post_id>.

```[GET] api/posts/analytics/[?date_from=&date_to=]``` - Retrieve number of likes per post per day in range of date_from to date_to.

```[GET] api/activity/<username>/``` - Get last login and last request of user by <username>.

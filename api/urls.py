from django.urls import include, path

urlpatterns = [
    path('', include('posts.urls')),
    path('', include('users.urls'))
]

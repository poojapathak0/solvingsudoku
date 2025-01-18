from django.urls import path, include
app_name = 'accounts'
urlpatterns = [ 
    #include default auth urls.
    path('', include('django.contrib.atuh.urls')),
]
from django.urls import path
from . import views
app_name = "newsletter_app"

urlpatterns = [  
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('top_contributors', views.top_contributors, name="top_contributors"),
    path('top_viewed', views.top_viewed, name="top_viewed"),
    path('domain/?P<int:domain_id>', views.domain, name="domain"),
    path('add_view/?P<int:article_id>', views.add_view, name="add_view"),    
]



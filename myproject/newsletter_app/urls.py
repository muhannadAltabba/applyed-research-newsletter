from django.urls import path
from . import views
app_name = "newsletter_app"

urlpatterns = [  
    path('', views.home, name="home"),
    path('how-to-publish/', views.how_to_publish, name="how_to_publish"),
    path('statistics', views.statistics, name="statistics"),
    path('top-contributors', views.top_contributors, name="top_contributors"),
    path('top-viewed', views.top_viewed, name="top_viewed"),
    path('domain/?P<int:domain_id>', views.domain, name="domain"),
    path('add_view/?P<int:article_id>', views.add_view, name="add_view"),    
]



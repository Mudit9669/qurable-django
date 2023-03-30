from . import views
from django.urls import path , include

app_name='main'

urlpatterns = [
    path('',views.index , name='index'),
    path('inside1/',views.inside1,name='inside1'),
    path('inside2/',views.inside2,name='inside2'),
    path('inside3/',views.inside3,name='inside3'),
    path('inside4/',views.inside4,name='inside4'),
    path('inside5/',views.inside5,name='inside5'),
    path('inside6/',views.inside6,name='inside6'),
    path('inside7/',views.inside7,name='inside7'),
    path('inside8/',views.inside8,name='inside8'),
    path('inside9/',views.inside9,name='inside9'),
    path('parent1/',views.parent1,name='parent1'),
    path('parent2/',views.parent2,name='parent2'),
    path('parent3/',views.parent3,name='parent3'),
    path('parent4/',views.parent4,name='parent4'),
    
]

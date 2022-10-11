from django.urls import path

from . import views

urlpatterns = [
    path('', views.teacher, name='teacher'),
    path('create/', views.create, name='create'),
    path('creatediscipline/', views.creatediscipline, name='creatediscipline'),
    path('createteacher/', views.createteacher, name='createteacher'),
    path('thanks/', views.thanks, name='thanks'),
    path('showgroupp/', views.showgroupp, name='showgroupp')

]
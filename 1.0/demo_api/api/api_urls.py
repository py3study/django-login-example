from django.conf.urls import url
# from django.urls import path
from api import views

urlpatterns = [
    # 学校
    # url(r'login/$', views.SchoolView.as_view()),
    # url(r'login/$',views.UserlView.as_view({'post':'login'}),name='login'),
    url(r'login/$', views.UserlView.as_view())
    # path('login/', views.UserlView.as_view())
]
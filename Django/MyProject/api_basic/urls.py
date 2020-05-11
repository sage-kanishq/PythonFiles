from . import views
from django.urls import path,include

urlpatterns = [

    path('generic/article/<int:id>',views.GenericAPIView.as_view()),
    path('article/',views.article_list,name="articles"),
    path('detail/<int:pk>/',views.article_detail,name="detail"),
    path('generic/article/',views.GenericAPIView.as_view(),name="generic articles"),
]

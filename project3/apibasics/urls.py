from django.urls import path
from .views import article_list, article_detail,ArticleAPIView,ArticleDetail
urlpatterns = [
   # path('articles/', article_list, name='articles'),
    path('articles/', ArticleAPIView.as_view()),
   # path('detail/<int:pk>/', article_detail, name='details'),
    path('detail/<int:pk>/',ArticleDetail.as_view() ),
]
from django.urls import include, path
from watchlist_app.api.views import ReviewCreate, ReviewDetail, ReviewList, WatchDetailAV, WatchListAV, StreamPlatformAV, StreamDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie_list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='movie_detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>', StreamDetailAV.as_view(), name='stream_detail'),
    # path('review/', ReviewList.as_view(), name='review_list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review_detail'),
    path('movie/<int:pk>/review', ReviewList.as_view(), name='review_list'),
    path('movie/<int:pk>/review-create', ReviewCreate.as_view(), name='review_create'),
]
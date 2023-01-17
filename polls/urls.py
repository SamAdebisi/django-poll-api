from django.urls import path, include

from .apiviews import (
    PollList, PollDetail,
    ChoiceList, CreateVote,
    PollViewSet, UserCreate
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

urlpatterns = [
    # path('polls/', polls_list, name="polls_list"),
    # path('polls/', PollViewSet.as_view({'get': 'queryset'}), name="polls_list"),
    path('polls/', PollList.as_view(), name="polls_list"),

    # path('polls/<int:pk>/', polls_detail, name="polls_detail"),
    # path('polls/<int:pk>/', PollViewSet.as_view({'get': 'polls'}),
    #      name="polls_detail"),
    path('polls/<int:pk>/', PollDetail.as_view(),
         name="polls_detail"),

    path('polls/<int:pk>/choices/',
         ChoiceList.as_view(), name="choice_list"),

    path('polls/<int:pk>/choices/<int:choice_pk>/vote/',
         CreateVote.as_view(), name="create_vote"),

    path('users/', UserCreate.as_view(), name="user_create"),
]

urlpatterns += router.urls

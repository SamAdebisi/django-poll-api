from django.urls import path, include

# from .views import polls_list, polls_detail
from .apiviews import PollList, PollDetail

urlpatterns = [
    # path('polls/', polls_list, name="polls_list"),
    path('polls/', PollList.as_view(), name="polls_list"),

    # path('polls/<int:pk>/', polls_detail, name="polls_detail"),
    path('polls/<int:pk>/', PollDetail.as_view(), name="polls_detail"),
]

""" Definitions of url patterns """
# pylint: disable=E1101
from django.urls import path
from . import views


urlpatterns = [
    path("team-chat/<int:team_id>", views.TeamChat.as_view()),
    path("team-chat-post/<int:team_id>", views.TeamChatPost.as_view()),
    path("team-chat-put/<int:message_id>", views.TeamChatPut.as_view()),
    path("team-chat-delete/<int:message_id>", views.TeamChatDelete.as_view()),
    path("team-chat-list/", views.TeamChatList.as_view()),
]

from django.urls import path
from . import views

app_name='bang'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('signin/', views.signin,name="signin"),
    path('idfind', views.idfind, name='idfind'),
    path('idfind_ok', views.idfind_ok, name='idfind_ok'),
    path('pwfind', views.pwfind, name='pwfind'),
    path('pwfind_ok', views.pwfind_ok, name='pwfind_ok'),
    path('pwfind_submit', views.pwfind_submit, name='pwfind_submit'),
    path('signin/signin_ok', views.signin_ok,name="signin_ok"),
    path('signup/', views.signup,name="signup"),
    path('signup/signup_ok', views.signup_ok,name="signup_ok"),
    path('profile/', views.profile, name="profile"),
    path('profile/verify_pwd', views.verify_pwd, name='verify_pwd'),
    path('profile/verify_pwd/verify_pwd_ok', views.verify_pwd_ok, name='verify_pwd_ok'),
    path('profile/verify_pwd/update_ok', views.update_ok, name='update_ok'),

    path('signout/', views.signout, name="signout"),
    path('board/', views.board, name='board'),
    path('board/search', views.search, name='search'),
    path('board/order', views.order, name='order'),
    path('board/<ccode>', views.boardcategory, name='boardcategory'),
    path('board/detail/<int:id>', views.detail, name='detail'),
    path('board/detail/<int:id>/comments', views.comments_create, name='comments'),
    path('board/detail/<int:id>/comments/<int:comment_id>/delete',
         views.comments_delete, name='comments_delete'),
    path('board/detail/<int:id>/like', views.like, name='like'),
    path('board/detail/<int:id>/delete', views.articleDelete, name="articleDelete"),
    path('board/detail/<int:id>/article_update_ok', views.articleUpdate, name="article_update_ok"),
    path('write/', views.write, name='write'),
    path('write/write_ok', views.write_ok, name='write_ok'),
    path('db/champion/', views.champion, name='champion'),
    path('db/champion/ch_details/<name>', views.ch_details, name='ch_details'),
    path('db/map/', views.map, name='map'),
    path('db/map/Howling_Abyss', views.howling_abys, name='Howling_Abys'),
    path('db/map/Summoners_Rift', views.summoners_rift, name='Summoners_Rift'),
    path('db/spell', views.spell, name='spell'),
    path('db/rune', views.rune, name='rune'),
    path('videos/', views.videos, name='videos'),

]


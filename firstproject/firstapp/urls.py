from django.urls import path
from . import views

urlpatterns=[
  path('',views.home,name='homepage'),
  path('about',views.about),
  path('contact',views.contact),

  path('audio', views.audio),
  path('ss',views.some,name='some'),
  path('ds',views.upl,name='upl'),
  path('sp', views.son, name='son'),
  path('translated',views.translated,name='translated'),
  # path('upload', views.upload),
  path('collection',views.collection),
  path('bookpost', views.bookpost),
  path('mybook', views.mybook),
  path('fbook', views.fbook),
  path('four', views.four),
  path('five', views.five),
  path('six', views.six),
  # path('book/<int:id>', views.bookpost, name='bookpost'),

]
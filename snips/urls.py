from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snips import views
from django.urls import path, include
# from views import add_book


urlpatterns = [
    # path("", views.index, name="index"),
    # path("add_book/", views.add_book, name="add_book"),
    # path('snips/', views.snips_list),
    path('snips/', views.snips_list),
    path('snips/<int:pk>', views.snips_detail),
    
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
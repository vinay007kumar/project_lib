from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snips import views
from django.urls import path, include


urlpatterns = [
    # path('snips/', views.snips_list),
    path('snips/', views.SnipsList.as_view()),
    path('snips/<int:pk>', views.SnipsDetail.as_view()),
    
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
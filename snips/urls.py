from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snips import views
# from views import add_book


urlpatterns = [
    # path("", views.index, name="index"),
    # path("add_book/", views.add_book, name="add_book"),
    # path('snips/', views.snips_list),
    path('snips/', views.snips_list),
    path('snips/<int:pk>', views.snips_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
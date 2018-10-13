from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'accounts'

# urlpatterns = [
#     # path('student/<int:pk>', views.student)
#     url(r'^student_detail/(?P<pk>\d+)/', views.student_detail),
#     url(r'^student/', views.student)
# ]
urlpatterns = [
    url(r'^student_list/', views.get_students_list.as_view()),
    url(r'^student_detail/(?P<pk>\d+)/$', views.get_students_detail.as_view())
]

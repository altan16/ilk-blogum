import django.urls

from . import views

urlpatterns=[
	django.urls.path('',views.index1, name='gameindex'),
]

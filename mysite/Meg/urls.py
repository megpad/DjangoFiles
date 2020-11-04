#from django.contrib import admin
from django.urls import path
#from django.conf.urls import url, include

#from django.conf.urls import url
from . import views

app = "Meg"
urlpatterns = [
	#
	#url('myapp1/', include('myapp1.urls')),
    #url('myapp2/', include('myapp2.urls')),
    #path('admin/', admin.site.urls),

    #url('', views.index, name='index'), 

    #path('', views.index, name='index'),
    path('article/', views.article, name='article'),
    #path('page/<int:page_id>/', views.page, name='page'),
	]

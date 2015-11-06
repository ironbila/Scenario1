from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
     url(r'^$', views.index, name='index'),
     url(r'^viewTodo$', views.view_todo),
     url(r'^addToTodo/(?P<id>[1-9]+)/$', views.create_todo),
	 url(r'^deleteTodo/(?P<id>[1-9]+)/$', views.delete_todo),
	 url(r'^completeTodo/(?P<id>[1-9]+)/$', views.complete_todo),
     url(r'^viewList$', views.view_lists),
     url(r'^addToList$', views.create_list),
     url(r'^deleteList/(?P<id>[1-9]+)/$', views.delete_list),
     url(r'^newList$', views.view_list_form),
     url(r'^editList/(?P<id>[1-9]+)/$', views.edit_list_form),
     url(r'^editTodo/(?P<id>[1-9]+)/$',views.edit_todo_form),
     url(r'^changeList/(?P<id>[1-9]+)/$', views.edit_list),
     url(r'^changeTodo/(?P<id>[1-9]+)/$', views.edit_todo),

    #User accounts stuff


]

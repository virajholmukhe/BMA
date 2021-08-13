from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home),
    path('view_all_idols_list',views.showAllIdols),
    path('categories_list/<cid>',views.showCategorywiseIdols),
    path('view_idol/<pid>',views.showIdol),
    path('search_text',views.search),



    path('',views.test),

]



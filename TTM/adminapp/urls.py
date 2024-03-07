import views
from django.urls import path
from.import views
urlpatterns=[
    path("checkadminlogin",views.checkadminlogin,name="checkadminlogin"),
    path("checkregisteration",views.checkregisteration,name="checkregisteration"),
    path("checkpackages",views.checkpackages,name="checkpackages"),
    path("viewplaces",views.viewplaces,name="viewplaces"),
    path("changepassword",views.checkChangePassword,name="changepassword"),
    path("logout",views.logout,name="logout"),
    path("ttmhome",views.ttmhome,name="ttmhome")
]

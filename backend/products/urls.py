from django.urls import path

from . import views 

urlpatterns = [
    path('<int:pk>/update' , views.ProductUpdatesApiView.as_view() ,) ,
    path('<int:pk>/delete' , views.ProductDestroyApiView.as_view() ,) ,
    path('<int:pk>/' , views.ProductDetailsApiView.as_view() ,) ,
    path('' , views.ProductCreateApiView.as_view() ,),
]

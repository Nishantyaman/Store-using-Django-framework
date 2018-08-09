from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    #path('product/',views.productlist.as_view(),name='product')
    path('home/',views.homeform,name='home'),
    path('add/',views.addform,name='add'),
    path('product/',views.index,name='product'),
    path('details/',views.readable_format,name='details')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


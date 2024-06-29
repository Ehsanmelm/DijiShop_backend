from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('seller_signup' ,views.SellerViewSet  , basename='seller_signup')
router.register('add_store' ,views.StoreViewset  , basename='add_store')
router.register('stuffs' ,views.StuffViewset  , basename='stuffs')

urlpatterns = []
urlpatterns += router.urls
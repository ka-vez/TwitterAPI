from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.endopoints),
    path('advocates/', views.advocates_list,),
    # path('advocates/<str:username>', views.advocate_detail),
    path('advocates/<str:username>', views.AdvocatesDetail.as_view(), name='advocate-detail'),
    path('company/', views.company_list, name='company-detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
from django.contrib import admin
from core.views import DashboardView
from django.urls import path, include
from users.views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # App Routes
    path("api/", include("appointments.urls")),
    path("api/users/", include("users.urls")),

    # JWT Authentication
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # API Schema & Docs
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    
    path("admin/", admin.site.urls),
    path("api/", include("appointments.urls")),
    path("api/dashboard/", DashboardView.as_view()),
    
    path("api/token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
]
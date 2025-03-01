from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('UsersApp.urls')),
    
    #JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczNjc2NTEyMCwiaWF0IjoxNzM2Njc4NzIwLCJqdGkiOiIwZDE1YmEzYWVmYzg0Y2JmYjBmYTQxNTQwY2RjOTZlMSIsInVzZXJfaWQiOjF9.RsER2V2K4FkXgTEBGgGDAFaXr7yT7lo7NA4yjzOj2uI",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM2NjgyMzIwLCJpYXQiOjE3MzY2Nzg3MjAsImp0aSI6IjM2OTViNDY4MmJmMjQxZjc4YWY5MjRjOTBmYTAwNWI5IiwidXNlcl9pZCI6MX0.DyVIijlLCu1EGSmJmhPACmQbMImPFqhLkkQKSl4saW8"
# }
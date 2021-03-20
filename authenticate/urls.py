from django.urls import path, include

urlpatterns = [
    # path('rest-auth/login/', CustomLoginView.as_view(), name='login' ),
    # path('rest-auth/password/reset/confirm/', CustomPasswordResetConfirmView.as_view(), name='password-reset-confirm' ),
    # path('rest-auth/password/reset/', CustomPasswordResetView.as_view(), name='password-reset' ),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]
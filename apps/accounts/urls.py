from django.urls import path
from .views import ClientView,ClientViewState,ClientForStoreView


urlpatterns=[
    path('accounts/',ClientView.as_view(),name="accounts_list"),
    path('accounts/<int:id>',ClientView.as_view(),name="accounts_process"),
    path('accounts/states/<int:id>',ClientViewState.as_view(),name="accounts_state_process"),
    path('accounts/store/<int:id>',ClientForStoreView.as_view(),name="accounts_store_process")
]
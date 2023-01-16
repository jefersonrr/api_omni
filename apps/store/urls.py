from django.urls import path
from .views import StoreView, StateView, CityView, CountryView,CityforStateView


urlpatterns=[
    path('store/',StoreView.as_view(),name="store_list"),
    path('store/<int:id>',StoreView.as_view(),name="store_process"),
    path('country/',CountryView.as_view(),name="country_list"),
    path('country/<int:id>',CountryView.as_view(),name="country_process"),
    path('state/',StateView.as_view(),name="state_list"),
    path('state/<int:id>',StateView.as_view(),name="state_process"),
    path('city/',CityView.as_view(),name="city_list"),
    path('city/<int:id>',CityView.as_view(),name="city_process"),
    path('city/state/<int:id>',CityforStateView.as_view(),name="city_state_process"),
]
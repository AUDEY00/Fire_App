from django.contrib import admin
from django.urls import path
from fire.views import HomePageView,ChartView,PieCountbySeverity,LineCountbyMonth,MultilineIncidentTop3Country,multipleBarbySeverity, IncidentList, IncidentCreateView, IncidentUpdateView, IncidentDeleteView,FirefightersList,FirefightersCreateView,FirefightersUpdateView,FirefightersDeleteView,FireStationList,FireStationCreateView,FireStationUpdateView,FireStationDeleteView,FireTruckList,FireTruckCreateView,FireTruckUpdateView,FireTruckDeleteView,WeatherConditionsList,WeatherConditionsCreateView,WeatherConditionsUpdateView,WeatherConditionsDeleteView,LocationsList,LocationsCreateView,LocationsUpdateView,LocationsDeleteView
from fire import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('stations', views.map_station, name='map-station'),
    path('incidents', views.map_incident, name='map-incident'),
    path('dashboardchart', ChartView.as_view(), name='dashboard-chart'),
    path('chart/', PieCountbySeverity, name='chart'),
    path('lineChart/', LineCountbyMonth, name='chart'),
    path('multilineChart/', MultilineIncidentTop3Country, name='chart'),
    path('multiBarChart/', multipleBarbySeverity, name='chart'),
    path('incident_list', IncidentList.as_view(), name='incident-list'),
    path('incident_list/add', IncidentCreateView.as_view(), name='incident-add'),
    path('incident_list/<pk>',IncidentUpdateView.as_view(), name='incident-update'),
    path('incident_list/<pk>/delete', IncidentDeleteView.as_view(), name='incident-delete'),
    path('Firefighters_list', FirefightersList.as_view(), name='Firefighters-list'),
    path('Firefighters_list/add', FirefightersCreateView.as_view(), name='Firefighters-add'),
    path('Firefighters_list/<pk>',FirefightersUpdateView.as_view(), name='Firefighters-update'),
    path('Firefighters_list/<pk>/delete', FirefightersDeleteView.as_view(), name='Firefighters-delete'),
    path('FireStation_list', FireStationList.as_view(), name='FireStation-list'),
    path('FireStation_list/add', FireStationCreateView.as_view(), name='FireStation-add'),
    path('FireStation_list/<pk>',FireStationUpdateView.as_view(), name='FireStation-update'),
    path('FireStation_list/<pk>/delete', FireStationDeleteView.as_view(), name='FireStation-delete'),
    path('FireTruck_list', FireTruckList.as_view(), name='FireTruck-list'),
    path('FireTruck_list/add', FireTruckCreateView.as_view(), name='FireTruck-add'),
    path('FireTruck_list/<pk>',FireTruckUpdateView.as_view(), name='FireTruck-update'),
    path('FireTruck_list/<pk>/delete', FireTruckDeleteView.as_view(), name='FireTruck-delete'),
    path('WeatherConditions_list', WeatherConditionsList.as_view(), name='WeatherConditions-list'),
    path('WeatherConditions_list/add', WeatherConditionsCreateView.as_view(), name='WeatherConditions-add'),
    path('WeatherConditions_list/<pk>',WeatherConditionsUpdateView.as_view(), name='WeatherConditions-update'),
    path('WeatherConditions_list/<pk>/delete', WeatherConditionsDeleteView.as_view(), name='WeatherConditions-delete'),
    path('Locations_list', LocationsList.as_view(), name='Locations-list'),
    path('Locations_list/add', LocationsCreateView.as_view(), name='Locations-add'),
    path('Locations_list/<pk>',LocationsUpdateView.as_view(), name='Locations-update'),
    path('Locations_list/<pk>/delete', LocationsDeleteView.as_view(), name='Locations-delete'),

]

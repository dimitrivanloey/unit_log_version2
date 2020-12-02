"""Defines URL patterns for learning_logs"""

from django.urls import path

from . import views

app_name = 'unit_logs'
urlpatterns = [
    # Home page
    path('', views.index, name ='index'),
    # Winx
    path('winxes/', views.winxes, name ='winxes'),
    path('winxes/<int:winx_id>/', views.winx, name='winx'),
    path('winx/', views.winx_page, name ='winx_page'),
    # Arkle
    path('arkles/', views.arkles, name ='arkles'),
    path('arkles/<int:arkle_id>/', views.arkle, name='arkle'),
    path('arkle/', views.arkle_page, name ='arkle_page'),
    # Denman
    path('denmans/', views.denmans, name ='denmans'),
    path('denmans/<int:denman_id>/', views.denman, name='denman'),
    path('denman/', views.denman_page, name ='denman_page'),
    # Enable
    path('enables/', views.enables, name ='enables'),
    path('enables/<int:enable_id>/', views.enable, name='enable'),
    path('enable/', views.enable_page, name ='enable_page'),
    # Frankel
    path('frankels/', views.frankels, name ='frankels'),
    path('frankels/<int:frankel_id>/', views.frankel, name='frankel'),
    path('frankel/', views.frankel_page, name ='frankel_page'),
    # Kauto
    path('kautos/', views.kautos, name ='kautos'),
    path('kautos/<int:kauto_id>/', views.kauto, name='kauto'),
    path('kauto/', views.kauto_page, name ='kauto_page'),
    # Page for adding a new winx
    path('new_winx/', views.new_winx, name='new_winx'),
    # Page for adding a new arkle
    path('new_arkle/', views.new_arkle, name='new_arkle'),
    # Page for adding a new denman
    path('new_denman/', views.new_denman, name='new_denman'),
    # Page for adding a new enable
    path('new_enable/', views.new_enable, name='new_enable'),
    # Page for adding a new frankel
    path('new_frankel/', views.new_frankel, name='new_frankel'),
    # Page for adding a new kauto
    path('new_kauto/', views.new_kauto, name='new_kauto'),
    # Delete units
    path('winxes/<int:winx_id>/delete', views.deletewinx, name='deletewinx'),
    path('arkles/<int:arkle_id>/delete', views.deletearkle, name='deletearkle'),
    path('denmans/<int:denman_id>/delete', views.deletedenman, name='deletedenman'),
    path('enables/<int:enable_id>/delete', views.deleteenable, name='deleteenable'),
    path('frankels/<int:frankel_id>/delete', views.deletefrankel, name='deletefrankel'),
    path('kautos/<int:kauto_id>/delete', views.deletekauto, name='deletekauto'),
    
    # New Winx entry
    path('new_winx_entry/<int:winx_id>', views.new_winx_entry, name='new_winx_entry'),
    # New Enable entry
    path('new_enable_entry/<int:enable_id>', views.new_enable_entry, name='new_enable_entry'),
    # New Arkle entry
    path('new_arkle_entry/<int:arkle_id>', views.new_arkle_entry, name='new_arkle_entry'),
    # New Denman entry
    path('new_denman_entry/<int:denman_id>', views.new_denman_entry, name='new_denman_entry'),
    # New Kauto entry
    path('new_kauto_entry/<int:kauto_id>', views.new_kauto_entry, name='new_kauto_entry'),
    # New Frankel entry
    path('new_frankel_entry/<int:frankel_id>', views.new_frankel_entry, name='new_frankel_entry'),
]


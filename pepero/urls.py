from django.urls import path
from .views import pepero_make_choco_view, pepero_make_letter_view, pepero_make_deco_view,pepero_make_sauce_view,pepero_make_start_view

app_name = 'pepero'

urlpatterns = [
    path('',pepero_make_start_view,name='pepero_start'),
    path('choco/',pepero_make_choco_view, name='pepero_choco'),
    path('sauce/',pepero_make_sauce_view, name='pepero_sauce'),
    path('deco/',pepero_make_deco_view, name='pepero_deco'),
    path('letter/',pepero_make_letter_view, name='ppepero_letter'),
]
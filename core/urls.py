from django.conf import settings
from django.conf.urls.defaults import url, patterns, include
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from core.views import *

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template':'home.html'}),
    url(r'^dump$', direct_to_template, {'template':'dump.html'}),
    url(r'^games/all$', all_games, name="all-games"),
    url(r'^games/add$', add_game, name="add-game"),
    url(r'^games/view/(?P<game_id>[\w|-]+)$', view_game, name="view-game"),
    
    url(r'^games/(?P<game_id>[\w|-]+)/level/add$', add_game_level, name="add-game-level"),
    
    url(r'^games/(?P<game_id>[\w|-]+)/(?P<game_level_id>[\w|-]+)/apt/submit$', add_apt, name="add-apt"),
    url(r'^games/(?P<game_id>[\w|-]+)/(?P<game_level_id>[\w|-]+)/apt/all$', view_apts, name="view-apts"),
)

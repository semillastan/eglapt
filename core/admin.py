from django.contrib import admin
from accounts.models import *
from core.models import *

class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'game_id', 'api_key','public','date_created','created_by']
    list_filter  = ['name']

admin.site.register(Game, GameAdmin)

class GameLevelAdmin(admin.ModelAdmin):
    list_display = ['game','level','difficulty','date_created','created_by']
    list_filter = ['game']
    
admin.site.register(GameLevel, GameLevelAdmin)

class APTAdmin(admin.ModelAdmin):
    list_display = ['user','game_level','date_played','total_score','playing_time']
    list_filter = ['user']
    
admin.site.register(APT, APTAdmin)

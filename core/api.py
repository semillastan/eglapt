from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication
from tastypie import fields
from tastypie.resources import ModelResource
from core.models import *

class GameResource(ModelResource):
    class Meta:
        queryset = Game.objects.all()
        resource_name = 'game'
	excludes = ['api_key']
	#allowed_methods = ['get']
	#authentication = ApiKeyAuthentication()

class GameLevelResource(ModelResource):
    game = fields.ForeignKey(GameResource, 'game')
    
    class Meta:
        queryset = GameLevel.objects.all()
        resource_name = 'level'
	#allowed_methods = ['get']

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'auth/user'
        excludes = ['email', 'password', 'is_superuser']
        # Add it here.
        authentication = BasicAuthentication()
	allowed_methods = ['get']

class APTResource(ModelResource):
    game_level = fields.ForeignKey(GameLevelResource, 'game_level')
    user = fields.ForeignKey(UserResource, 'user')
    
    class Meta:
        queryset = APT.objects.all()
        resource_name = 'apt'
	allowed_methods = ['get','post']
	always_return_data = True
	authentication = ApiKeyAuthentication()
	authorization = DjangoAuthorization()



from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile
from registration import signals

from helpers import get_object_or_404, render_to, reverse_redirect, get_object_or_None
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import send_mail, EmailMessage
from datetime import date

from core.models import *
from core.forms import *

@render_to('core/all-games.html')
def all_games(request):
    games = Game.objects.all()
    return { 'games':games }

@render_to('core/add-game.html')
def add_game(request):
    form = GameForm()
    if request.method == 'POST':
	form = GameForm(request.POST)
	if form.is_valid():
	    game = form.save(commit=False)
	    import uuid, hmac
	    try:
		from hashlib import sha1
	    except ImportError:
		import sha
		sha1 = sha.sha
	    new_uuid = uuid.uuid4()
	    api_key = hmac.new(str(new_uuid), digestmod=sha1).hexdigest()[0:24]
	    game.game_id = str(new_uuid)[0:8]
	    game.api_key = api_key
	    game.created_by = request.user
	    game.save()
	    return reverse_redirect('all-games')
    return { 'form':form }

@render_to('core/view-game.html')
def view_game(request, game_id=None):
    game = get_object_or_None(Game, pk=game_id)
    levels = GameLevel.objects.filter(game=game)
    return { 'game':game,'levels':levels }

@render_to('core/add-game-level.html')
def add_game_level(request, game_id=None):
    game = get_object_or_None(Game, pk=game_id)
    form = GameLevelForm()
    if request.method == 'POST':
	form = GameLevelForm(request.POST)
	if form.is_valid():
	    level = form.save(commit=False)
	    level.game = game
	    import datetime
	    level.date_created = datetime.datetime.today()
	    level.created_by = request.user
	    level.save()
	    return reverse_redirect('view-game', args=[game.id])
    return { 'form':form, 'game':game }

@render_to('core/view-game-level.html')
def view_game_level(request, game_level_id=None):
    level = get_object_or_None(GameLevel, pk=game_level_id)
    apts = APT.objects.filter(level=level)
    return { 'level':level,'apts':apts }
    
@render_to('core/add-apt.html')
def add_apt(request, game_id=None, game_level_id=None):
    level = get_object_or_None(GameLevel, pk=game_level_id)
    form = APTForm()
    if request.method == 'POST':
	form = APTForm(request.POST)
	if form.is_valid():
	    apt = form.save(commit=False)
	    apt.user = request.user
	    apt.game_level = level
	    import datetime
	    apt.date_added = datetime.datetime.today()
	    apt.added_by = request.user
	    apt.save()
	    return reverse_redirect('view-game', args=[level.game.id])
    return { 'form':form, 'level':level }

@render_to('core/view-apts.html')
def view_apts(request, game_id=None, game_level_id=None):
    level = get_object_or_None(GameLevel, pk=game_level_id)
    apts = APT.objects.filter(game_level=level)
    return { 'level':level,'apts':apts }

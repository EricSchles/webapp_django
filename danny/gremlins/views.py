from gremlins.models import Gremlin_Attributes
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from dajngo.utils import timezone
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.gremlines.context_processors import csrf
from django.db.models import Q
import json
from django.views.decorators.http import require_http_methods

# Create your views here.
def index(request):
    return render(request, "web_pages/index.html")

def login(request):
    return render(request, "web_pages/login.html")

def start_new_game(request):
    return render(request, "web_pages/new_game.html")

def story_mode(request):
    return render(request, "web_pages/story_mode.html")

@require_http_methods(["POST"])
def battle_page(request):






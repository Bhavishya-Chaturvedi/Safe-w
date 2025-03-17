from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import VoiceCommand
import openai
from django.http import HttpResponse

openai.api_key = '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'

def index(request):
    return render(request, 'voice/index.html')

def voice_input(request):
    if request.method == 'POST':
        voice_text = request.POST.get('voice_text')
        # Save the voice text to the database
        VoiceCommand.objects.create(command_text=voice_text)
        return HttpResponse(f"Received voice text: {voice_text}")

    # Retrieve all stored voice commands to display them
    commands = VoiceCommand.objects.all()
    return render(request, 'voice_input.html', {'commands': commands})


# chatbot/views.py
from django.shortcuts import render
from django.http import JsonResponse
# from .models import ChatMessage  # Temporarily commented out
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
# import google.generativeai as genai (deprecated)
from google import genai  # Updated import

client = genai.Client(api_key=settings.GEMINI_API_KEY) # ---

# Create your views here.
def home(request):
    return JsonResponse({'status': 'success', 'message': 'go to /chat to start chatting with the bot!'})


models = ["gemini-2.5-flash", "gemini-3-flash-preview", "gemini-3.1-flash-lite-preview"]

@csrf_exempt
def chat_view(request):
    if request.method == "POST":
        user_message = request.POST.get("message")
        print("Received message:", user_message)

        try:            
            response = client.models.generate_content(
                model=models[2],  # ai model -----
                contents=user_message
            )
            bot_message = response.text
            print("Bot response:", bot_message)
        except Exception as e:
            print("Error from Gemini:", str(e))
            bot_message = f"Error: {str(e)}"

        # Temporarily commenting out database save to test basic functionality
        # ChatMessage.objects.create(
        #     user="Anonymous",
        #     message=user_message, 
        #     bot_response=bot_message
        # )
        
        return JsonResponse({"response": bot_message})

    return render(request, "chatbot/chat.html")

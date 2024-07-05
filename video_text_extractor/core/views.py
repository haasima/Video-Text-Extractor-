from django.shortcuts import render
from django.http import JsonResponse
import pytesseract
from PIL import Image
from io import BytesIO
import base64
from googletrans import Translator
import json

def index(request):
    return render(request, 'core/index.html')


def process_frame(request):
    if request.method == 'POST':
        image_data = request.POST.get('image')
        image_data = image_data.split(',')[1]
        image = Image.open(BytesIO(base64.b64decode(image_data)))
        text = pytesseract.image_to_string(image, lang='eng')
        return JsonResponse({'text': text})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def translate_text(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            text = data.get('text')
            language = data.get('language')
            translator = Translator()
            translation = translator.translate(text, dest=language).text
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500) 
        return JsonResponse({'translation': translation})
    return JsonResponse({'error': 'Invalid request'}, status=400)
        
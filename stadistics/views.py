from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Watersample, Modelprofile
from django.forms.models import model_to_dict
import json, datetime

# Create your views here.
@csrf_exempt
def save_water_sample(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ph = float(data.get('ph', 0.0))
        condu = float(data.get('condu', 0.0))
        termo = float(data.get('termo', 0.0))
        otro_sensor = float(data.get('otroSensor', 0.0))
        user_id = data.get('user_id')

        if user_id is not None:
            sensor_data = Watersample(timestamp=datetime.datetime.now(), ph=ph, condu=condu, termo=termo, otroSensor=otro_sensor, user_id=user_id)
            sensor_data.save()
            return JsonResponse({'message': 'Data saved correctly.', 'status': True})
        else:
            return JsonResponse({'message': 'Invalid user_id.', 'status': False})
    else:
        return JsonResponse({'message': 'Method not allowed.', 'status': False})

def get_sample_by_day(request, date):
    if request.method == 'GET':
        results = Watersample.objects.filter(timestamp__date=date)
        if results:
            serialized_data = [model_to_dict(result) for result in results]
            return JsonResponse({'data': serialized_data, 'message': 'Sample found.', 'status': True})
        else:
            return JsonResponse({'message': 'Data not found.', 'status': False})
    else:
        return JsonResponse({'message': 'Method not allowed.', 'status': False})

def get_model_profile(request):
    model_profile = Modelprofile.objects.first()
    model_profile_dict = {
        'ph': model_profile.ph,
        'termo': model_profile.termo,
        'condu': model_profile.condu,
        'otroSensor': model_profile.otroSensor,
    }
    return JsonResponse({'data': model_profile_dict, 'status': True})

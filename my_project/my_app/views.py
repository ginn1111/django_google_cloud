from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from my_app.models import SensorData
from datetime import date

# Create your views here.


def chart(request):
    return render(request, 'dht11/chart.html')


def dht11(request):
    dic = request.GET
    print(dic.get("hum"))
    print(dic.get("temp"))
    sensor_data = SensorData(humidity=dic.get(
        "hum"), temperature=dic.get("temp"), time=date.today())
    sensor_data.save()
    return JsonResponse({"status": "ok"})


def get_data(request):
    data = SensorData.objects.all()
    if len(data):
        hum_data = [(data.humidity, data.time) for _, data in enumerate(data)]
        temp_data = [(data.temperature, data.time)
                     for _, data in enumerate(data)]
    else:
        return JsonResponse({"code": 0})

    return JsonResponse({"code": 1, "hum_data": hum_data, "temp_data": temp_data})

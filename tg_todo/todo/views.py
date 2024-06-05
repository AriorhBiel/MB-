from django.apps import apps
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import sys
from .models import *
from .serializer import *
from .form import *


def field_verbose(model_):
    model_fields = model_._meta.fields + model_._meta.many_to_many
    titles_ = {f.name: f.verbose_name for f in model_fields}
    relation_titles_ = [i.name for i in model_fields if i.is_relation]
    table_ = model_._meta.verbose_name_plural
    return table_, titles_, relation_titles_


def index(request):
    return render(request, 'index.html')


tableDict = {'user': 'User', 'record': 'Record', 'date': 'Date'}


@csrf_exempt
def note(request, slug=''):
    for key in tableDict:
        if slug == key:
            slug_name = tableDict[key]
            break

    # slug_name = slug.capitalize() + 's'
    print(slug)

    try:
        model = getattr(sys.modules[__name__], slug_name + "Serializer2")
    except:
        return HttpResponse('<h1>Такой таблицы нет</h1>', status=403)

    table = apps.get_model(app_label='todo', model_name=slug_name)

    if request.method == 'GET':
        table_name, titles, relation_titles = field_verbose(table)
        data = (table.objects.all().order_by('id').prefetch_related(*relation_titles))
        serialized_data = model(data, many=True).data
        form = getattr(sys.modules[__name__], slug_name + 'Form')        

        #print(serialized_data)

        return render(request, 'table_base.html', {'tb_name': table_name, 'table':serialized_data, 'title': titles, 'form': form()})
        #return JsonResponse(serialized_data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        ser = model(data=data)
        print(ser.is_valid())
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201)
        else:
            print(ser.errors)
            return HttpResponse('<h1>Неверные данные</h1>', status=400)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        if 'id' not in data.keys():
            return HttpResponse('Method Not Allowed', status=400)
        instance = table.objects.filter(pk=data["id"])
        if len(instance) < 1:
            return HttpResponse('put', status=400)
        instance = instance[0]

        ser = model(data=data, instance=instance)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201)
        else:
            print(ser.errors)
            return HttpResponse('<h1>Неверные данные</h1>', status=400)

    elif request.method == "DELETE":
        data = JSONParser().parse(request)
        if 'id' not in data.keys():
            return HttpResponse('Method Not Allowed', status=400)

        instance = table.objects.filter(id=data["id"])
        if len(instance) < 1:
            return HttpResponse('delete', status=400)

        instance.delete()
        return JsonResponse(data, status=201)
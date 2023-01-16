from django.views import View
from .models import Store,State,Country,City
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

class StoreView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)
    def get(self,request,id=0):

        if id>0:
            stores = list(Store.objects.filter(id=id).values())
            if len(stores)>0:
                data = {'message':"Success",'store':stores[0]}
            else:
                data = {'message':"Store not found"}
            return JsonResponse(data)
        else:
            stores = list(Store.objects.values())
            if len(stores)>0:
                data = {'message':"Success",'stores':stores}
            else:
                data = {'message':"Stores not found"}
            return JsonResponse(data)

    def post(self,request):
        jd =json.loads(request.body)
        Store.objects.create(name=jd['name'],code=jd['code'])
        data = {'message':"Success"}

        return JsonResponse(data)

    def put(self,request,id):
        jd =json.loads(request.body)
        stores = list(Store.objects.filter(id=id).values())
        if len(stores)>0:
            store=Store.objects.get(id=id)
            store.name= jd['name']
            store.code= jd['code']
            store.save()
            data = {'message':"Success"}
        else:
            data = {'message':"Store not found"}
        return JsonResponse(data)

    def delete(self,request,id):
        stores = list(Store.objects.filter(id=id).values())
        if len(stores)>0:
            store=Store.objects.filter(id=id).delete()
            data = {'message':"Success"}
        else:
            data = {'message':"Store not found"}
        return JsonResponse(data)


class CountryView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)
    def get(self,request,id=0):

        if id>0:
            countrys = list(Country.objects.filter(id=id).values())
            if len(countrys)>0:
                data = {'message':"Success",'country':countrys[0]}
            else:
                data = {'message':"Country not found"}
            return JsonResponse(data)
        else:
            countrys = list(Country.objects.values())
            if len(countrys)>0:
                data = {'message':"Success",'countrys':countrys}
            else:
                data = {'message':"Countrys not found"}
            return JsonResponse(data)

    def post(self,request):
        jd =json.loads(request.body)
        try:
            Country.objects.create(name=jd['name'],code=jd['code'])
            data = {'message':"Success"}
        except Exception as e:
            data={'message':"an error occurred while saving the record"}

        return JsonResponse(data)

    def put(self,request,id):
        jd =json.loads(request.body)
        countrys = list(Country.objects.filter(id=id).values())
        if len(countrys)>0:
            countrys=Country.objects.get(id=id)
            countrys.name= jd['name']
            countrys.code= jd['code']
            countrys.save()
            data = {'message':"Success"}
        else:
            data = {'message':"Country not found"}
        return JsonResponse(data)

    def delete(self,request,id):
        countrys = list(Country.objects.filter(id=id).values())
        if len(countrys)>0:
            country=Country.objects.filter(id=id).delete()
            data = {'message':"Success"}
        else:
            data = {'message':"State not found"}
        return JsonResponse(data)

class CityforStateView(View):


    def get(self,request,id=0):
        citys = list(City.objects.filter(state=id).values())
        if len(citys)>0:
            data = {'message':"Success",'country':citys}
        else:
            data = {'message':"Countrys not found for State"+ str(id)}
        return JsonResponse(data)
        


class StateView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)
    def get(self,request,id=0):

        if id>0:
            states = list(State.objects.filter(id=id).values())
            if len(states)>0:
                data = {'message':"Success",'state':states[0]}
            else:
                data = {'message':"State not found"}
            return JsonResponse(data)
        else:
            states = list(State.objects.values())
            if len(states)>0:
                data = {'message':"Success",'states':states}
            else:
                data = {'message':"States not found"}
            return JsonResponse(data)

    def post(self,request):
        jd =json.loads(request.body)
        try:
            country = Country.objects.filter(id=jd['country'])
            State.objects.create(name=jd['name'],code=jd['code'],country=country[0])
            data = {'message':"Success"}
        except Exception as e:
            data={'message':"an error occurred while saving the record"}

        return JsonResponse(data)

    def put(self,request,id):
        jd =json.loads(request.body)
        states = list(State.objects.filter(id=id).values())
        country = Country.objects.filter(id=jd['country'])

        if len(states)>0:
            states=State.objects.get(id=id)
            states.name= jd['name']
            states.code= jd['code']
            states.country=country[0]
            states.save()
            data = {'message':"Success"}
        else:
            data = {'message':"State not found"}
        return JsonResponse(data)

    def delete(self,request,id):
        states = list(State.objects.filter(id=id).values())
        if len(states)>0:
            store=State.objects.filter(id=id).delete()
            data = {'message':"Success"}
        else:
            data = {'message':"State not found"}
        return JsonResponse(data)

class CityView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)
    def get(self,request,id=0):

        if id>0:
            citys = list(City.objects.filter(id=id).values())
            if len(citys)>0:
                data = {'message':"Success",'City':citys[0]}
            else:
                data = {'message':"City not found"}
            return JsonResponse(data)
        else:
            citys = list(City.objects.values())
            if len(citys)>0:
                data = {'message':"Success",'Citys':citys}
            else:
                data = {'message':"Citys not found"}
            return JsonResponse(data)

    def post(self,request):
        jd =json.loads(request.body)
        try:
            state = State.objects.filter(id= jd['state'])
            City.objects.create(name=jd['name'],code=jd['code'],state=state[0])
            data = {'message':"Success"}
        except Exception as e:
            data={'message':"an error occurred while saving the record"}

        return JsonResponse(data)

    def put(self,request,id):
        jd =json.loads(request.body)
        citys = list(City.objects.filter(id=id).values())
        if len(citys)>0:
            state = State.objects.filter(id= jd['state'])
            citys=City.objects.get(id=id)
            citys.name= jd['name']
            citys.code= jd['code']
            citys.state=state[0]
            citys.save()
            data = {'message':"Success"}
        else:
            data = {'message':"City not found"}
        return JsonResponse(data)

    def delete(self,request,id):
        citys = list(City.objects.filter(id=id).values())
        if len(citys)>0:
            city=City.objects.filter(id=id).delete()
            data = {'message':"Success"}
        else:
            data = {'message':"City not found"}
        return JsonResponse(data)
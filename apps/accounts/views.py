from django.views import View
from .models import Client
from apps.store.models import State,Store,City,Country
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.


class ClientView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)
    def get(self,request,id=0):

        if id>0:
            clients = list(Client.objects.filter(id=id).values())
            if len(clients)>0:
                data = {'message':"Success",'client':clients[0]}
            else:
                data = {'message':"Client not found"}
            return JsonResponse(data)
        else:
            clients = list(Client.objects.values())
            if len(clients)>0:
                data = {'message':"Success",'clients':clients}
            else:
                data = {'message':"Clients not found"}
            return JsonResponse(data)

    def post(self,request):
        jd =json.loads(request.body)
        try:
            country = Country.objects.filter(id=jd['country'])
            state = State.objects.filter(id=jd['state'])
            city = City.objects.filter(id=jd['city'])
            store = Store.objects.filter(id=jd['favorite_store'])
            Client.objects.create(name=jd['name'],surname=jd['surname'],country=country[0],state=state[0],city=city[0],favorite_store=store[0])
            data = {'message':"Success"}
        except Exception as e:
            data={'message':"an error occurred while saving the record"}

        return JsonResponse(data)

    def put(self,request,id):
        jd =json.loads(request.body)
        clients = list(Client.objects.filter(id=id).values())
        country = Country.objects.filter(id=jd['country'])
        state = State.objects.filter(id=jd['state'])
        city = City.objects.filter(id=jd['city'])
        store = Store.objects.filter(id=jd['favorite_store'])

        if len(clients)>0:
            clients=Client.objects.get(id=id)
            clients.name= jd['name']
            clients.surname= jd['surname']
            clients.country=country[0]
            clients.state=state[0]
            clients.city=city[0]
            clients.favorite_store=store[0]
            clients.save()
            data = {'message':"Success"}
        else:
            data = {'message':"client not found"}
        return JsonResponse(data)

    def delete(self,request,id):
        clients = list(Client.objects.filter(id=id).values())
        if len(clients)>0:
            client=Client.objects.filter(id=id).delete()
            data = {'message':"Success"}
        else:
            data = {'message':"client not found"}
        return JsonResponse(data)
    
    def get_for_state(self,request,id=0):

        if id>0:
            clients = list(Client.objects.filter(id=id).values())
            if len(clients)>0:
                data = {'message':"Success",'client':clients[0]}
            else:
                data = {'message':"Client not found"}
            return JsonResponse(data)
        else:
            clients = list(Client.objects.values())
            if len(clients)>0:
                data = {'message':"Success",'clients':clients}
            else:
                data = {'message':"Clients not found"}
            return JsonResponse(data)


class ClientForStoreView(View):

    def get(self,request,id=0):

        clients = list(Client.objects.filter(favorite_store=id).values())
        if len(clients)>0:
            data = {'message':"Success",'client':clients}
        else:
            data = {'message':"Clients not found for Store : "+ str(id) }
        return JsonResponse(data)
        

class ClientViewState(View):

    def get(self,request,id=0):

        clients = list(Client.objects.filter(state=id).values())
        if len(clients)>0:
            data = {'message':"Success",'client':clients}
        else:
            data = {'message':"Clients not found for State : "+ str(id) }
        return JsonResponse(data)
        

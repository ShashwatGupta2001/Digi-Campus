from django.shortcuts import render, redirect
from .models import messMain, messOrder,messExtras
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import messOrderSerializer,messExtrasSerializer,messMainSerializer
from django.contrib.auth.decorators import login_required
from Login.models import Profile

# Create your views here

@login_required
def mess_view(request,*args,**kwargs):
    element=messExtras.objects.get(id=1)
    context={'BDMR':'50',
    'Extras_1':element.extras_1,
    'Extras_2':element.extras_2,
    'Extras_3':element.extras_3,
    'Extras_4':element.extras_4,
    'Extras_5':element.extras_5,
    'Extras_6':element.extras_6,
    'price_1':element.price_1,
    'price_2':element.price_2,
    'price_3':element.price_3,
    'price_4':element.price_4,
    'price_5':element.price_5,
    'price_6':element.price_6,
    }
    return render(request,"mess.html",context)

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/task-list/'
    }
    return Response(api_urls)

@api_view(['GET'])
def orderlist(request):
    orders = messOrder.objects.all()
    serializer = messOrderSerializer(orders, many=True)
    return Response(serializer.data) 

@api_view(['GET'])
def orderDetail(request,pk):
    orders = messOrder.objects.get(id=pk)
    serializer = messOrderSerializer(orders, many=False)
    return Response(serializer.data) 

@api_view(['POST'])
def orderCreate(request):
    serializer = messOrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        obj = Profile.objects.get(roll_no=serializer.data['rollno'])
        obj.expense_current = obj.expense_current+serializer.data['total']
        obj.expense_total = obj.expense_total+serializer.data['total']
        obj.order_id = serializer.data['id']
        print(serializer.data['total'])
        obj.save()
        #object.expense_total = object.expense_total+serializer.data['total']
        return Response(serializer.data) 
    else:
        return Response("ankurs mom")
    

@api_view(['DELETE'])
def orderDelete(request,pk):
    order = messOrder.objects.get(id=pk)
    order.delete()
    return Response('mom')

def manager_view(request,*args,**kwargs):
    return render(request,'manager.html')

def confirm_view(request):
    object=messOrder.objects.get(id=request.user.profile.order_id)
    context={
            'Selected_1' : object.item_1,
            'Selected_2' : object.item_2,
            'Selected_3' : object.item_3,
            'Selected_4' : object.item_4,
            'Selected_5' : object.item_5,
            'Selected_6' : object.item_6,
            'Quantity_1':object.quantity_1,
            'Quantity_2':object.quantity_2,
            'Quantity_3':object.quantity_3,
            'Quantity_4':object.quantity_4,
            'Quantity_5':object.quantity_5,
            'Quantity_6':object.quantity_6,
            'Price_1':object.price_1,
            'Price_2':object.price_2,
            'Price_3':object.price_3,
            'Price_4':object.price_4,
            'Price_5':object.price_5,
            'Price_6':object.price_6,

        }
    return render(request,'new_confirm.html',context)

def cancel_view(request):
    object=messOrder.objects.get(id=request.user.profile.order_id)
    object.delete()
    request.user.profile.order_id=0
    request.user.profile.save()
    return redirect ('../')
    

# def confirm_view(request):
#     from django.http import JsonResponse
#     if request.method=='POST' and request.is_ajax():
#         try:
#            request.user.messOrder.price_1=80

            
   
#         except messOrder.DoesNotExist:
#             return JsonResponse({'status':'Fail'})

#     else:
#         return JsonResponse({'status':'Fail'})

def hash_view(request,*args,**kwargs):
    return redirect('../../dashboard/')    


@api_view(['GET'])
def main_menu_list(request):
    orders = messMain.objects.all().order_by('-id')
    serializer = messMainSerializer(orders, many=True)
    return Response(serializer.data) 


@api_view(['GET'])
def main_menu_detail(request,pk):
    orders = messMain.objects.get(id=pk)
    serializer = messMainSerializer(orders, many=False)
    return Response(serializer.data) 

@api_view(['POST'])
def main_menu_create(request):
    serializer = messMainSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        #object.expense_total = object.expense_total+serializer.data['total']
        return Response(serializer.data) 
    else:
        return Response("ankurs mom")



@api_view(['DELETE'])
def main_menu_delete(request,pk):
    order = messMain.objects.get(id=pk)
    order.delete()
    return Response('mom')



@api_view(['GET'])
def main_extras_list(request):
    orders = messExtras.objects.all().order_by('-id')
    serializer = messExtrasSerializer(orders, many=True)
    return Response(serializer.data) 


@api_view(['GET'])
def main_extras_detail(request,pk):
    orders = messExtras.objects.get(id=pk)
    serializer = messExtrasSerializer(orders, many=False)
    return Response(serializer.data) 

@api_view(['POST'])
def main_extras_create(request):
    serializer = messExtrasSerializer(data=request.data)
    print(serializer.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data) 
    else:
        return Response("ankurs mom")



@api_view(['DELETE'])
def main_extras_delete(request,pk):
    order = messExtras.objects.get(id=pk)
    order.delete()
    return Response('mom')



import json
from django.shortcuts import render, redirect
from django.http import JsonResponse

from ui.models.menu import Category, Menu
from ui.serializers.menu import CategorySerializer, MenuSerializer
from ui.utils.common import *


def main_page(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "menu.html")


def read_menu(request):
    category = request.GET.get('category')
    if category:
        menus = MenuSerializer(Menu.objects.filter(category_id=category),
                               many=True)
    else:
        menus = MenuSerializer(Menu.objects.all(), many=True)
    return JsonResponse(menus.data, safe=False)


def read_categories(request):
    categories = CategorySerializer(Category.objects.all(), many=True)
    return JsonResponse(categories.data, safe=False)


def save_menu(request):
    if request.method == "POST":
        menu_data = get_post_data(request)

        if menu_data.get("id"):
            instance = Menu.objects.get(id=menu_data.get("id"))
            serializer = MenuSerializer(instance, data=menu_data)
        else:
            serializer = MenuSerializer(data=menu_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Menu saved successfully"})
        else:
            return JsonResponse({"message": "Menu not saved"}, status=400)
    else:
        return JsonResponse({"message": "Invalid request"})


def save_category(request):
    if request.method == "POST":
        data = request.POST.dict()
        data = eval(data)

        if data.get("id"):
            instance = Category.objects.get(id=data.get("id"))
            serializer = CategorySerializer(instance, data=data)
        else:
            serializer = CategorySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Category saved successfully"})
        else:
            return JsonResponse({"message": "Category not saved"})
    else:
        return JsonResponse({"message": "Invalid request"})


def delete_menu(request):
    if request.method == "POST":
        data = get_post_data(request)
        instance = Menu.objects.filter(id=data.get("id")).last()
        print("Instance: ", instance)

        if instance:
            print("DELETEDD")
            instance.delete()

        return JsonResponse({"message": "Menu deleted successfully"})
    else:
        return JsonResponse({"message": "Invalid request"})


def delete_category(request):
    if request.method == "POST":
        id = request.POST.get("id")
        instance = Category.objects.filter(id=id).last()

        if instance:
            instance.delete()

        return JsonResponse({"message": "Category deleted successfully"})
    else:
        return JsonResponse({"message": "Invalid request"})

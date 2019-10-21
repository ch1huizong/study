from django.shortcuts import render

from .models import OperatingSystem, Service, HardwareComponent, Server


def main(request):
    os_list = OperatingSystem.objects.all()
    svc_list = Service.objects.all()
    hardware_list = HardwareComponent.objects.all()
    return render(
        request,
        "inventory/main.html",
        {"os_list": os_list, "svc_list": svc_list, "hardware_list": hardware_list},
    )


def categorized(request, category, category_id):
    category_dict = {"os": "Operating System", "svc": "Service", "hw": "Hardware"}

    if category == "os":
        server_list = Server.objects.filter(os__exact=category_id)
        category_name = OperatingSystem.objects.get(id=category_id)

    elif category == "svc":
        server_list = Server.objects.filter(services__exact=category_id)  # 好吗
        category_name = Service.objects.get(id=category_id)  # 详细情况

    elif category == "hw":
        server_list = Server.objects.filter(hardware_component__exact=category_id)
        category_name = HardwareComponent.objects.get(id=category_id)

    else:
        server_list = []
    return render(
        request,
        "inventory/categoried.html",
        {
            "server_list": server_list,
            "category": category_dict[category],  # 分类概览
            "category_name": category_name,  # 详情
        },
    )


def server_detail(request, server_id):
    server = Server.objects.get(id=server_id)
    return render(request, "inventory/server_detail.html", {"server": server})

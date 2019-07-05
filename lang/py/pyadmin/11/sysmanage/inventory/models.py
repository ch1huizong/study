from django.db import models


class OperatingSystem(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class HardwareComponent(models.Model):
    manufacturer = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    model = models.CharField(max_length=50, blank=True, null=True)
    vendor_part_number = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.manufacturer


class Server(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    os = models.ForeignKey(OperatingSystem, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)
    hardware_component = models.ManyToManyField(HardwareComponent)

    def __str__(self):
        return self.name


class IPAddress(models.Model):
    # address = models.TextField(blank=True, null=True)
    address = models.GenericIPAddressField(blank=True, null=True)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)

    def __str__(self):
        return self.address

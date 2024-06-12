from django.db import models

# Create your models here.

class Fabric(models.Model):
    FabricID = models.AutoField(primary_key=True)
    FabricName = models.CharField(max_length=255)
    FabricType = models.CharField(max_length=255)
    ImageLink = models.CharField(max_length=2048)

    def __str__(self):
        return self.FabricName

class Fvendor(models.Model):
    VendorID = models.AutoField(primary_key=True)
    VendorName = models.CharField(max_length=255)
    VendorMail = models.CharField(max_length=400, null=True, blank=True)
    Phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.VendorName

class Inventory(models.Model):
    FabricID = models.OneToOneField(Fabric, on_delete=models.CASCADE, primary_key=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Swatch = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.FabricID)

class F_V(models.Model):
    FabricID = models.ForeignKey(Fabric, on_delete=models.CASCADE)
    VendorID = models.ForeignKey(Fvendor, on_delete=models.CASCADE)
    DeliveryLeadTime = models.IntegerField()
    MaxQuantity = models.IntegerField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    ValidFrom = models.DateField()
    ValidTill = models.DateField()

    class Meta:
        unique_together = (('FabricID', 'VendorID'),)

    def __str__(self):
        return f"{self.FabricID} - {self.VendorID}"

class Saleprice(models.Model):
    FabricID = models.ForeignKey(Fabric, on_delete=models.CASCADE)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    ValidFrom = models.DateField()
    ValidTill = models.DateField()

    class Meta:
        unique_together = (('FabricID', 'ValidFrom', 'ValidTill'),)

    def __str__(self):
        return f"{self.FabricID} - {self.ValidFrom} - {self.ValidTill}"
from django.db import models

# Create your models here.
class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone=models.IntegerField(null=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"
  


class Fashion(models.Model):
    ProductId = models.IntegerField(primary_key=True)
    Gender = models.CharField(max_length=10)
    Category = models.CharField(max_length=50)
    SubCategory = models.CharField(max_length=50, db_column='SubCategory')
    ProductType = models.CharField(max_length=50, db_column='ProductType')
    Colour = models.CharField(max_length=20)
    Usage = models.CharField(max_length=20, db_column='Usage')
    ProductTitle = models.CharField(max_length=100, db_column='ProductTitle')
    Image = models.CharField(max_length=50)
    ImageUrl = models.CharField(max_length=200, db_column='ImageURL')

    class Meta:
        managed = False  # Tell Django not to create or modify this table
        db_table = 'fashion'  # Specify the name of the existing table

    def __str__(self):
        return self.product_title


##Software from here


class Fabric(models.Model):
    FabricID = models.AutoField(primary_key=True)
    FabricName = models.CharField(max_length=255)
    FabricType = models.CharField(max_length=255)
    ImageLink = models.CharField(max_length=2048)

    # class Meta:
    #     managed = False  # Tell Django not to create or modify this table
    #     db_table = 'Fabric'

    def __str__(self):
        return self.FabricName

class Fvendor(models.Model):
    VendorID = models.AutoField(primary_key=True)
    VendorName = models.CharField(max_length=255)
    VendorMail = models.CharField(max_length=400, null=True, blank=True)
    Phone = models.CharField(max_length=20, null=True, blank=True)

    # class Meta:
    #     managed = False  # Tell Django not to create or modify this table
    #     db_table = 'Fvendor'

    def __str__(self):
        return self.VendorName

class Inventory(models.Model):
    FabricID = models.OneToOneField(Fabric, on_delete=models.CASCADE, primary_key=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Swatch = models.IntegerField(null=True, blank=True)

    # class Meta:
    #     managed = False  # Tell Django not to create or modify this table
    #     db_table = 'Inventory'

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
       
        # managed = False  # Tell Django not to create or modify this table
        # db_table = 'F_V'
        unique_together = (('FabricID', 'VendorID'),)

    

    def __str__(self):
        return f"{self.FabricID} - {self.VendorID}"

class Saleprice(models.Model):
    FabricID = models.ForeignKey(Fabric, on_delete=models.CASCADE)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    ValidFrom = models.DateField()
    ValidTill = models.DateField()

    class Meta:
        
        # managed = False  # Tell Django not to create or modify this table
        # db_table = 'SalePrice'
        unique_together = (('FabricID', 'ValidFrom', 'ValidTill'),)


    def __str__(self):
        return f"{self.FabricID} - {self.ValidFrom} - {self.ValidTill}"



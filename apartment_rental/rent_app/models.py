from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract =True

class Landlord(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name

class Apartment(BaseModel):
    address = models.CharField(max_length=150, null=True, blank=True)
    num_rooms = models.IntegerField(null=True, blank=True)
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    #Relationship
    landlord = models.ForeignKey(Landlord, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Apartment at {self.address}"

class Tenant(BaseModel):
    name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name
    
class RentalContract(BaseModel):
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # Relationship
    apartment = models.ForeignKey(Apartment, blank=True, null=True, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Contract {self.tenant.name} for {self.apartment.address}"
    
class MaintenanceRequest(BaseModel):
    description = models.TextField(blank=True, null=True)
    request_date = models.DateField(blank=True, null=True)
    is_resolved = models.BooleanField(default=False)

    apartment = models.ForeignKey(Apartment, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Request maintenance for {self.apartment.address}"
    
class Image(BaseModel):
    image = models.ImageField(upload_to='apartment_images', null=True, blank=True)

    apartment = models.ForeignKey(Apartment, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Image: {self.apartment.address}"

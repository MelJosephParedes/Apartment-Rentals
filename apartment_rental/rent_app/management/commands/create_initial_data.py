from django.core.management.base import BaseCommand
from rent_app.models import Landlord, Apartment, Tenant, RentalContract, MaintenanceRequest, Image
from django.core.files import File
from django.utils.crypto import get_random_string
from django.core.files.images import ImageFile
import os


class Command(BaseCommand):
    help = 'Creates initial data for the apartment rental system'

    def handle(self, *args, **options):
        landlord1 = Landlord.objects.create(name='Joemar Yson', email='yson123@gmail.com', phone='123-456-1111')
        landlord2 = Landlord.objects.create(name='Cherry Blessing', email='blessing@gmail.com', phone='09123456789')

        apartment1 = Apartment.objects.create(address='111 Zone 4', num_rooms=2, monthly_rent=2000, landlord=landlord1)
        apartment2 = Apartment.objects.create(address='222 Zone 3', num_rooms=3, monthly_rent=2500, landlord=landlord2)

        tenant1 = Tenant.objects.create(name='Carl Johnson', email='carl@gmail.com', phone='000-000-222')
        tenant2 = Tenant.objects.create(name='Snopp Dog', email='snopp@gmail.com', phone='000-000-333')

        rental_contract1 = RentalContract.objects.create(start_date='2023-05-01', end_date='2023-11-30', monthly_rent=2000, apartment=apartment1, tenant=tenant1)
        rental_contract2 = RentalContract.objects.create(start_date='2023-06-01', end_date='2023-12-30', monthly_rent=2500, apartment=apartment2, tenant=tenant2)

        maintenance_request1 = MaintenanceRequest.objects.create(description='Broken Window', request_date='2023-08-20', apartment=apartment1)
        maintenance_request2 = MaintenanceRequest.objects.create(description='Broken AC', request_date='2023-09-10', apartment=apartment2)

        image_path1 = r'C:\Users\meljo\Downloads\apartment1.jpg'
        image_path2 = r'C:\Users\meljo\Downloads\apartment2.png'

        create_image(image_path1, apartment1)
        create_image(image_path2, apartment2)

        self.stdout.write(self.style.SUCCESS('Initial data created successfully.'))

def create_image(image_path, apartment):
    with open(image_path, 'rb') as image_file:
        original_file_name = os.path.basename(image_path)
        image = Image.objects.create(apartment=apartment)
        image.image.save(original_file_name, ImageFile(image_file))
    return image
    
        


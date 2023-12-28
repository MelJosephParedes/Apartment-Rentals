from django.core.management.base import BaseCommand
from rent_app.models import Landlord, Apartment, Tenant, RentalContract, MaintenanceRequest, Image
from django.core.files.images import ImageFile
from django.utils.crypto import get_random_string
import tempfile
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

        image1 = create_image()
        image2 = create_image()

        Image.objects.create(image=image1, apartment=apartment1)
        Image.objects.create(image=image2, apartment=apartment2)

        self.stdout.write(self.style.SUCCESS('Initial data created successfully.'))

def create_image():

    image_content = get_random_string(1024).encode('utf-8')
    _, temp_file_path =tempfile.mkstemp(suffix=".png", dir=tempfile.gettempdir())

    with open(temp_file_path, 'wb') as temp_file:
        temp_file.write(image_content)

    return ImageFile(open(temp_file_path, 'rb'), name=os.path.basename(temp_file_path))
        


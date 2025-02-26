# Admin@123 ///
from django.db import models

class UploadedFile(models.Model):
    pdf_file = models.FileField(upload_to='uploads/')
    excel_file = models.FileField(upload_to='outputs/', blank=True, null=True)








 
from django.db import models

# Create your models here.
class ProductDetail(models.Model):
    name=models.CharField(max_length=225)
    weight=models.IntegerField()
    price=models.IntegerField()
    created_at=models.DateTimeField(blank=True, null=True)
    updated_at=models.DateTimeField(blank=True, null=True)


    def pub_date_pretty1(self):
        return self.created_at.strftime('%b %e %y')

    def pub_date_pretty2(self):
        return self.updated_at.strftime('%b %e %y')

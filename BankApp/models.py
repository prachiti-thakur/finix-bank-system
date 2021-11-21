from django.db import models

# Create your models here.
class Customer(models.Model):
    mail_id=models.EmailField(max_length = 254)
    amount=models.FloatField(default=500)
    
    class meta:
        db_table="Customer"
        
class Transaction_history(models.Model):
    sender=models.IntegerField()
    receiver=models.IntegerField()
    amount=models.FloatField(default=0)
    dnt=models.DateTimeField(editable=False)
    
    class meta:
        db_table="Transaction_history"    
from django.db import models
from customers.models import Customers
import uuid

class Transfer(models.Model):
    transferee = models.ForeignKey(Customers, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    transfered_amt = models.DecimalField(max_digits=200, decimal_places=2)

    def __str__(self) -> str:
        return str(self.transfered_amt)

from django.db import models

# Create your models here
class Portfolio(models.Model):
    pid = models.AutoField(primary_key=True)  # Explicitly defining an auto-incrementing integer primary key
    uid = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    total_value = models.DecimalField(max_digits=10, decimal_places=4)
    invested_value = models.DecimalField(max_digits=10, decimal_places=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.uid}'s Portfolio"


class PortfolioItem(models.Model):
    itemid = models.AutoField(primary_key=True)  # Explicitly defining an auto-incrementing integer primary key
    pid = models.ForeignKey('Portfolio', on_delete=models.CASCADE)
    ticker = models.CharField(max_length=10)
    quantity = models.DecimalField(max_digits=10, decimal_places=4)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ticker} in {self.pid}"
    

class Transaction(models.Model):
    tid = models.AutoField(primary_key=True)  # Explicitly defining an auto-incrementing integer primary key
    pid = models.ForeignKey('Portfolio', on_delete=models.CASCADE)
    ticker = models.CharField(max_length=10)
    quantity = models.DecimalField(max_digits=10, decimal_places=4)
    price = models.DecimalField(max_digits=10, decimal_places=4)
    transaction_date = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.action} {self.quantity} {self.ticker} in {self.pid}"
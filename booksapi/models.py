from django.db import models

# Create your models here.



class Books(models.Model):
    book_name = models.CharField(max_length=100, null=False, blank=False)
    book_quantity = models.IntegerField()
    book_gener = models.TextField()
    is_best_seller = models.CharField(max_length=100, null=False, blank=False)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.book_name
        
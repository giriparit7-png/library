from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    B_id=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=100)
    author=models.CharField()
    pages=models.IntegerField()
    status=models.BooleanField(default=True)

from django.contrib.auth.models import User

class BorrowedBook(models.Model):
    borrow_id = models.AutoField(primary_key=True)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    book = models.ForeignKey(
        'Book',
        on_delete=models.CASCADE
    )

    borrow_date = models.DateField(auto_now_add=True)

    due_date = models.DateField(null=True, blank=True)

    return_date = models.DateField(null=True, blank=True)

    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.book.Name}"

import uuid
from io import BytesIO

import qrcode
from PIL import Image, ImageDraw
from django.contrib.contenttypes.models import ContentType
from django.core.files import File
from django.db import models
from authentication.models import User


# Create your models here.

class Tickets(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cart = models.TextField(blank=True)
    buying_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    qr_code = models.ImageField(upload_to='qr_codes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sport_choice = models.CharField(max_length=250, blank=True)

    class Meta:
        abstract = True


    def save(self, *args, **kwargs):
        user_id = ContentType.objects.get(app_label='authentication', model='user')
        user_id = user_id.get_object_for_this_type(id=self.user.id)
        qrcode_img = qrcode.make(str(self.pk) + str(user_id.id))
        canvas = Image.new('RGB', (350, 350), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f"qr_code-{self.first_name}-{self.id}.png"
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)


class Solo(Tickets):
    pass


class Duo(Tickets):
    pass


class Famille(Tickets):
    pass


class CreditCardHolder(models.Model):
    holder_name = models.CharField(max_length=100)
    card_number = models.DecimalField(max_digits=16, decimal_places=0)
    card_validation_code = models.DecimalField(max_digits=3, decimal_places=0)
    card_validity = models.DateField()
    bought = models.BooleanField(default=True)
    buying_date = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(default=0, decimal_places=3, max_digits=6, blank=True, null=True)

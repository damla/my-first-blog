from django.db import models
from django.utils import timezone
# veritabani burada

class Post(models.Model): #veritabani modeli modelsten anlasiliyor
    yazar = models.ForeignKey('auth.User') #auth olan djangonun kendi user modeli// bir yazarin birden fazla makalesi olursa foreignkey , userda(yazar) primarykey oluyor
    baslik=models.CharField(max_length=200)
    yazi=models.TextField()
    yaratilma_tarihi= models.DateTimeField(default=timezone.now)
    yayinlanma_tarihi=models.DateTimeField(blank=True, null=True) #null bostan farklidir, olmayan bir obje, bos string tirnak icinde hicbirsey olmamasi gibi

    def yayinla(self): #classin icinde dikkat et!
        self.yayinlanma_tarihi = timezone.now()
        self.save() #veritabanina kaydediyor

    def __str__(self):
    return self.baslik #toString basligi sayfada gosteriyor
#silersen post objects yazar kendi iskeletinden

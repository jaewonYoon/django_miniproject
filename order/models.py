from django.db import models

# Create your models here.
class Order(models.Model):
    #ondelete 속성 값, 외래키 삭제될때 어떻게 삭제될건지 적는다.
    fcuser = models.ForeignKey('fcuser.Fcuser', on_delete=models.CASCADE, verbose_name='사용자')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name="상품")
    quantity = models.IntegerField(verbose_name='수량')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name ="등록날짜")
    
    class Meta:
        db_table = 'fastcampus_order'
        verbose_name ='주문'
        verbose_name_plural='주문'
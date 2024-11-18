import uuid

from django.db import models


# Create your models here.

class Media(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Ngày khởi tạo")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")
    is_active = models.BooleanField(default=True, verbose_name="Hoạt động",
                                    help_text="Chỉ định xem đối tượng này còn được coi là đang hoạt động. Bạn nên bỏ chọn này thay vì xóa đối tượng.")
    file = models.FileField(upload_to="media/%Y/%m/%d")

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()

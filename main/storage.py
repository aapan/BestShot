from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os, time, random
from django.http import HttpResponse


class ImageStorage(FileSystemStorage):

    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
        # 初始化
        super(ImageStorage, self).__init__(location, base_url)

    # 重写 _save方法
    def _save(self, name, content):
        # ext 為圖片副檔名
        ext = os.path.splitext(name)[1]
        # 文件目录
        doc = os.path.dirname(name)
        # 定义文件名，年月日时分秒随机数
        filename = time.strftime('%Y%m%d%H%M%S') + str(random.randint(10, 99))
        # 重写合成文件名
        name = os.path.join(doc, filename + ext)
        # 调用父类方法
        return super(ImageStorage, self)._save(name, content)


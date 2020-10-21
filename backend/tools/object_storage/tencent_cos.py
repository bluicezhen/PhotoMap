from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

from backend.settings import TENCENT_COS_REGION, TENCENT_SECRET_ID, TENCENT_SECRET_KEY

config = CosConfig(Region=TENCENT_COS_REGION, SecretId=TENCENT_SECRET_ID, SecretKey=TENCENT_SECRET_KEY)

client = CosS3Client(config)

x = client.list_buckets()
print(x)
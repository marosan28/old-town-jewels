import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "old-town-jewels.myshop.settings")
os.environ["DATABASE_URL"] = "postgres://rvqyyjhw:vL3wfBVBF16q3tB-WWLP_OpnVSU5JXxx@tai.db.elephantsql.com/rvqyyjhw"
os.environ["SECRET_KEY"] = "4&v-i=#jaiolacfkt$4)&mjnghgvq5vj3o&sx_e1xnpm^7r-cm"
os.environ["CLOUDINARY_URL"] = "cloudinary://522695269739824:oa4_FiNurIBFcShGyu3gXGAEpeM@dd9o1h7oh"
os.environ["BROKER_URL"] = "amqps://wkwlhded:HQKjWXS3rKL4Tw379eB6EkDlqVKshDVh@crow.rmq.cloudamqp.com/wkwlhded"
os.environ["CELERY_RESULT_BACKEND"] = "rpc://wkwlhded:HQKjWXS3rKL4Tw379eB6EkDlqVKshDVh@crow.rmq.cloudamqp.com/wkwlhded"
os.environ['DEVELOPMENT'] = 'True'
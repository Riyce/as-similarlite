# as-similarlite
.env
echo BROKER_URL=... >> .env
echo RESULT_BACKEND=... >> .env


Celery
======

sudo cp -R /home/similar/similar/celery-aws.service /etc/systemd/system/celery_similar.service
sudo systemctl daemon-reload
sudo systemctl start celery_similar
sudo systemctl status celery_similar
sudo systemctl stop celery_similar
sudo systemctl restart celery_similar

# AWS
sudo cp -R /home/similar/similar/celery-aws.service /etc/systemd/system/celery_similar.service
tail -f /home/similar/similar/data/logs/celery-*.log
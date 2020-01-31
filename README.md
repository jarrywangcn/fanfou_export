# fanfou_export

export statuses to css file

## requirements

```
pip install -U -r requirements.txt
```

## in fanfou_export.py

change to your own key&secret&id&password
```
consumer = {'key': 'your_key', 'secret': 'your_secret'}
client = fanfou.XAuth(consumer, 'your_id', 'your_password')

```
## start

```
#enter the package folder
python fanfou_export.py
```
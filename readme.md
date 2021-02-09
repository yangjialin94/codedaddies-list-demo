##Steps(Mac):

```
$ cd ~/Desktop
$ git clone https://github.com/yangjialin94/codedaddies_list.git
$ cd codedaddies_list
$ pipenv shell
$ pip3 install bs4 django requests
$ python3 manage.py migrate
$ python3 manage.py createsuperuser
$ python3 manage.py runserver

Home Page: http://127.0.0.1:8000/
Admin Page: http://127.0.0.1:8000/admin/
```

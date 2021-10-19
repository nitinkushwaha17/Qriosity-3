# Arcane 

### Installation 
- Run ` pip install -r requirements2.txt `
- Create a config.json file following <a href="dummy.json">dummy.json</a>
- Put it inside the Qriosity Folder (one constaining ```settings.py ``` 
- Run `python local.py migrate`


### For running it locally use

```sh
python local.py runserver
```

instead of

```sh
python manage.py runserver
```

### To play the quiz locally 

- Create superuser credentials
```sh
python local.py createsuperuser
```
- login to admin panel (\harrypotter)
- create a player instance (from admin panel)

Now you can play the quiz with the player instance that you created  

- To upgrade anyone to level 2 make the count2 variable in admin panel = 0
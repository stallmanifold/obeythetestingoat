# Provisioning A New Site
=========================

## Required Packages:
```
* nginx
* Python 3.6
* virtualenv + pip
* Git
```

For example, on `Ubuntu`, do the following:
```    
$ sudo add-apt-repository ppa:deadsnakes
$ sudo apt-get install nginx git python3.6 python3.6-venv
```

## Nginx Virtual Host Config
```
* See nginx.template.conf
* Replace SITENAME with, e.g., staging,my-domain.com
```

## Systemd Service
```
* See gunicorn-systemd.template.service
* Replace SITENAME with, e.g., staging.my-domain.com
```

## Folder structure

Assume we have a user account at `/home/username` on the deployment server.
The folder structure may look as follows.

```
$ tree /home/username
/home/username
└── sites
    └── SITENAME
        ├── database
        ├── source
        ├── static
        └── virtualenv
```

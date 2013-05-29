Sample use case of geolocate library
============

Since I've been writing the same code all over the place I might as well make
a barebone version of it public.

This program uses grok framework with pygeoip library while assuming that
package geoip-database is installed on the system.

Pygeoip -- https://pypi.python.org/pypi/pygeoip/
geoip-database -- http://packages.debian.org/sid/geoip-database

This application takes exactly 10 lines to write and way more effort to configure.


Front-facing nginx configuration for grok.

server {

        listen   myip.flamy.ca:80; ## listen for ipv4
        server_name myip.flamy.ca;

        access_log  /var/log/nginx/myip.access.log;
        location /{
                proxy_pass http://127.0.0.1:3456/myiplocate/++vh++http:myip.flamy.ca:80/++;
                proxy_set_header X-Forwarded-For $remote_addr;

        }
}


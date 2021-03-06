In this directory you can find templates which are used by
``zc.buildout`` to create the configuration files in the parts/etc/ subdir
of your project.

If you modify files in this directory, you have to run::

  $ bin/buildout

afterwards to rebuild the configuration files in parts/etc/.

In the templates you can use placesholders recognized by zc.buildout
to name local paths, etc. A zc.buildout placeholder looks like this::

  ${buildout:directory}

which gives you the path of the project directory and will be
substituted with the real path when you run buildout the next
time. The set of available placeholders depends on your
buildout.cfg.

You can also modify files in parts/etc directly, but those changes
will be overwritten after running bin/buildout the next time.

To run your project you can do::

  $ bin/paster serve parts/etc/deploy.ini

###################
Nginx config for setting up X-Forwarded-For headers.

For additional informatio, visit
http://grok.zope.org/documentation/how-to/grok-virtual-hosting-and-nginx


server {

        listen   myip.flamy.ca:80; ## listen for ipv4
        server_name myip.flamy.ca;

        access_log  /var/log/nginx/myip.access.log;
        location /{
                proxy_pass http://127.0.0.1:3456/myiplocate/++vh++http:myip.flamy.ca:80/++;
                proxy_set_header X-Forwarded-For $remote_addr;

        }
}

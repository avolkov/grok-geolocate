import grok
import os.path
import pygeoip

from myiplocate import resource

geolocate_path = '/usr/share/GeoIP/GeoIP.dat'

assert os.path.isfile(geolocate_path)
gi = pygeoip.GeoIP(geolocate_path, pygeoip.MEMORY_CACHE)


class Myiplocate(grok.Application, grok.Container):
    pass

class Index(grok.View):
    def update(self):
        resource.style.need()
        self.remote_ip = self.request.get('HTTP_X_FORWARDED_FOR')
        self.country = gi.country_name_by_addr(self.remote_ip)

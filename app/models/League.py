from google.appengine.ext import ndb
import json

class League(ndb.Model):
    """Models an individual Guestbook entry with author, content, and date."""
    commissioner = ndb.UserProperty()
    name = ndb.StringProperty()

class LeagueEncoder(json.JSONEncoder):
    def default(self, obj):
    	objDictionary = {"commissioner": obj.commissioner.email(), "name": obj.name }
        return objDictionary
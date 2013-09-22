import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb
from League import League
from League import LeagueEncoder
import json

class LeaguesListHandler(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()
		if user:
			leagueQuery = League.query(League.commissioner == user)
			leagues = leagueQuery.fetch()
			print "json=",json.dumps(leagues, cls=LeagueEncoder)
			self.response.write(json.dumps(leagues, cls=LeagueEncoder))
		else:
			self.redirect('/')

	def post(self):
		user = users.get_current_user()
		if user:
			league = League()
			jsonBody = json.loads(self.request.body)
			league.name = jsonBody['name']
			print "name=", jsonBody['name']
			league.commissioner = user
			league.put()
			print "json=",json.dumps(league, cls=LeagueEncoder)
			self.response.write(json.dumps(league, cls=LeagueEncoder))
		else:
			self.redirect('/')



	
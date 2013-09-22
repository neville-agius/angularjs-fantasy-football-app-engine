#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.api import users

import webapp2
import jinja2
import json
import os

import LeagueHandler

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	user = users.get_current_user()
    	if user:
    		userDictionary = {"email": user.email(), "userid": user.user_id()}
    	else:
    		userDictionary = None
        template_values = {
            'user': json.dumps( userDictionary ),
        }

        template = JINJA_ENVIRONMENT.get_template('app/views/index.html')
        self.response.write(template.render(template_values))

class SignoutHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect(users.create_logout_url('/'))

class SigninHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect(users.create_login_url('/'))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/signout', SignoutHandler),
    ('/signin', SigninHandler),
    ('/leagues', LeagueHandler.LeaguesListHandler)
], debug=True)

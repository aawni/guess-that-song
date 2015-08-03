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
import os
import webapp2
import jinja2
from google.appengine.ext import ndb


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# class Song(ndb.Model):
#     source = ndb.StringProperty(required=True)
#     title = ndb.StringProperty(required=True)
#     artist = nbd.StringProperty(required=True)

song_source="Fashion Killa.mp3"
song_title="Fashion Killa"
song_artist="A$AP ROCKIE"

#create an array by genre
#randomize array
#compare user's input to the song name and artist
# so if input = intended name then add to correct answers
# correct = 1
# hip_hop[[  "A$AP Rocky"       ][ "Fashion Killa"     ]]
# if artist_answer && song_answer = hip_hop[0][0]:
#     correct += 1
# else:
#     corect = correct


class QuizHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {"song1_source": song_source}
        template = JINJA_ENVIRONMENT.get_template('templates/quiz.html')
        self.response.write(template.render(template_values))

class ResultsHandler(webapp2.RequestHandler):
    def post(self):
        amount_right=0
        artist_answer= self.request.get("artist")
        song_answer=self.request.get("song_title")
        if (artist_answer==song_artist and song_answer==song_title):
            amount_right+=1

        template_values = {"amount_right": amount_right}
        template = JINJA_ENVIRONMENT.get_template('templates/results.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/quiz', QuizHandler),
    ('/results', ResultsHandler)
], debug=True)

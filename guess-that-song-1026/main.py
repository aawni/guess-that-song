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

class Song(ndb.Model):
    source = ndb.StringProperty(required=True)
    title = ndb.StringProperty(required=True)
    artist = ndb.StringProperty(required=True)

hiphop_songs=[Song(source="songs/hiphop/Fashion_Killa.mp3", title="Fashion Killa", artist="A$AP ROCKY"),
               Song(source="songs/hiphop/Alright.mp3", title="Alright", artist="Kendrick Lamar"),
               Song(source="songs/hiphop/Commas.mp3", title="Commas", artist="Future"),
               Song(source="songs/hiphop/Good_Life.mp3", title="Good Life", artist="Kanye West"),
               Song(source="songs/hiphop/Love_Sosa.mp3", title="Love Sosa", artist="Chief Keef"),
               Song(source="songs/hiphop/Forbidden_Fruit.mp3", title="Forbidden Fruit", artist="Kendrick Lamar"),
               Song(source="songs/hiphop/My_Way.mp3", title="My Way", artist="Fetty Wap"),
               Song(source="songs/hiphop/Planes.mp3", title="Planes", artist="Jeremih"),
               Song(source="songs/hiphop/Versace.mp3", title="Versace", artist="Migos")]
genres={"hiphop":hiphop_songs}


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/setup.html')
        self.response.write(template.render())


class QuizHandler(webapp2.RequestHandler):
    def post(self):
        genre=self.request.get("genre")
        template_values = {"songs":genres[genre],"genre":genre}

        template = JINJA_ENVIRONMENT.get_template('templates/quiz.html')
        self.response.write(template.render(template_values))

class ResultsHandler(webapp2.RequestHandler):
    def post(self):
        amount_right=0
        genre=self.request.get("genre")
        counter=1
        print genres[genre]
        for song in genres[genre]:
            artist_answer=self.request.get("artist"+str(counter)).lower()
            song_answer=self.request.get("song_title"+str(counter)).lower()
            if artist_answer!="" and song_answer!="":
                if artist_answer==genres[genre][counter-1].artist.lower() and song_answer==genres[genre][counter-1].title.lower():
                    amount_right+=1

        template_values = {"amount_right": amount_right}
        template = JINJA_ENVIRONMENT.get_template('templates/results.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/quiz', QuizHandler),
    ('/results', ResultsHandler)
], debug=True)

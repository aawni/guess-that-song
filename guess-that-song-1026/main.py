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
from google.appengine.api import users



JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class UserModel(ndb.Model):
    currentUserID = ndb.StringProperty(required = True)
    questions_correct = ndb.IntegerProperty()
    questions_played = ndb.IntegerProperty()
    is_new_user = ndb.BooleanProperty()


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
               Song(source="songs/hiphop/Planes.mp3", title="Planes", artist="Jeremiah"),
               Song(source="songs/hiphop/Versace.mp3", title="Versace", artist="Migos")]

pop_songs=[Song(source="songs/pop/Bad_Blood.mp3", title="Bad Blood", artist="Taylor Swift"),
            Song(source="songs/pop/Cheerleader.mp3",title="Cheerleader",artist= "Omi"),
            Song(source="songs/pop/Cool_For_The_Summer.mp3",title="Cool for the Summer",artist= "Demi Lovato"),
            Song(source="songs/pop/Diamonds.mp3",title="Diamonds",artist= "Rihanna"),
            Song(source="songs/pop/Flashlight.mp3",title="Flashlight",artist= "Jessie J"),
            Song(source="songs/pop/Fun.mp3",title= "Fun", artist= "Chris Brown"),
            Song(source="songs/pop/Good_For_You.mp3",title="Good For You",artist= "Selena Gomez"),
            Song(source="songs/pop/Shouldve_Been_Us.mp3",title="Should've Been Us",artist= "Tori Kelly"),
            Song(source="songs/pop/Uptown_Funk.mp3",title="Upton Funk",artist= "Bruno Mars"),
            Song(source="songs/pop/Worth_It.mp3",title="Worth It",artist= "Fifth Harmony")

            ]
genres={"hiphop":hiphop_songs, "pop":pop_songs}



class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.response.write(user)
            previous_user_query=UserModel.query().filter(UserModel.currentUserID==user.user_id()).fetch()
            if previous_user_query:
                current_user = previous_user_query[0]
                current_user.is_new_user=False
            else:
                current_user = UserModel(currentUserID = user.user_id(), questions_played=0,questions_correct=0, is_new_user=True)
            current_user.put()
        else:
            self.redirect(users.create_login_url(self.request.uri))

        template_vars={"nickname": user.nickname(),"logout_url":users.create_logout_url('/')}
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
        user=users.get_current_user()
        user.questions_played+=genres[genre]
        user.questions_correct+=amount_right

        template_values = {"amount_right": amount_right}
        template = JINJA_ENVIRONMENT.get_template('templates/results.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/quiz', QuizHandler),
    ('/results', ResultsHandler)
], debug=True)

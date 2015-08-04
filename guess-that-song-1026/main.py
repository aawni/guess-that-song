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
    youtube_ID = ndb.StringProperty(required=True)
    title = ndb.StringProperty(required=True)
    artist = ndb.StringProperty(required=True)

hiphop_songs=[Song(youtube_ID="Z-48u_uWMHY", title="Alright", artist="Kendrick Lamar"),
               Song(youtube_ID="frOjjVDb8R8", title="Commas", artist="Future"),
               Song(youtube_ID="NtTLfSOujTI", title="Planes", artist="Jeremih"),
               Song(youtube_ID="YWyHZNBz6FE", title="Love Sosa", artist="Chief Keef"),
               Song(youtube_ID="rF-hq_CHNH0", title="Versace", artist="Migos"),
               Song(youtube_ID="C0U4aDOjr_M", title="Look At Me Now", artist="Chris Brown"),
               Song(youtube_ID="vKzwbsI7ISQ", title="We Dem Boyz", artist="Wiz Khalifa"),
               Song(youtube_ID="Bo0WMtwoqtY", title="Blessed", artist="Big Sean"),
               Song(youtube_ID="Cvu0Q4Cl7pU", title="My Way", artist="Fetty Wap"),
               Song(youtube_ID="pVhYGC2CdJo", title="Back to Back", artist="Drake"), Song(youtube_ID="Z-48u_uWMHY", title="Alright", artist="Kendrick Lamar"),
               Song(youtube_ID="_JZom_gVfuw", title="Juicy", artist="Biggie"),
               Song(youtube_ID="RubBzkZzpUA", title="Started From The Bottom", artist="Drake"),
               Song(youtube_ID="ucoK6KN1dzU", title="Nothing But A G Thang", artist="Snoop Dogg"),
               Song(youtube_ID="fPTJLHjzyEo", title="Where Ya At", artist="Future"),
               Song(youtube_ID="6vwNcNOTVzY", title="Gold Digger", artist="Kanye West"),
               Song(youtube_ID="r_dh16HQkqQ", title="Hustle Hard", artist="Ace Hood"),
               Song(youtube_ID="8UFIYGkROII", title="Crank Thank Soulja Boy", artist="Soulja Boy"),
               Song(youtube_ID="LDZX4ooRsWs", title="Nicki Minaj", artist="Nicki Minaj"),
               Song(youtube_ID="hGKK8eGQQEk", title="Nasty Freestyle", artist="T-Wayne")
               Song(youtube_ID="avFq9errZCk", title="Tuesday", artist="ILOVEMAKONNEN")
               Song(youtube_ID="LDZX4ooRsWs", title="Nicki Minaj", artist="Nicki Minaj"),
               Song(youtube_ID="hGKK8eGQQEk", title="Nasty Freestyle", artist="T-Wayne")
               Song(youtube_ID="RAzzv6Ks9nc", title="Check", artist="Young Thug")
               
pop_songs=[]

rock_songs=[Song(youtube_ID="BcL---4xQYA", title="Stairway To Heaven", artist="Led Zeppelin"),
Song(youtube_ID="6JCLY0Rlx6Q", title="Shut Up and Dance", artist="Walk The Moon"),
Song(youtube_ID="TLV4_xaYynY", title="All Along The Watchtower", artist="Jimi Hendrix"),
Song(youtube_ID="pAgnJDJN4VA", title="Back in Black", artist="ACDC"),
Song(youtube_ID="D0W1v0kOELA", title="Free Bird", artist="Lynyrd Skynyrd"),
Song(youtube_ID="lDK9QqIzhwk", title="Living On A Prayer", artist="Bon Jovi"),
Song(youtube_ID="P-Q9D4dcYng", title="A Day in the Life", artist="The Beatles"),
Song(youtube_ID="vD3iXpv4h-o", title="The Wolf", artist="Mumford & Sons"),
Song(youtube_ID="mqiH0ZSkM9I", title="Hold Back The River", artist="James Bay")]

genres={"hiphop":hiphop_songs, "pop":pop_songs, "rock":rock_songs}


class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            previous_user_query=UserModel.query().filter(UserModel.currentUserID==user.user_id()).fetch()
            if previous_user_query:
                current_user = previous_user_query[0]
                current_user.is_new_user=False
            else:
                current_user = UserModel(currentUserID = user.user_id(), questions_played=0,questions_correct=0, is_new_user=True)
            current_user.put()
            template_vars={"nickname": user.nickname(),"logout_url":users.create_logout_url('/')}
            template = JINJA_ENVIRONMENT.get_template('templates/setup.html')
            self.response.write(template.render(template_vars))

        else:
            self.redirect(users.create_login_url(self.request.uri))



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
        for song in genres[genre]:
            artist_answer=self.request.get("artist"+str(counter)).lower()
            song_answer=self.request.get("song_title"+str(counter)).lower()
            if artist_answer!="" and song_answer!="":
                if artist_answer==genres[genre][counter-1].artist.lower() and song_answer==genres[genre][counter-1].title.lower():
                    amount_right+=1
            counter+=1
        user=users.get_current_user()
        user_query=UserModel.query().filter(UserModel.currentUserID==user.user_id()).fetch()
        user_in_datastore=user_query[0]
        user_in_datastore.questions_played+=len(genres[genre])
        user_in_datastore.questions_correct+=amount_right
        user_in_datastore.put()
        total_percent_correct=int((user_in_datastore.questions_correct * 1.0/user_in_datastore.questions_played)*100)

        template_values = {"amount_right": amount_right,"percent_correct":total_percent_correct}
        template = JINJA_ENVIRONMENT.get_template('templates/results.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/quiz', QuizHandler),
    ('/results', ResultsHandler)
], debug=True)

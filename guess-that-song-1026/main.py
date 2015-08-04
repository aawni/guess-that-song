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
import random
import logging



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
               Song(youtube_ID="pVhYGC2CdJo", title="Back to Back", artist="Drake")]

pop_songs=[]
genres={"hiphop":hiphop_songs, "pop":pop_songs}


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
        song_indexs=[]
        selected_songs=[]
        count=1
        while count <=8:
            rand_ind=random.randint(0,len(genres[genre])-1)
            if rand_ind not in song_indexs:
                selected_songs.append(genres[genre][rand_ind])
                song_indexs.append(rand_ind)
                count+=1
        template_values = {"songs":selected_songs,"genre":genre, "song_indexs":song_indexs}

        template = JINJA_ENVIRONMENT.get_template('templates/quiz.html')
        self.response.write(template.render(template_values))

class ResultsHandler(webapp2.RequestHandler):
    def post(self):
        amount_right=0
        genre=self.request.get("genre")
        song_indexs=self.request.get("song_indexs")
        logging.info(song_indexs)
        counter=1
        selected_songs=[]
        for ind in song_indexs:
            selected_songs.append(genres[genre][ind])

        for song in selected_songs:
            artist_answer=self.request.get("artist"+str(counter)).lower()
            song_answer=self.request.get("song_title"+str(counter)).lower()
            if artist_answer!="" and song_answer!="":
                if artist_answer==selected_songs[counter-1].artist.lower() and song_answer==selected_songs[counter-1].title.lower():
                    amount_right+=1
            counter+=1
        user=users.get_current_user()
        user_query=UserModel.query().filter(UserModel.currentUserID==user.user_id()).fetch()
        user_in_datastore=user_query[0]
        user_in_datastore.questions_played+=len(selected_songs)
        user_in_datastore.questions_correct+=amount_right
        user_in_datastore.put()
        total_percent_correct=int((user_in_datastore.questions_correct * 1.0/user_in_datastore.questions_played)*100)
        percent_correct=int((amount_right*1.0/len(selected_songs))*100)

        template_values = {"amount_right": amount_right,"total_percent_correct":total_percent_correct,"percent_correct":percent_correct}
        template = JINJA_ENVIRONMENT.get_template('templates/results.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/quiz', QuizHandler),
    ('/results', ResultsHandler)
], debug=True)

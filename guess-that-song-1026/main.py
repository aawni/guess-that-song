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
    nickname = ndb.StringProperty()
    friends_ids = ndb.StringProperty(repeated=True)


class Song(ndb.Model):
    youtube_ID = ndb.StringProperty(required=True)
    title = ndb.StringProperty(required=True)
    artist = ndb.StringProperty(required=True)
    genre = ndb.StringProperty(required=True)

hiphop_song1=Song(youtube_ID="Z-48u_uWMHY", title="Alright", artist="Kendrick Lamar",genre="hiphop")
hiphop_song2=Song(youtube_ID="frOjjVDb8R8", title="Commas", artist="Future",genre="hiphop")
hiphop_song3=Song(youtube_ID="NtTLfSOujTI", title="Planes", artist="Jeremih",genre="hiphop")
hiphop_song4=Song(youtube_ID="YWyHZNBz6FE", title="Love Sosa", artist="Chief Keef",genre="hiphop")
hiphop_song5=Song(youtube_ID="rF-hq_CHNH0", title="Versace", artist="Migos",genre="hiphop")
hiphop_song6=Song(youtube_ID="C0U4aDOjr_M", title="Look At Me Now", artist="Chris Brown",genre="hiphop")
hiphop_song7=Song(youtube_ID="vKzwbsI7ISQ", title="We Dem Boyz", artist="Wiz Khalifa",genre="hiphop")
hiphop_song8=Song(youtube_ID="Bo0WMtwoqtY", title="Blessed", artist="Big Sean",genre="hiphop")
hiphop_song9=Song(youtube_ID="Cvu0Q4Cl7pU", title="My Way", artist="Fetty Wap",genre="hiphop")
hiphop_song10=Song(youtube_ID="pVhYGC2CdJo", title="Back to Back", artist="Drake",genre="hiphop")
hiphop_song11=Song(youtube_ID="Z-48u_uWMHY", title="Alright", artist="Kendrick Lamar",genre="hiphop")
hiphop_song12=Song(youtube_ID="_JZom_gVfuw", title="Juicy", artist="Biggie",genre="hiphop")
hiphop_song13=Song(youtube_ID="RubBzkZzpUA", title="Started From The Bottom", artist="Drake",genre="hiphop")
hiphop_song14=Song(youtube_ID="ucoK6KN1dzU", title="Nothing But A G Thang", artist="Snoop Dogg",genre="hiphop")
hiphop_song15=Song(youtube_ID="fPTJLHjzyEo", title="Where Ya At", artist="Future",genre="hiphop")
hiphop_song16=Song(youtube_ID="6vwNcNOTVzY", title="Gold Digger", artist="Kanye West",genre="hiphop")
hiphop_song17=Song(youtube_ID="r_dh16HQkqQ", title="Hustle Hard", artist="Ace Hood",genre="hiphop")
hiphop_song18=Song(youtube_ID="8UFIYGkROII", title="Crank Thank Soulja Boy", artist="Soulja Boy",genre="hiphop")
hiphop_song19=Song(youtube_ID="LDZX4ooRsWs", title="Nicki Minaj", artist="Nicki Minaj",genre="hiphop")
hiphop_song20=Song(youtube_ID="hGKK8eGQQEk", title="Nasty Freestyle", artist="T-Wayne",genre="hiphop")
hiphop_song21=Song(youtube_ID="avFq9errZCk", title="Tuesday", artist="ILOVEMAKONNEN",genre="hiphop")
hiphop_song22=Song(youtube_ID="hGKK8eGQQEk", title="Nasty Freestyle", artist="T-Wayne",genre="hiphop")
hiphop_song23=Song(youtube_ID="RAzzv6Ks9nc", title="Check", artist="Young Thug",genre="hiphop")
# hiphop_song1.put()
# hiphop_song2.put()
# hiphop_song3.put()
# hiphop_song4.put()
# hiphop_song5.put()
# hiphop_song6.put()
# hiphop_song7.put()
# hiphop_song8.put()
# hiphop_song9.put()
# hiphop_song10.put()
# hiphop_song11.put()
# hiphop_song12.put()
# hiphop_song13.put()
# hiphop_song14.put()
# hiphop_song15.put()
# hiphop_song16.put()
# hiphop_song17.put()
# hiphop_song18.put()
# hiphop_song19.put()
# hiphop_song20.put()
# hiphop_song20.put()
# hiphop_song21.put()
# hiphop_song22.put()
# hiphop_song23.put()

rock_song1=Song(youtube_ID="BcL---4xQYA", title="Stairway To Heaven", artist="Led Zeppelin",genre="rock")
rock_song2=Song(youtube_ID="6JCLY0Rlx6Q", title="Shut Up and Dance", artist="Walk The Moon",genre="rock")
rock_song3=Song(youtube_ID="TLV4_xaYynY", title="All Along The Watchtower", artist="Jimi Hendrix",genre="rock")
rock_song4=Song(youtube_ID="pAgnJDJN4VA", title="Back in Black", artist="ACDC",genre="rock")
rock_song5=Song(youtube_ID="D0W1v0kOELA", title="Free Bird", artist="Lynyrd Skynyrd",genre="rock")
rock_song6=Song(youtube_ID="lDK9QqIzhwk", title="Living On A Prayer", artist="Bon Jovi",genre="rock")
rock_song7=Song(youtube_ID="P-Q9D4dcYng", title="A Day in the Life", artist="The Beatles",genre="rock")
rock_song8=Song(youtube_ID="vD3iXpv4h-o", title="The Wolf", artist="Mumford & Sons",genre="rock")
rock_song9=Song(youtube_ID="mqiH0ZSkM9I", title="Hold Back The River", artist="James Bay",genre="rock")
# rock_song1.put()
# rock_song2.put()
# rock_song3.put()
# rock_song4.put()
# rock_song5.put()
# rock_song6.put()
# rock_song7.put()
# rock_song8.put()
# rock_song9.put()

pop_song1=Song(youtube_ID="kMsHEKy8N14", title="Cool For The Summer", artist="Demi Lovato", genre="pop")
pop_song2=Song(youtube_ID="Wp0hWIO8DiU", title="Good For You", artist="Selena Gomez", genre="pop")
pop_song3=Song(youtube_ID="ncObwOWDT0Q", title="The Hills", artist="The Weeknd", genre="pop")
pop_song4=Song(youtube_ID="vFKpy59h5fM", title="Fun", artist="Chris Brown", genre="pop")
pop_song5=Song(youtube_ID="nlYbDjwBe2Y", title="Talking Body", artist="Tove Lo", genre="pop")
pop_song6=Song(youtube_ID="gdf5XaHU11U", title="Waves", artist="Mr Probz", genre="pop")
pop_song7=Song(youtube_ID="QA8ZbxS5dFs", title="Lips are Movin", artist="Megan Trainor", genre="pop")
pop_song8=Song(youtube_ID="bfC0IkLkL8o", title="The Night Is Still Young", artist="Nicki Minaj", genre="pop")
pop_song9=Song(youtube_ID="8zqdo_Umd5c", title="Somebody", artist="Natalie La Rose", genre="pop")
pop_song10=Song(youtube_ID="7hPMmzKs62w", title="Bitch Im Madonna", artist="Madonna", genre="pop")
pop_song11=Song(youtube_ID="rC8RRXcfeo", title="Stay With Me", artist="Sam Smith", genre="pop")
pop_song12=Song(youtube_ID="WpyfrixXBqU", title="Thinking Out Loud", artist="Ed Sheeran", genre="pop")
pop_song13=Song(youtube_ID="wg6J-_fTJ44", title="Cheerleader", artist="Omi", genre="pop")
pop_song14=Song(youtube_ID="rn9AQoI7mYU", title="Lean On", artist="Major Lazor", genre="pop")
pop_song15=Song(youtube_ID="ntggGgbKr4w", title="Want You To Want Me", artist="Jason Derulo", genre="pop")
# pop_song1.put()
# pop_song2.put()
# pop_song3.put()
# pop_song4.put()
# pop_song5.put()
# pop_song6.put()
# pop_song7.put()
# pop_song8.put()
# pop_song9.put()
# pop_song10.put()
# pop_song11.put()
# pop_song12.put()
# pop_song13.put()
# pop_song14.put()
# pop_song15.put()

users_current_songs={}



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
            template_values={"is_new_user":current_user.is_new_user,"logout_url":users.create_logout_url('/')}
            if current_user.nickname:
                template_values["nickname"]=current_user.nickname
            template = JINJA_ENVIRONMENT.get_template('templates/setup.html')
            self.response.write(template.render(template_values))

        else:
            self.redirect(users.create_login_url(self.request.uri))



class QuizHandler(webapp2.RequestHandler):
    def post(self):
        genre=self.request.get("genre")
        songs=Song.query().filter(Song.genre==genre).fetch()
        song_indexs=[]
        selected_songs=[]
        count=1
        while count <=5:
            rand_ind=random.randint(0,len(songs)-1)
            if rand_ind not in song_indexs:
                selected_songs.append(songs[rand_ind])
                song_indexs.append(rand_ind)
                count+=1
        template_values = {"songs":selected_songs,"genre":genre, "logout_url":users.create_logout_url('/')}
        user=users.get_current_user()
        user_in_datastore=UserModel.query().filter(UserModel.currentUserID==user.user_id()).fetch()[0]
        nickname=self.request.get("nickname")
        if nickname:
            user_in_datastore.nickname=nickname
            user_in_datastore.put()
        users_current_songs[user.user_id()]=selected_songs

        template = JINJA_ENVIRONMENT.get_template('templates/quiz.html')
        self.response.write(template.render(template_values))

class ResultsHandler(webapp2.RequestHandler):
    def post(self):
        amount_right=0
        genre=self.request.get("genre")
        counter=1
        user=users.get_current_user()
        selected_songs=users_current_songs[user.user_id()]


        for song in selected_songs:
            artist_answer=self.request.get("artist"+str(counter)).lower()
            song_answer=self.request.get("song_title"+str(counter)).lower()
            if artist_answer!="" and song_answer!="":
                if artist_answer==selected_songs[counter-1].artist.lower() and song_answer==selected_songs[counter-1].title.lower():
                    amount_right+=1
            counter+=1

        users_current_songs[user.user_id()]=[]
        user_query=UserModel.query().filter(UserModel.currentUserID==user.user_id()).fetch()
        user_in_datastore=user_query[0]
        user_in_datastore.questions_played+=len(selected_songs)
        user_in_datastore.questions_correct+=amount_right
        user_in_datastore.put()
        total_percent_correct=int((user_in_datastore.questions_correct * 1.0/user_in_datastore.questions_played)*100)
        percent_correct=int((amount_right*1.0/len(selected_songs))*100)

        template_values = {"amount_right": amount_right,"total_percent_correct":total_percent_correct,"percent_correct":percent_correct,"logout_url":users.create_logout_url('/')}
        template = JINJA_ENVIRONMENT.get_template('templates/results.html')
        self.response.write(template.render(template_values))

class FriendsHandler(webapp2.RequestHandler):
    def get(self):
        user=users.get_current_user()
        user_in_datastore=UserModel.query().filter(UserModel.currentUserID==user.user_id()).fetch()[0]
        template_values={}
        if user_in_datastore.friends_ids:
            friends_list=[]
            for friend_id in user_in_datastore.friends_ids:
                friends_list.append(UserModel.query().filter(UserModel.currentUserID==friend_id).fetch())
            template_values["friends"]=friends_list

        template = JINJA_ENVIRONMENT.get_template('templates/friends.html')
        self.response.write(template.render(template_values))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/quiz', QuizHandler),
    ('/results', ResultsHandler),
    ('/friends',FriendsHandler)
], debug=True)

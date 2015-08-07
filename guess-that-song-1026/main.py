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
import json
from datetime import datetime

start = None
# start = datetime.now()




JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class UserModel(ndb.Model):
    currentUserID = ndb.StringProperty(required = True)
    questions_correct = ndb.IntegerProperty()
    questions_played = ndb.IntegerProperty()
    nickname = ndb.StringProperty()
    friends_ids = ndb.StringProperty(repeated=True)
    best_min = ndb.StringProperty()
    best_sec = ndb.StringProperty()


class Song(ndb.Model):
    youtube_ID = ndb.StringProperty(required=True)
    title = ndb.StringProperty(required=True)
    artist = ndb.StringProperty(required=True)
    genre = ndb.StringProperty(required=True)


country_song1=Song(youtube_ID="_9TShlMkQnc", title="Live like you were dying", artist="Tim McGraw" , genre= "country")
country_song2=Song(youtube_ID="6iXPlJHKB1g", title="Springsteen", artist="Eric Church" , genre= "country")
country_song3 =Song(youtube_ID="Vd2qlMV-seQ", title="Drunk on a Plane", artist="Dierks Bently" , genre= "country")
country_song4 =  Song(youtube_ID="9wR-z4XEzKk", title="House Party", artist="Sam Hunt", genre= "country")
country_song5 = Song(youtube_ID="mWecuhUUvX0", title="Girl Crush", artist="Little Big Town", genre= "country")
country_song6 =Song(youtube_ID="LoH9klMK1rg", title="Crash and Burn", artist="Thomas Rhett", genre= "country")
country_song7= Song(youtube_ID="ZhsdBOlczHY", title="Like a Wrecking Ball", artist="Eric Church", genre= "country")
country_song8 = Song(youtube_ID="mQPjKSVe1tQ", title="Buy Me a Boat", artist="Chris Janson", genre= "country")
country_song9 = Song(youtube_ID="w11aKrkCZYQ", title="Loving You Easy", artist="Zac Brown Band", genre= "country")
country_song10 =  Song(youtube_ID="lBGUfVuBkMg", title="Burning House", artist="Cam", genre= "country")
country_song11 = Song(youtube_ID="WaSy8yy-mr8", title="Before He Cheats", artist="Carrie Underwood", genre= "country")
country_song12 =  Song(youtube_ID="lydBPm2KRaU", title="Jesus Take The Wheel", artist="Carrie Underwood", genre= "country")
country_song13 = Song(youtube_ID="ULYOUCjhVZw", title="Kick the Dust Up", artist="Luke Bryan", genre= "country")
# country_song1.put()
# country_song2.put()
# country_song3.put()
# country_song4.put()
# country_song5.put()
# country_song6.put()
# country_song7.put()
# country_song8.put()
# country_song9.put()
# country_song10.put()
# country_song11.put()
# country_song12.put()
# country_song13.put()


hiphop_song1=Song(youtube_ID="Z-48u_uWMHY", title="Alright", artist="Kendrick Lamar",genre="hiphop")
hiphop_song2=Song(youtube_ID="L-RlmxyCB2k", title="Commas", artist="Future",genre="hiphop")
hiphop_song3=Song(youtube_ID="NtTLfSOujTI", title="Planes", artist="Jeremih",genre="hiphop")
hiphop_song4=Song(youtube_ID="YWyHZNBz6FE", title="Love Sosa", artist="Chief Keef",genre="hiphop")
hiphop_song5=Song(youtube_ID="rF-hq_CHNH0", title="Versace", artist="Migos",genre="hiphop")
hiphop_song6=Song(youtube_ID="C0U4aDOjr_M", title="Look At Me Now", artist="Chris Brown",genre="hiphop")
hiphop_song7=Song(youtube_ID="vKzwbsI7ISQ", title="We Dem Boyz", artist="Wiz Khalifa",genre="hiphop")
hiphop_song8=Song(youtube_ID="Bo0WMtwoqtY", title="Blessings", artist="Big Sean",genre="hiphop")
hiphop_song9=Song(youtube_ID="Cvu0Q4Cl7pU", title="My Way", artist="Fetty Wap",genre="hiphop")
hiphop_song10=Song(youtube_ID="pVhYGC2CdJo", title="Back to Back", artist="Drake",genre="hiphop")
hiphop_song12=Song(youtube_ID="_JZom_gVfuw", title="Juicy", artist="The Notorious B.I.G",genre="hiphop")
hiphop_song13=Song(youtube_ID="RubBzkZzpUA", title="Started From The Bottom", artist="Drake",genre="hiphop")
hiphop_song14=Song(youtube_ID="ucoK6KN1dzU", title="Nothing But A G Thang", artist="Snoop Dogg",genre="hiphop")
hiphop_song15=Song(youtube_ID="fPTJLHjzyEo", title="Where Ya At", artist="Future",genre="hiphop")
hiphop_song16=Song(youtube_ID="6vwNcNOTVzY", title="Gold Digger", artist="Kanye West",genre="hiphop")
hiphop_song17=Song(youtube_ID="r_dh16HQkqQ", title="Hustle Hard", artist="Ace Hood",genre="hiphop")
hiphop_song18=Song(youtube_ID="8UFIYGkROII", title="Crank Thank Soulja Boy", artist="Soulja Boy",genre="hiphop")
hiphop_song19=Song(youtube_ID="LDZX4ooRsWs", title="Nicki Minaj", artist="Nicki Minaj",genre="hiphop")
hiphop_song20=Song(youtube_ID="hGKK8eGQQEk", title="Nasty Freestyle", artist="T-Wayne",genre="hiphop")
hiphop_song21=Song(youtube_ID="avFq9errZCk", title="Tuesday", artist="ILOVEMAKONNEN",genre="hiphop")
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
rock_song10=Song(youtube_ID="KQ6zr6kCPj8", title="Party Rock Anthem", artist="LMFAO",genre="rock")
rock_song11=Song(youtube_ID="KCy7lLQwToI", title="Don't Stop Believing", artist="Journey",genre="rock")
rock_song12=Song(youtube_ID="xPU8OAjjS4k", title="Kyrptonite", artist="3 Doors",genre="rock")
rock_song13=Song(youtube_ID="H25ORRgLxdA", title="Second Chance", artist="Shinedown",genre="rock")
rock_song14=Song(youtube_ID="ip-8VhGSMWg", title="Rockstar", artist="Nickelback",genre="rock")
rock_song15=Song(youtube_ID="RiSfTyrvJlg", title="Lips of and Angel", artist="Hinder",genre="rock")
# rock_song1.put()
# rock_song2.put()
# rock_song3.put()
# rock_song4.put()
# rock_song5.put()
# rock_song6.put()
# rock_song7.put()
# rock_song8.put()
# rock_song9.put()
# rock_song10.put()
# rock_song11.put()
# rock_song12.put()
# rock_song13.put()
# rock_song14.put()
# rock_song15.put()


pop_song1=Song(youtube_ID="kMsHEKy8N14", title="Cool For The Summer", artist="Demi Lovato", genre="pop")
pop_song2=Song(youtube_ID="Wp0hWIO8DiU", title="Good For You", artist="Selena Gomez", genre="pop")
pop_song3=Song(youtube_ID="ncObwOWDT0Q", title="The Hills", artist="The Weeknd", genre="pop")
pop_song4=Song(youtube_ID="vFKpy59h5fM", title="Fun", artist="Chris Brown", genre="pop")
pop_song5=Song(youtube_ID="O8tDTsjTqKs", title="Talking Body", artist="Tove Lo", genre="pop")
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
pop_song16=Song(youtube_ID="uO59tfQ2TbA", title="Hey Mama", artist="Nick Minaj", genre="pop")
pop_song17=Song(youtube_ID="o4C4xzkQ8q4", title="Can't Stop Dancing", artist="Becky G", genre="pop")
pop_song18=Song(youtube_ID="lKzKTDp00Z4", title="7/11", artist="Beyonce", genre="pop")
pop_song19=Song(youtube_ID="Wg92RrNhB8s", title="One Last Time", artist="Ariana Grande", genre="pop")
pop_song20=Song(youtube_ID="7RMQksXpQSk", title="This is How We Do", artist="Katy Perry", genre="pop")
pop_song21=Song(youtube_ID="5RYY0hwHIRw", title="Elastic Heart", artist="Sia", genre="pop")
pop_song22=Song(youtube_ID="-KXPLT2Xk5k", title="Chandelier", artist="Sia", genre="pop")
pop_song23=Song(youtube_ID="hnIeRkCqD-E", title="Bitch Better Have My Money", artist="Rihanna", genre="pop")
pop_song24=Song(youtube_ID="e-ORhEE9VVg", title="Blank Space", artist="Taylor Swift", genre="pop")
pop_song25=Song(youtube_ID="xo1VInw-SKc", title="Fight Song", artist="Rachel Platten", genre="pop")
pop_song26=Song(youtube_ID="nSDgHBxUbVQ", title="Photograph", artist="Ed Sheeran", genre="pop")
pop_song27 = Song(youtube_ID="dqt8Z1k0oWQ", title="Can't Feel My Face", artist="The Weeknd", genre="pop")
pop_song28 = Song(youtube_ID="DCNd-TgfOAo", title="Freedom", artist="Allen Stone", genre="pop")
pop_song29 = Song(youtube_ID="48VSP-atSeI", title="Sugar", artist="Maroon 5", genre="pop")
pop_song30 = Song(youtube_ID="h12oDyv-1as", title="Shut Up and Dance", artist="Walk the Moon", genre="pop")
pop_song31 = Song(youtube_ID="HAlz5TiKOCM", title="All About that  Bass", artist="Meghan Trainor", genre="pop")
pop_song32 = Song(youtube_ID="ABhDiXbUaBE", title="Break the Rules", artist="Charlie XCX", genre="pop")
pop_song33 = Song(youtube_ID="O4uD6o9XxLs", title="Young and Beautiful", artist="Lana Del Rey", genre="pop")
pop_song34 = Song(youtube_ID="_SoWPGzeN30", title="Love Me Like You Do", artist="Ellie Goulding", genre="pop")
pop_song35 = Song(youtube_ID="2XY3AvVgDns", title="Countdown", artist="Beyonce", genre="pop")
pop_song36= Song(youtube_ID="up9frWH_hjk", title="Drunk in Love", artist="Beyonce", genre="pop")
pop_song37 = Song(youtube_ID="zoJAcgmOS4Q", title="Roar", artist="Amy Whinehouse", genre="pop")


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
# pop_song16.put()
# pop_song17.put()
# pop_song18.put()
# pop_song19.put()
# pop_song20.put()
# pop_song21.put()
# pop_song22.put()
# pop_song23.put()
# pop_song24.put()
# pop_song25.put()
# pop_song26.put()
# pop_song27.put()
# pop_song28.put()
# pop_song29.put()
# pop_song30.put()
# pop_song31.put()
# pop_song32.put()
# pop_song33.put()
# pop_song34.put()
# pop_song35.put()
# pop_song36.put()
# pop_song37.put()


users_current_songs={}



class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            songs=Song.query().fetch()
            rand_ind=random.randint(0,len(songs))
            song_ID=songs[rand_ind].youtube_ID
            template_values={"song_ID":song_ID}

            template = JINJA_ENVIRONMENT.get_template('templates/welcome.html')
            self.response.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            previous_user_query=UserModel.query().filter(UserModel.currentUserID==user.user_id()).fetch()
            if previous_user_query:
                current_user = previous_user_query[0]
            else:
                current_user = UserModel(currentUserID = user.user_id(), questions_played=0,questions_correct=0)
                current_user.put()
            if current_user.nickname is None:
                no_nickname=True
            else:
                no_nickname=False
            template_values={"no_nickname":no_nickname,"logout_url":users.create_logout_url('/')}
            if current_user.nickname:
                template_values["nickname"]=current_user.nickname
            template = JINJA_ENVIRONMENT.get_template('templates/home.html')
            self.response.write(template.render(template_values))

        else:
            self.redirect(users.create_login_url(self.request.uri))



class QuizHandler(webapp2.RequestHandler):
    def get(self):
        global start
        start = datetime.now()

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
        user=users.get_current_user()
        users_current_songs[user.user_id()]=selected_songs
        template_values = {"songs":selected_songs,"genre":genre, "logout_url":users.create_logout_url('/')}

        template = JINJA_ENVIRONMENT.get_template('templates/quiz.html')
        self.response.write(template.render(template_values))

class ResultsHandler(webapp2.RequestHandler):
    def post(self):
        stop = datetime.now()
        genre=self.request.get("genre")
        user=users.get_current_user()
        user_query=UserModel.query().filter(UserModel.currentUserID==user.user_id()).fetch()
        user_in_datastore=user_query[0]

        correct_question_nums=[]
        selected_songs = users_current_songs[user.user_id()]
        amount_right=0
        counter=1
        for song in selected_songs:
            artist_answer=self.request.get("artist"+str(counter)).lower()
            song_answer=self.request.get("song_title"+str(counter)).lower()
            if artist_answer!="" and song_answer!="":
                if artist_answer==selected_songs[counter-1].artist.lower() and song_answer==selected_songs[counter-1].title.lower():
                    amount_right+=1
                    correct_question_nums.append(counter)
            counter+=1


        # users_current_songs[user.user_id()]=[]
        if start:
            total_time = stop - start
            seconds = str(total_time.seconds%60)
            if int(seconds)<10:
                seconds="0"+seconds
            minutes = str(total_time.seconds//60)
            if amount_right==len(selected_songs):
                if user_in_datastore.best_min>minutes:
                    if user_in_datastore.best_sec>seconds:
                        user_in_datastore.best_min=minutes
                        user_in_datastore.best_sec=seconds
                        is_best_time=True
                    else:
                        is_best_time=False
                else:
                    is_best_time=False
            else:
                is_best_time=False
        else:
            is_best_time=False
        user_in_datastore.questions_played+=len(selected_songs)
        user_in_datastore.questions_correct+=amount_right
        user_in_datastore.put()
        total_percent_correct=int((user_in_datastore.questions_correct * 1.0/user_in_datastore.questions_played)*100)
        percent_correct=int((amount_right*1.0/len(selected_songs))*100)

        template_values = {"amount_right":amount_right,"total_percent_correct":total_percent_correct,"minutes": minutes, "seconds":seconds,
        "percent_correct":percent_correct,"logout_url":users.create_logout_url('/'),"selected_songs":selected_songs,"is_best_time":is_best_time,"correct_question_nums":correct_question_nums}
        template = JINJA_ENVIRONMENT.get_template('templates/results.html')
        self.response.write(template.render(template_values))

class FriendsHandler(webapp2.RequestHandler):
    def get(self):
        user=users.get_current_user()
        template_values={}
        user_in_datastore=UserModel.query().filter(UserModel.currentUserID==user.user_id()).fetch()[0]
        if user_in_datastore.friends_ids:
            friends_list=[]
            for friend_id in user_in_datastore.friends_ids:
                friends_list.append(UserModel.query().filter(UserModel.currentUserID==friend_id).fetch()[0])
            template_values["friends"]=friends_list
        template_values["logout_url"]=users.create_logout_url('/')
        template = JINJA_ENVIRONMENT.get_template('templates/friends.html')
        self.response.write(template.render(template_values))
    def post(self):
        friend_nickname=self.request.get("friend_nickname")
        user=users.get_current_user()
        user_in_datastore=UserModel.query().filter(UserModel.currentUserID==user.user_id()).fetch()[0]
        friends=UserModel.query().filter(UserModel.nickname==friend_nickname).fetch()
        template_values={}
        if friends:
            friend=friends[0]
            if friend.currentUserID not in user_in_datastore.friends_ids:
                user_in_datastore.friends_ids.append(friend.currentUserID)
                user_in_datastore.put()
                repeat=False
            else:
                repeat=True

        response={"repeat":repeat}
        self.response.headers['Content-Type'] = "application/json"
        self.response.out.write(json.dumps(response))

class SearchNicknameHandler(webapp2.RequestHandler):
    def post(self):
        nickname=self.request.get("nickname")
        nickname_results=UserModel.query().filter(UserModel.nickname==nickname).fetch()
        if nickname_results:
            is_unique=False
        else:
            is_unique=True
            user=users.get_current_user()
            user_in_datastore=UserModel.query().filter(UserModel.currentUserID==user.user_id()).fetch()[0]
            user_in_datastore.nickname=nickname
            user_in_datastore.put()
        response={"is_unique":is_unique}
        self.response.headers['Content-Type'] = "application/json"
        self.response.out.write(json.dumps(response))

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/about.html')
        self.response.write(template.render())


app = webapp2.WSGIApplication([
    ('/', WelcomeHandler),
    ('/home', HomeHandler),
    ('/quiz', QuizHandler),
    ('/results', ResultsHandler),
    ('/friends',FriendsHandler),
    ('/searchnickname',SearchNicknameHandler),
    ('/about', AboutHandler)
], debug=True)

# -*- coding: utf-8 -*-
from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message, ContentType as Type, LoginRequest, ChatRoomAnnouncementContents, ChatRoomAnnouncement
from LineAPI.thrift.TMultiplexedProcessor import *
from LineAPI.thrift.TSerialization import *
from LineAPI.thrift.TRecursive import *
from LineAPI.thrift import transport, protocol, server
from LineAPI.thrift.protocol import TCompactProtocol
from LineAPI.thrift.transport import THttpClient
from LineAPI.thrift.Thrift import *
from datetime import datetime, timedelta, date
import time, random, sys, json, codecs, threading, asyncio, glob, re, string, os, six, ast, pytz, atexit, traceback, timeago, requests
botStart = time.time()

#line = LINE('EMAIL', 'PASSWORD')
#line = LINE()
line = LINE('EFwCK2L7xVNScnEREiK2.CxvA6Jjqk7QUeWH9E9LnyG.Iev2V7sRmmp1ztLZmfQ374m9ZxYwr/CfzlWI0T8rr3k=')

#Put your mid only(respon bot) 
acorp = ["u71755aea32502bbaae13087d7bd94d62","u81abc4643de94548bd22ba9338f3b3f3","uc01e543dea7fe2d04b8c5141edc3a749","u481a911a50dcd7c30fb3907c8fbe31ba"]
lineMid = line.profile.mid
mid = line.getProfile().mid
lineProfile = line.getProfile()
lineProfile = line.profile
# Initialize OEPoll with LINE instance
oepoll = OEPoll(line)
# Receive messages from OEPoll

with open('1.json', 'r') as fp:
    wait = json.load(fp)
with open('2.json', 'r') as fp:
    wait2 = json.load(fp)
    
read = {
    "ROM": {},
    "readPoint": {},
    "readMember": {},
    "readTime": {}
}

def autorestart():
    print("[ AUTO RESTARTED ]")
    time.sleep(10800)
    restart_program()

thread6 = threading.Thread(target=autorestart)
thread6.daemon = True
thread6.start()

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Day %02d Hours %02d Minute %02d Second' % (days, hours, mins, secs)
def timeChange(secs):
	mins, secs = divmod(secs,60)
	hours, mins = divmod(mins,60)
	days, hours = divmod(hours,24)
	weeks, days = divmod(days,7)
	months, weeks = divmod(weeks,4)
	text = ""
	if months != 0: text += "%02d Bulan" % (months)
	if weeks != 0: text += " %02d Minggu" % (weeks)
	if days != 0: text += " %02d Hari" % (days)
	if hours !=  0: text +=  " %02d Jam" % (hours)
	if mins != 0: text += " %02d Menit" % (mins)
	if secs != 0: text += " %02d Detik" % (secs)
	if text[0] == " ":
		text = text[1:]
	return text    
def backupjson_2():
    with open('2.json', 'w') as fp:
        json.dump(wait2, fp, sort_keys=True, indent=4)
def backupjson_1():
    with open('1.json', 'w') as fp:
        json.dump(wait, fp, sort_keys=True, indent=4)        
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)    
def NOTIFIED_READ_MESSAGE(op):
    if op.param1 in wait2['readPoint']:
        wait2['ROM'][op.param1][op.param2] = op.param2
        wait2['setTime'][op.param1][op.param2] = op.createdTime
        backupjson_2()
    else:
        pass
oepoll.addOpInterruptWithDict({
    OpType.NOTIFIED_READ_MESSAGE: NOTIFIED_READ_MESSAGE
})    
def SEND_MESSAGE(op):  
        msg = op.message
        agtxt = msg.text
        msg_id = msg.id
        acorp = msg.to
        saya = msg._from

        if msg.contentType == 0:
            if agtxt.lower() == 'speed':speed(acorp,'')            
            if agtxt.lower() == 'sp':speed(acorp,'')        
            #if agtxt.lower() == 'sptest':sptest(acorp,'')
            #if agtxt.lower() == 'speedtest':sptest(acorp,'')
            if agtxt.lower() == 'help':help(acorp,'')            
            if agtxt.lower() == 'debug':debug(acorp,'')            
            if agtxt.lower() == 'about':about(acorp,'')            
            if agtxt.lower() == 'lurk':lurk(acorp,'')            
            if agtxt.lower() == 'autoread on':autoreadon(acorp,"")
            if agtxt.lower() == 'autoread off':autoreadoff(acorp,"")          
            if agtxt.lower() == 'autolike on':autolikeon(acorp,"")
            if agtxt.lower() == 'autolike off':autolikeoff(acorp,"")                      
            if agtxt.lower() == 'send':
            	line.sendMessageMusic(acorp, title=line.getContact(acorp).displayName, subText=str(line.getContact(acorp).statusMessage), url='gamee.com/game/kAHVRl', iconurl="http://dl.profile.line-cdn.net/{}".format(line.getContact(acorp).pictureStatus), contentMetadata={})
            #	line.sendMessageMusic(acorp, url='http://gamee.com/game/kAHVRl', iconurl="http://gamee.com/game", contentMetadata={})
            if agtxt.lower() == 'runtime':
                start = time.time() - botStart
                line.sendMessage(acorp," 「 Timing 」\n" + runtime(start))            
            if agtxt.lower() == 'renew':
                line.sendMessage(acorp," 「 Restarting 」\nType: Restart Program\nRestarting...")                
                restart_program()                
            if agtxt.lower() == 'mentionall':
                group = line.getGroup(acorp)
                midMembers = [contact.mid for contact in group.members]
                midSelect = len(midMembers)//20
                for mentionMembers in range(midSelect+1):
                    no = 0
                    ret_ = "╭──[ Mention Member ]"
                    dataMid = []
                    for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                        dataMid.append(dataMention.mid)
                        no += 1
                        ret_ += "\n│{}. @!".format(str(no))
                    ret_ += "\n╰──[ Total {} Members ]".format(str(len(dataMid)))                  
                    line.sendMentionV2(acorp, ret_, dataMid)
            if agtxt.lower() == 'lurk result':
                if msg.to in wait2['readPoint']:
                    chiya = []
                    for rom in wait2["ROM"][acorp].items():
                        chiya.append(rom[1])
                    sidertag(acorp,'',chiya)
                    wait2['setTime'][acorp]  = {}
                    wait2['ROM'][acorp] = {}
                    backupjson_2()
                else:
                    line.sendMessage(acorp, " 「 Lurk 」\nLurk point not on♪")
            if agtxt.lower() == 'lurk on':
                if msg.to in wait2['readPoint']:
                    line.sendMessage(acorp, " 「 Lurk 」\nLurk already set♪")
                else:
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['setTime'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['setTime'][acorp]  = {}
                    wait2['ROM'][acorp] = {}
                    backupjson_2()
                    line.sendMessage(acorp, " 「 Lurk 」\nLurk point set♪")
            if agtxt.lower() == 'lurk off':
                if msg.to not in wait2['readPoint']:
                    line.sendMessage(acorp, " 「 Lurk 」\nLurk already off♪")
                else:
                    try:
                       del wait2['readPoint'][msg.to]
                       del wait2['setTime'][msg.to]
                    except:
                       pass
                    line.sendMessage(acorp, " 「 Lurk 」\nLurk point off♪")        
            if agtxt.lower().startswith('comment s'):
                separate = agtxt.split("et ")
                text = agtxt.replace(separate[0]+"et ","")
                a = wait["comment"]
                wait["comment"] = text
                backupjson_1()
                line.sendMessage(acorp," 「 Comment」\nType: Comment\nStatus: Success\nFrom: "+a.title()+"\nTo: "+text.title())                      
# Add function to OEPoll
oepoll.addOpInterruptWithDict({
    OpType.SEND_MESSAGE: SEND_MESSAGE
})    
def RECEIVE_MESSAGE(op):
        msg = op.message
        agtxt = msg.text
        msg_id = msg.id
        acorp = msg.to
        saya = msg._from
        if msg.contentType == 0:
        	return
        #if msg.contentType == 16:
        #    line.likePost(msg.contentMetadata["postEndUrl"], [25:58], [66:], likeType=1003)
       #     line.createComment(msg.contentMetadata["postEndUrl"], [25:58], [66:], wait["comment1"], [acorp])                 
        if wait["autoread"] == True:
            if msg.toType == 2:
                pass
            else:               
                line.sendChatChecked(saya,msg_id)    
            if acorp in read["readPoint"]:
                if saya not in read["ROM"][acorp]:
                    read["ROM"][acorp][saya] = True
oepoll.addOpInterruptWithDict({
    OpType.RECEIVE_MESSAGE: RECEIVE_MESSAGE
})
def postTemplate(to,data):
    url = 'https://ryns-api.herokuapp.com/postTemplate'
    data = {'to': to, 'data': data, 'lineApp': line.server.APP_NAME, 'lineToken': line.authToken}
    url = requests.post(url, json=data)
    res = url.json()
    print(res)
    
	
def testing(to,text,data):
    data = {
    "type": "flex",
    "altText": "Kepo Bner Dah",
    "contents": {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "align": "center",
                    "color": "#00FFF3",
                    "text": "hii",
                    "wrap": True
                }
            ]
        }
    }
}
    postTemplate(to,data)

def speed(to,text):
    start = time.time()
    line.sendMessage(to, "Waiting for sec...")
    take = time.time() - start 
    ret_ = "╭──「Speed」"
    ret_ += "\n├| Type : |"
    ret_ += "\n├ • Taken : %.10f"
    ret_ += "\n╰──────"   
    a = [line.sendMessage(to, ret_ % (time.time() - start)) for a in range(1)]

def debug(to,text):
    get_profile_time_start = time.time()
    get_profile = line.getProfile()
    get_profile_time = time.time() - get_profile_time_start
    get_group_time_start = time.time()
    get_group = line.getGroupIdsJoined()
    get_group_time = time.time() - get_group_time_start
    get_contact_time_start = time.time()
    get_contact = line.getContact(mid)
    get_contact_time = time.time() - get_contact_time_start
    ret_ = "╭──「Debug」"
    ret_ += "\n├| Type : |"
    ret_ += "\n├ • Get Profile" 
    ret_ += "\n├    %.10f" 
    ret_ += "\n├ • Get Contact" 
    ret_ += "\n├    %.10f"  
    ret_ += "\n├ • Get Group" 
    ret_ += "\n├    %.10f"
    ret_ += "\n╰──────"
    line.sendMessage(to, ret_ % (get_profile_time/4,get_contact_time/4,get_group_time/4))
   # line.sendMessage(to, " 「 Debug 」\nType:\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/4,get_contact_time/4,get_group_time/4))
def sidertag(to, text='', dataMid=[]):
    now = datetime.now()
    arr = []
    list_text=' 「 Lurk 」\nLurkers: %i Orang'%(len(dataMid))
    if '[list]' in text.lower():
        i=0
        for l in dataMid:
            list_text+='\n@[list-'+str(i)+']'
            i=i+1
        text=text.replace('[list]', list_text)
    elif '[list-' in text.lower():
        text=text
    else:
        i=0
        no=0
        for l in dataMid:
            z = ""
            chiya = []
        for rom in wait2["setTime"][to].items():
            chiya.append(rom[1])
        for b in chiya:
            a = str(timeago.format(now,b/1000))
            no+=1
            list_text+='\n   '+str(no)+'. @[list-'+str(i)+']\n     「 '+a+" 」"
            i=i+1
        list_text +="\n   Data Rewrite:\n      "+datetime.now().strftime('%H:%M:%S')
        text=text+list_text
    i=0
    for l in dataMid:
        mid=l
        name='@[list-'+str(i)+']'
        ln_text=text.replace('\n',' ')
        if ln_text.find(name):
            line_s=int( ln_text.index(name) )
            line_e=(int(line_s)+int( len(name) ))
        arrData={'S': str(line_s), 'E': str(line_e), 'M': mid}
        arr.append(arrData)
        i=i+1
    contentMetadata={'MENTION':str('{"MENTIONEES":' + json.dumps(arr).replace(' ','') + '}')}
    line.sendMessage(to, text, contentMetadata)
def autoreadon(to,text):
    if wait["autoread"] == True:
        line.sendMessage(to," 「 Auto Read 」\nAuto Read already on")
    else:
        wait["autoread"] = True
        backupjson_1()
        line.sendMessage(to," 「 Auto Read 」\nAuto Read set to on")
def autoreadoff(to,text):
    if wait["autoread"] == False:
        line.sendMessage(to," 「 Auto Read 」\nAuto Read already off")
    else:
        wait["autoread"] = False
        backupjson_1()
        line.sendMessage(to," 「 Auto Read 」\nAuto Read set to off")
def autolikeon(to,text):
    if wait["autolike"] == True:
        line.sendMessage(to," 「 Auto Like 」\nAuto Like already on")
    else:
        wait["autolike"] = True
        backupjson_1()
        line.sendMessage(to," 「 Auto Like 」\nAuto Like set to on")
def autolikeoff(to,text):
    if wait["autolike"] == False:
        line.sendMessage(to," 「 Auto Like 」\nAuto Like already off")
    else:
        wait["autolike"] = False
        backupjson_1()
        line.sendMessage(to," 「 Auto Like 」\nAuto Like set to off")        
def lurk(to,text):
    if to in wait2['readPoint']:
        ret_ ="「Lurk」\nLurk State: ENABLED♪"
    else:
        ret_ ="「Lurk」\nLurk State: DISABLED♪"
    line.sendMessage(to, ret_+"\nCommand:\n Lurk Point\n  Usage: lurk on\n Lurk Del\n  Usage:  lurk off\n Lurk Cek\n  Usage: lurk result")
def about(to,text):
    agler = "u71755aea32502bbaae13087d7bd94d62"  
    friend = line.getAllContactIds()
    group = line.getGroupIdsJoined()
    blockedlist = line.getBlockedContactIds()
    favorite = line.getFavoriteMids()
    userid = line.getProfile().userid
    region = line.getProfile().regionCode
    timeNow = time.time()
    runtime = timeNow - botStart
    runtime = timeChange(runtime)
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    ret_ = "╭──「About Selfbot」"
    ret_ += "\n├ • User : @!"
    ret_ += "\n├ • Friend : {}".format(str(len(friend)))
    ret_ += "\n├ • Group : {}".format(str(len(group)))
    ret_ += "\n├ • Runtime : {}".format(str(runtime))
    ret_ += "\n├ • Blocked : {}".format(str(len(blockedlist))) 
    ret_ += "\n├ • Favorite : {}".format(str(len(favorite)))
    ret_ += "\n├ • UserId : {}".format(str(userid))                                    
    ret_ += "\n├ • Region : {}".format(str(region))
    ret_ += "\n├ • Type : Selfbot"
    ret_ += "\n├ • Version : Beta v6.9"
    ret_ += "\n├ • Creator : @!"
    ret_ += "\n├──「About Time」"
    ret_ += "\n├ • Day : " + datetime.strftime(timeNow,'%Y-%m-%d')
    ret_ += "\n├ • Time : " + datetime.strftime(timeNow,'%H:%M:%S') + " WIB"
    ret_ += "\n├──「Special Thanks」"
    ret_ += "\n├ • TNB_TEAM"
    ret_ += "\n├ • Naufal-Agler"
    ret_ += "\n├ • And Other People:)"
    ret_ += "\n╰───「Finish」"
    line.sendMentionV2(to, ret_, [lineMid, agler])
def help(to,text):
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz) 
    agler = "uc01e543dea7fe2d04b8c5141edc3a749"  
    ret_ = "╭──「Selfbot v8.1」"
    ret_ += "\n├    | Command |"
    ret_ += "\n├ • Lurk"
    ret_ += "\n├ • Mentionall"
    ret_ += "\n├ • Runtime"
    ret_ += "\n├ • Speed/Sp"
    #ret_ += "\n├ • Sptest"
    ret_ += "\n├ • Debug"
    ret_ += "\n├ • About"
    ret_ += "\n├──────"
    ret_ += "\n├ • Autoread on/off"
    ret_ += "\n├ • Autolike on/off"
    ret_ += "\n├ • Comment set"
    ret_ += "\n├ • Renew" 
    ret_ += "\n├──────"    
    ret_ += "\n├    | Bot Info |" 
    ret_ += "\n├ •  User : @!" 
    ret_ += "\n├ •  Creator : @!"         
    ret_ += "\n├ •  Day : " + datetime.strftime(timeNow,'%Y-%m-%d')
    ret_ += "\n├ •  Time : " + datetime.strftime(timeNow,'%H:%M:%S')
    ret_ += "\n├ •  Selfbot Edition"         
    ret_ += "\n╰──────"
    line.sendMentionV2(to, ret_, [lineMid, agler])     

def aLIKE():
    while True:
        if wait['autolike'] == True:     
            a = line.getFeed()
            for i in a["result"]["feeds"]:
                c = i['post']['postInfo']['postId']
                d = i['post']['userInfo']['mid']      
                try:                       
                    line.likePost(d,c,random.choice([1001,1002,1003,1004,1005]))
                    #time.sleep(1)
                    #line.createComment(d,c,'{}'.format(wait['comment']))
                    #time.sleep(1)
                    print("DiLike")
                except:
                    pass
    else:
    	pass
time.sleep(30)                  
        #else:
            #pass       
        #else:                                 
            #else:                    
   
thread2 = threading.Thread(target=aLIKE)
thread2.daemon = True
thread2.start()

def autolike():
    count = 1
    while True:
        try:
           for posts in line.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                   line.likePost(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   print("Like")
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          line.createComment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread3 = threading.Thread(target=autolike)
thread3.daemon = True
thread3.start()

def autoLike():
    count = 1
    while True:
        try:
          # for posts in cl.getFeed(postLimit=10, commentLimit=1, likeLimit=1, order='TIME')["result"]["feed"]:
             if hasil["postInfo"]["homeId"]["postId"] is False:
                if wait["sukaPost"] == True:
                   line.likePost(hasil["userMid"]["writerMid"], hasil["postInfo"]["postId"], likeType=1001)
                   print("Like")
                   if wait["commentOn"] == True:
                      if hasil["homeId"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          line.createComment(posts["userMid"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass

thread5 = threading.Thread(target=autoLike)
thread5.daemon = True
thread5.start()   
            
def autoLiked():
	#if settings["sukaPost"] == True:
		lastTimeLiking = time.time()
		if time.time() - lastTimeLiking >= 60*60:
			listLikeType = 1001
			myComment = "lsb #hunniextamvan"
			feed = line.getFeed()
			if feed["message"] != 'succes':
				lastTimeLiking = time.time()
				return True
			del feed["result"]["feedInfos"]
			result = ["result"]["feeds"]
			for res in result:
				postInfo = res["post"]["postInfo"]
				homeId = postInfo["homeId"]
				postId = postInfo["postId"]
				likeStat = postInfo["liked"]
				if likeStat == True:
					continue
				else:
					line.likePost(homeId, postId, listLikeType)
					line.createComment(homeId, postId, myComment)
					lastTimeLiking = time.time()

thread1 = threading.Thread(target=autoLiked)
thread1.daemon = True
thread1.start()   

while True:
    oepoll.trace()    
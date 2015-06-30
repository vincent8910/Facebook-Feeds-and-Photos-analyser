import facebook
import numpy
import networkx
import pylab
from collections import Counter
from operator import itemgetter
from collections import OrderedDict

ACCESS_TOKEN = 'CAACEdEose0cBAGB2cqdiuFxgUi5wst86CrvYLL0QDnZBTP7ZBc5lYkFA10PTTZAdiOU14L4Iqh3brsSYzcYjSKPS6zTp5dvK6srwh7mDXVXt1GeDsOLx8nnoxUFUzbQQfOqvW4mQCcbsMVqgZAyV7WUZAdl0pZCCrTyctLFDgNhZCyZAdoV2PI3ZCepGFYMEjXvVruZCOlJourKAZDZD'
fb = facebook.GraphAPI(ACCESS_TOKEN)

def getBirth(fb):
    print "start get birth"
    arg = {'fields': 'birthday,name'}
    fbirths = fb.get_object("me/friends",**arg)
    return fbirths

def starsign(fbirths):
    name = []
    birth = []
    month=[]
    Aries=0	
    Taurus=0	
    Gemini=0
    Cancer=0	
    Leo=0	
    Virgo=0	
    Libra=0	
    Scorpio=0	
    Sagittarius=0	
    Capricorn=0	
    Aquarius=0	
    Pisces=0
    for fbirth in fbirths['data']:
        if('birthday' in fbirth):
            tempstr = str(fbirth['birthday'])
            tempstr_c=tempstr.split("/")
            day =  int(str(tempstr_c[1]),10)
            month =  int(str(tempstr_c[0]),10)
            birth.extend(tempstr if type(tempstr) == list else [tempstr])
            if(month==1):
                if(day>=1 and day<=20):
                    Capricorn+=1
                else:
                    Aquarius+=1
            if(month==2):
                if(day>=1 and day<=29):
                    Aquarius+=1
                else:
                    Pisces+=1
            if(month==3):
                if(day>=1 and day<=20):
                    Pisces+=1
                else:
                    Aries+=1	
            if(month==4):
                if(day>=1 and day<=20):
                    Aries+=1
                else:
                    Taurus+=1
            if(month==5):
                if(day >=1 and day <=21):
                    Taurus+=1
                else:
                    Gemini+=1
            if(month==6):
                if(day >=1 and day <=21):
                    Gemini+=1
                else:
                    Cancer+=1
            if(month==7):
                if(day >=1 and day <=23):
                    Cancer+=1
                else:
                    Leo+=1
            if(month==8):
                if(day >=1 and day <=23):
                    Leo+=1
                else:
                    Virgo+=1
            if(month==9):
                if(day >=1 and day <=23):
                    Virgo+=1
                else:
                    Libra+=1
            if(month==10):
                if(day >=1 and day <=23):
                    Libra+=1
                else:
                    Scorpio+=1
            if(month==11):
                if(day >=1 and day <=22):
                    Scorpio+=1
                else:
                    Sagittarius+=1
            if(month==12):
                if(day >=1 and day <=22):
                    Sagittarius+=1
                else:
                     Capricorn+=1
        else:
            birth.extend("x")
    
    for fbirth in fbirths['data']:
        tempstr = str(fbirth['name'].encode('utf-8'))
        name.extend(tempstr if type(tempstr) == list else [tempstr])

    for i in range (0,len(name)):
        print '%s : %s' %(name[i],birth[i])

    print '%s : %d' %("Aries",Aries)
    print '%s : %d' %("Taurus",Taurus)
    print '%s : %d' %("Gemini",Gemini)
    print '%s : %d' %("Cancer",Cancer)
    print '%s : %d' %("Leo",Leo)
    print '%s : %d' %("Virgo",Virgo)
    print '%s : %d' %("Libra",Libra)
    print '%s : %d' %("Scorpio",Scorpio)
    print '%s : %d' %("Sagittarius",Sagittarius)
    print '%s : %d' %("Capricorn",Capricorn)
    print '%s : %d' %("Aquarius",Aquarius)
    print '%s : %d' %("Pisces",Pisces)

    print len(name)
#------------------------------------------------------------------------------------------

fbirths = getBirth(fb)
starsign(fbirths)
print '============================'
print "finished!"

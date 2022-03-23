# -*- encoding=utf-8 -*-

import os
import sys
import time
import pygame
from tkinter   import *
from tkinter   import ttk
from tkinter   import messagebox
from threading import Thread

global mainw

mainw = Tk()

width = 1200
height = 715

mainw.title('Purpose Player 4')
mainw.geometry('{}x{}+{}+{}'.format(width, height, 0, 0))

columns = ['Type', 'Size', 'Date' ]

global tr

scr1=Scrollbar(mainw,orient='vertical')

tr = ttk.Treeview(
           mainw,
           height=40,
           columns=columns,
           show='tree headings',
           selectmode='browse',
           yscrollcommand=scr1.set,
                 )

s = ttk.Style()
s.configure('Treeview', rowheight=16)
                
tr.heading('#0'  , text='Name')
tr.heading('Type', text='Type')  
tr.heading('Size', text='Size')  
tr.heading('Date', text='Date')  

tr.column('#0'  , width=1200-60-70-160-12) 
tr.column('Type', width= 60)
tr.column('Size', width= 70)
tr.column('Date', width=160)

scr1['command']=tr.yview

tr.grid(row=0,rowspan=40,column=0,columnspan=80)

scr1.grid(row=0,rowspan=40,column=81,sticky='ns')

#tr.config(yscrollcommand = scr1.set)
#scr1.config(command = tree1.yview)

global img1
global img2
global img3
global img4

#img1=PhotoImage(file='./i1.png')
#img2=PhotoImage(file='./i2.png')
#img3=PhotoImage(file='./i3.png')
#img4=PhotoImage(file='./i4.png')

info = [ '', '', '',]

global rf1,rf2,rf3,rf4,rf5,rf6,rf7,rf8,rf9,rf10,rf11

rf1 =tr.insert('', END, text='<>/'  , open=True, values=info )
rf2 =tr.insert('', END, text='<>C:/', open=True, values=info )
rf3 =tr.insert('', END, text='<>D:/', open=True, values=info )
rf4 =tr.insert('', END, text='<>E:/', open=True, values=info )
rf5 =tr.insert('', END, text='<>F:/', open=True, values=info )
rf6 =tr.insert('', END, text='<>G:/', open=True, values=info )
rf7 =tr.insert('', END, text='<>H:/', open=True, values=info )
rf8 =tr.insert('', END, text='<>I:/', open=True, values=info )
rf9 =tr.insert('', END, text='<>J:/', open=True, values=info )
rf10=tr.insert('', END, text='<>K:/', open=True, values=info )
rf11=tr.insert('', END, text='<>L:/', open=True, values=info )

global mu_play,mu_load,mu_pause,item_id0

mu_play=0
mu_load=0
mu_pause=0
item_id0=''

probar1 = ttk.Progressbar(mainw, orient=HORIZONTAL, length=980, mode='indeterminate')
probar1['maximum'] = 100
probar1['value'] = 0
probar1.grid(row=41,column=0,columnspan=65)

probar2 = ttk.Progressbar(mainw, orient=HORIZONTAL, length=200, mode='indeterminate')
probar2['maximum'] = 100
probar2['value'] = 0
probar2.grid(row=41,column=66,columnspan=14)

lb = Label(mainw, width=18, text="00:00:00/00:00:00")
lb.grid(row=42,column=0)

lb2 = Label(mainw, width=8, text="Volume")
lb2.grid(row=42,column=79)


def btClick():

    global mu_play,mu_load,mu_pause

    if mu_load==1:
        if mu_play==1:
            mu_pause=1
            pygame.mixer.music.pause()
            mu_play=0
            bt['text']='Play'
        else:
            pygame.mixer.music.unpause()
            mu_play=1
            mu_pause=0
            bt['text']='Pause'
        
global bt

bt=Button(mainw,height=1,width=20,text='Play',command=btClick)
bt.grid(row=42,column=35)

def file_size_format(size_n1):

  i=0
  f1=0.0

  if size_n1<0 or size_n1>=100000:
      size_str2="****"
  elif size_n1>=10000 and size_n1<100000:
      i=size_n1/100;
      size_str2=str(i)
  elif size_n1>=1000 and size_n1<10000:
      i=size_n1/10;
      f1=i/10;
      size_str2=str(f1)
  elif size_n1<1000:
      f1=size_n1/100;
      size_str2=str(f1)

  #print('1-',size_str2)

  if len(size_str2)>5:
    size_str2=size_str2[0:4]
  #elif len(size_str2)<4:
  #  size_str2="    "

  #print('2-',size_str2)

  return size_str2
  
def trClick(event):

    global mu_play,mu_load,mu_pause,item_id0,mainw,tr

    item_dir  =''
    item_id0  =tr.selection()
    item_id1  =item_id0
    item_text =tr.item(item_id1,'text')
    
    if len(item_text)==0:
        return
    if item_text[0]==':':
      item_text2=item_text.split('|',1)
    elif item_text[0]=='<':
      item_text2=item_text.split('>',1)
    else:
      return
    item_dir=item_text2[1]
    
    while 1:
      item_id2  =tr.parent(item_id1)
      
      if len(item_id2)==0:
        item_text5=item_dir
        break
      item_text3=tr.item(item_id2,'text')
      
      item_text4=item_text3.split('>',1)
      item_text5=item_text4[1].upper()

      if item_text4[1]=='/':
        item_dir=item_text4[1]+item_dir
        break
      elif item_text5[0]>='C' and item_text5[0]<='Z' and item_text5[1]==':':
        item_dir=item_text5+item_dir
        break
      else:
        item_dir=item_text4[1]+'/'+item_dir
        item_id1=item_id2

    driver=0     
    if len(item_dir)==3:
        if item_dir[0]>='C' and item_dir[0]<='Z' and item_dir[1]==':' :
            driver=1

    if os.path.isdir(item_dir) or driver==1 :
        print(item_dir,driver)

        item_empt=1
        chld=tr.get_children(item_id0)
        
        if len(chld)==0:
          dirs=[]
          try:
              dirs = os.listdir(item_dir)
              dirs.sort()
              dir_ok=1
          except:
              dir_ok=0

          if dir_ok==1:
            for files in dirs:
              
              info2= ['', '', '',]
              if os.path.isdir(item_dir+'/'+files):
                  item_empt=0
                  tr.insert(item_id0, END, text='<>'+files, open=True)
            
          dirs=[]
          try:  
              dirs = os.listdir(item_dir)
              dirs.sort()
              dir_ok=1
          except:
              dir_ok=0

          if dir_ok==1:
            for files in dirs:
              
              if os.path.isfile(item_dir+'/'+files):
                item_empt=0
                ext=files.split('.',-1)
                
                if len(ext[-1])>5:
                    ext[-1]=''
                
                file_info=os.lstat(item_dir+'/'+files)
                if file_info.st_size>=1000000000000000:
                  size_str1=''
                  size_str2='****'
                elif file_info.st_size>=1000000000000 and file_info.st_size<1000000000000000:
                  size_str1='TB'
                  size_n1  =int(file_info.st_size/10000000000)
                  size_str2=file_size_format(size_n1)
                elif file_info.st_size>=1000000000 and file_info.st_size<1000000000000:
                  size_str1='GB'
                  size_n1  =int(file_info.st_size/10000000)
                  size_str2=file_size_format(size_n1)
                elif file_info.st_size>=1000000 and file_info.st_size<1000000000:
                  size_str1='MB'
                  size_n1  =int(file_info.st_size/10000)
                  size_str2=file_size_format(size_n1)
                elif file_info.st_size>=1000 and file_info.st_size<1000000:
                  size_str1='KB'
                  size_n1  =int(file_info.st_size/10)
                  size_str2=file_size_format(size_n1)
                elif file_info.st_size<1000:
                  size_str1='B '
                  size_str2=str(file_info.st_size)

                mtime = file_info.st_mtime
                file_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
                
                info2= [ext[-1], size_str2+size_str1, file_time,]
                
                tr.insert(item_id0, END, text=':|'+files, open=True, values=info2 )

          if item_empt==1:
              tr.insert(item_id0, END, text='??'+'Empty Fold', open=True)

        else:
          for o in chld:
              tr.delete(o)
    else:
        event = pygame.event.Event(pygame.USEREVENT+2)
        pygame.event.post(event)
            
def mpNext():

  global mu_load,mu_play,mu_pause,item_id0,mainw,tr,bt

  pygame.init()
  chld=[]
  id0=[]
  stop=0
  
  pygame.time.set_timer(pygame.USEREVENT+3,500)
  
  while 1:
    event = pygame.event.wait()
    
    print('event.type',event.type,'pg.User1',pygame.USEREVENT+1)
    
    if event.type == pygame.QUIT:
        return

    if event.type == pygame.USEREVENT+2 : #start to play

      id0=item_id0

      if pygame.mixer.music.get_busy() or mu_pause==1 :
        pygame.mixer.music.stop()

        bt['text']='Play'     #dead lock
        mu_load=0
        mu_play=0
        stop=1
      
      item_id1  =tr.parent(id0)

      chld=tr.get_children(item_id1)
      step=0
      nextsong=''

      for o in chld:

        if step==0:
            for o2 in id0:
                if o==o2:
                    step=1

        if step==1:
            item_dir  =''
            o3        =o

            try:
                item_text =tr.item(o3,'text')
            except:
                break
            
            if len(item_text)==0:
                break

            if item_text[0]==':':
                item_text2=item_text.split('|',1)
            else:
                item_text2=item_text.split('>',1)
            item_dir=item_text2[1]

            while 1:
              item_id2  =tr.parent(o3)
              
              if len(item_id2)==0:
                  item_text5=item_dir
                  break
              item_text3=tr.item(item_id2,'text')
              
              item_text4=item_text3.split('>',1)
              item_text5=item_text4[1].upper()

              if item_text4[1]=='/':
                  item_dir=item_text4[1]+item_dir
                  break
              elif item_text5[0]>='C' and item_text5[0]<='Z' and item_text5[1]==':':
                  item_dir=item_text5+item_dir
                  break
              else:
                  item_dir=item_text4[1]+'/'+item_dir
                  o3=item_id2

            print('item_dir',item_dir)
            
            item_dir2=item_dir.split('.',-1)
            item_dir2[-1]=item_dir2[-1].lower()
            if item_dir2[-1]=='mp3':

                try:
                    pygame.mixer.init()
                    pygame.mixer.music.load(item_dir)
                    pygame.mixer.music.play()
                except:
                    print('break1')
                    break;

                bt['text']='Pause'
                mu_load=1
                mu_play=1

                ol=[o,]
                tr.selection_set(ol)

                mainw.title(item_dir)
                
                pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)

                vl=pygame.mixer.music.get_volume()
                vl2=vl*100
                probar2['value'] = vl2
                mainw.update()
                
                step=2
                print('continue2')
                continue
            else:
                print('break3')
                break
                
        if step==2:
            nextsong=o
            print('break4')
            break

    if event.type == pygame.USEREVENT+1: #auto next
    
      if stop==1:
        stop=0
        continue

      if pygame.mixer.music.get_busy() or mu_pause==1 :
        pygame.mixer.music.stop()

        bt['text']='Play'     #dead lock
        mu_load=0
        mu_play=0
        stop=1
                
      step=0
      id0=[nextsong,]
      nextsong=''

      for o in chld:

        if step==0:
            for o2 in id0:
                if o==o2:
                    step=1

        if step==1:
            item_dir  =''
            o3        =o

            try:
                item_text =tr.item(o3,'text')
            except:
                break
            
            if len(item_text)==0:
                break

            if item_text[0]==':':
                item_text2=item_text.split('|',1)
            else:
                item_text2=item_text.split('>',1)
            item_dir=item_text2[1]

            while 1:
              item_id2  =tr.parent(o3)
              
              if len(item_id2)==0:
                  item_text5=item_dir
                  break
              item_text3=tr.item(item_id2,'text')
              
              item_text4=item_text3.split('>',1)
              item_text5=item_text4[1].upper()

              if item_text4[1]=='/':
                  item_dir=item_text4[1]+item_dir
                  break
              elif item_text5[0]>='C' and item_text5[0]<='Z' and item_text5[1]==':':
                  item_dir=item_text5+item_dir
                  break
              else:
                  item_dir=item_text4[1]+'/'+item_dir
                  o3=item_id2


            item_dir2=item_dir.split('.',-1)
            item_dir2[-1]=item_dir2[-1].lower()
            if item_dir2[-1]=='mp3':

                try:
                    pygame.mixer.init()
                    pygame.mixer.music.load(item_dir)
                    pygame.mixer.music.play()
                except:
                    print('break1')
                    break;

                bt['text']='Pause'
                mu_load=1
                mu_play=1

                ol=[o,]
                tr.selection_set(ol)

                mainw.title(item_dir)
                
                pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)

                vl=pygame.mixer.music.get_volume()
                vl2=vl*100
                probar2['value'] = vl2
                mainw.update()
                
                step=2
                print('continue2')
                continue
            else:
                print('break3')
                break
                
        if step==2:
            nextsong=o
            print('break4')
            break
            
    if event.type == pygame.USEREVENT+3 : #display position
    
      if pygame.mixer.music.get_busy() :
        ps=pygame.mixer.music.get_pos()
        ps1=int(ps/1000)
        ps2=int(ps1/3600)
        ps3=int((ps1-ps2*3600)/60)
        ps4=int(ps1-ps2*3600-ps3*60)
        
        s1=str(int(ps2))
        if len(s1)==1:
          s1='0'+s1
        s2=str(int(ps3))
        if len(s2)==1:
          s2='0'+s2
        s3=str(int(ps4))
        if len(s3)==1:
          s3='0'+s3
          
        ps5=s1+':'+s2+':'+s3+'/00:00:00'
        print('pos=',ps5)
        lb.config(text=ps5)

def mainwClose():

    global mainw

    event = pygame.event.Event(pygame.QUIT)
    pygame.event.post(event)
    
    mainw.destroy()

mainw.protocol("WM_DELETE_WINDOW", mainwClose)

tr.bind('<ButtonRelease-1>', trClick)

thr=Thread(target=mpNext)
thr.start()

mainw.mainloop()


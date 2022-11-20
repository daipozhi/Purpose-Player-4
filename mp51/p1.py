# -*- encoding=utf-8 -*-

import sys

args = sys.argv[1:] 

if len(args)>=2 :
  width =int(args[0])
  height=int(args[1])
  if width <640 :
      width=640
  if width >7680:
      width=7680
  if height<480:
      height=480
  if height>4320:
      height=4320
else:
  width  = 1200
  height =  720

g_topic_h =20
g_char_h  =17
g_scr_h   =17
g_bt_h    =20

g_lines= int((height -g_topic_h -g_scr_h -g_bt_h)/g_char_h -1 +0.5)

g_char_w=15
g_tr_w  = int(width/g_char_w +0.5)
g_probar2_w= int(200/g_char_w +0.5)

g_pbar1=1.0             # 16  minutes
g_pbar2=g_pbar1*0.7     # 32  minutes
g_pbar3=g_pbar2*0.49    # 64  minutes
g_pbar4=g_pbar3*0.343   # 128 minutes

g_bt_init=0
g_bt_step=0
g_bt_y1=0
g_bt_y2=0
g_bt_y3=0
g_bt_adj=0

g_bt_y1=height

import os
import time
import pygame
from tkinter   import *
from tkinter   import ttk
from tkinter   import messagebox
from threading import Thread

global mainw

mainw = Tk()

mainw.title('Purpose Player 4')
mainw.geometry('{}x{}+{}+{}'.format(width, height, 0, 0))

mainw.grid_rowconfigure(0, weight=1)
mainw.grid_columnconfigure(2, weight=1)

columns = ['Type', 'Size', 'Date' ]

global tr

scr1=Scrollbar(mainw,orient='vertical')

tr = ttk.Treeview(
           mainw,
           height=g_lines,
           columns=columns,
           show='tree headings',
           selectmode='browse',
           yscrollcommand=scr1.set,
                 )

s = ttk.Style()
s.configure('Treeview', rowheight=17)
                
tr.heading('#0'  , text='Name')
tr.heading('Type', text='Type')  
tr.heading('Size', text='Size')  
tr.heading('Date', text='Date')  

tr.column('#0'  , width=width-60-70-160-12) 
tr.column('Type', width= 60,minwidth=60 ,stretch=0)
tr.column('Size', width= 70,minwidth=70 ,stretch=0)
tr.column('Date', width=160,minwidth=160,stretch=0)

scr1['command']=tr.yview

tr.grid(row=0,rowspan=g_lines+1,column=0,columnspan=g_tr_w,sticky='nsew')

scr1.grid(row=0,rowspan=g_lines+1,column=g_tr_w,sticky='nsew')

#global img1
#global img2
#global img3
#global img4

#img1=PhotoImage(file='./i1.png')
#img2=PhotoImage(file='./i2.png')
#img3=PhotoImage(file='./i3.png')
#img4=PhotoImage(file='./i4.png')

info = [ '', '', '',]

global rf1,rf2,rf3,rf4,rf5,rf6,rf7,rf8,rf9,rf10,rf11

rf1 =tr.insert('', END, text='</>'  , open=False, values=info )
rf2 =tr.insert('', END, text='<C:/>', open=False, values=info )
rf3 =tr.insert('', END, text='<D:/>', open=False, values=info )
rf4 =tr.insert('', END, text='<E:/>', open=False, values=info )
rf5 =tr.insert('', END, text='<F:/>', open=False, values=info )
rf6 =tr.insert('', END, text='<G:/>', open=False, values=info )
rf7 =tr.insert('', END, text='<H:/>', open=False, values=info )
rf8 =tr.insert('', END, text='<I:/>', open=False, values=info )
rf9 =tr.insert('', END, text='<J:/>', open=False, values=info )
rf10=tr.insert('', END, text='<K:/>', open=False, values=info )
rf11=tr.insert('', END, text='<L:/>', open=False, values=info )

global mu_play,mu_load,mu_pause,mu_pos,item_id0,item_cur,item_notclose,item_close

mu_play=0
mu_load=0
mu_pause=0
mu_pos=0
item_id0=''
item_cur=''
item_notclose=0
item_close=0

probar1 = ttk.Progressbar(mainw, orient=HORIZONTAL, length=width-200-20, mode='indeterminate')
probar1['maximum'] = 10000
probar1['value'] = 0
probar1.grid(row=g_lines+2,column=0,columnspan=g_tr_w-g_probar2_w-1,sticky='nsew')

probar2 = ttk.Progressbar(mainw, orient=HORIZONTAL, length=200, mode='indeterminate')
probar2['maximum'] = 100
probar2['value'] = 100
probar2.grid(row=g_lines+2,column=g_tr_w-g_probar2_w,columnspan=g_probar2_w,sticky='nsew')

global bt3

def bt1Click():
    global mu_pos
    
    if pygame.mixer.music.get_busy() :
        ps=pygame.mixer.music.get_pos()
        #print(int(ps/1000))
        ps1=mu_pos+ps/1000-30
        if ps1<0:
            ps1=0
        #print(ps1)
        #pygame.mixer.music.rewind()
        #pygame.mixer.music.set_pos(ps1)
        pygame.mixer.music.play(0,ps1)
        mu_pos=ps1
    return
    
def bt2Click():
    global mu_pos
    
    if pygame.mixer.music.get_busy() :
        ps=pygame.mixer.music.get_pos()
        #print(int(ps/1000))
        ps1=mu_pos+ps/1000+30
        #print(ps1)
        #pygame.mixer.music.rewind()
        #pygame.mixer.music.set_pos(ps1)
        pygame.mixer.music.play(0,ps1)
        mu_pos=ps1
    return

def bt3Click():

    global mu_play,mu_load,mu_pause

    if mu_load==1:
        if mu_play==1:
            mu_pause=1
            pygame.mixer.music.pause()
            mu_play=0
            bt3['text']='Play'
        else:
            pygame.mixer.music.unpause()
            mu_play=1
            mu_pause=0
            bt3['text']='Pause'
        
def bt4Click():

    vl=probar2['value']
    if vl<2 :
      vl=2
    vl2=vl*0.85
    if vl2<0  :
        vl2=0
    if vl2>100:
        vl2=100
    probar2['value'] = vl2
    pygame.mixer.music.set_volume(vl2/100)
    mainw.update()
                
    return


def bt5Click():

    vl=probar2['value']
    if vl<2 :
      vl=2
    vl2=vl*1.18
    if vl2<0  :
        vl2=0
    if vl2>100:
        vl2=100
    probar2['value'] = vl2
    pygame.mixer.music.set_volume(vl2/100)
    mainw.update()
                
    return

bt1=Button(mainw,height=1,width=1,text='-',command=bt1Click)
bt1.grid(row=g_lines+3,column=0)

lb1 = Label(mainw, height=1, width=18, text="00:00:00/00:00:00")
lb1.grid(row=g_lines+3,column=1)

bt2=Button(mainw,height=1,width=1,text='+',command=bt2Click)

bt3=Button(mainw,height=1,width=14,text='Play',command=bt3Click)
#bt3.grid(row=g_lines+3,column=37)

bt4=Button(mainw,height=1,width=1,text='-',command=bt4Click)

lb2 =Label(mainw, height=1, width=6, text="Volume")
#lb2.grid(row=g_lines+3,column=g_tr_w-1)

bt5=Button(mainw,height=1,width=1,text='+',command=bt5Click)

def file_size_format(size_n1):

  i=0
  f1=0.0

  if size_n1<0 or size_n1>=100000:
      size_str2="****"
  elif size_n1>=10000 and size_n1<100000:
      i=int(size_n1/100);
      size_str2=str(i)
  elif size_n1>=1000 and size_n1<10000:
      i=int(size_n1/10);
      f1=i/10;
      size_str2=str(f1)
  elif size_n1<1000:
      f1=size_n1/100;
      size_str2=str(f1)

  #print('1-',size_str2)

  if len(size_str2)>4:
    size_str2=size_str2[0:3]
  #elif len(size_str2)<4:
  #  size_str2="    "

  #print('2-',size_str2)

  return size_str2
  
def trClick(event):

    global mu_play,mu_load,mu_pause,item_id0,item_cur,item_notclose,item_close,mainw,tr

    if item_close==1: #click [-]
      item_close=0
      
      if len(item_cur)>0:
          err=0
          
          try:
            text =tr.item(item_cur,'text')
          except:
            item_cur=''
            err=1
        
          if err==0:
            ol=[item_cur,]
            tr.selection_set(ol)
            
      print('close return')
      return

    if item_notclose==1: #click [+]
      #item_notclose=0
      
      print('open proccess')


    #print('focus'    ,tr.focus())
    #print('selection',tr.selection())

    item_dir  =''
    item_id0  =tr.selection()
    item_id1  =item_id0
    item_text =tr.item(item_id1,'text')
    
    if len(item_text)==0:
        return
        
    if item_text[0]=='<':
      item_text2=item_text.split('<',1)
      item_text3=item_text2[1]
      item_text4=item_text3.split('>',1)
      item_text5=item_text4[0]
    elif item_text[0]=='|':
      return
    else:
      item_text5=item_text
      
    item_dir=item_text5
    
    while 1:
      item_id2  =tr.parent(item_id1)
      
      if len(item_id2)==0:
        #item_text5=item_dir
        break
        
      item_text=tr.item(item_id2,'text')
      
      item_text2=item_text.split('<',1)
      item_text3=item_text2[1]
      item_text4=item_text3.split('>',1)
      item_text5=item_text4[0].upper()

      if item_text4[0]=='/':
        item_dir=item_text4[0]+item_dir
        break
      elif len(item_text5)>=2:
        if item_text5[0]>='C' and item_text5[0]<='Z' and item_text5[1]==':':
          item_dir=item_text5+item_dir
          break
        else:
          item_dir=item_text4[0]+'/'+item_dir
          item_id1=item_id2
      else:
        item_dir=item_text4[0]+'/'+item_dir
        item_id1=item_id2

    driver=0     
    if len(item_dir)==3:
        if item_dir[0]>='C' and item_dir[0]<='Z' and item_dir[1]==':' :
            driver=1

    if os.path.isdir(item_dir) or driver==1 :
        print(item_dir,driver)

        item_empt=1
        chld=tr.get_children(item_id0)
        item_open=tr.item(item_id0,'open')
        
        #print('item_open=',item_open)
        
        if item_open==False or item_notclose==1 :
        
          for o in chld:
              tr.delete(o)
         
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
                  tr.insert(item_id0, END, text='<'+files+'>', open=False)
            
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
                
                tr.insert(item_id0, END, text=files, open=True, values=info2 )

          if item_empt==1:
              tr.insert(item_id0, END, text='|'+'Empty Fold'+'|', open=True)

          item_notclose=0;
          
          tr.item(item_id0,open=True)

        else:

          tr.item(item_id0,open=False)
        
        if len(item_cur)>0:
          err=0
          
          try:
            text =tr.item(item_cur,'text')
          except:
            item_cur=''
            err=1
        
          if err==0:
            ol=[item_cur,]
            tr.selection_set(ol)

    else:
        event = pygame.event.Event(pygame.USEREVENT+2)
        pygame.event.post(event)
            
def trItemOpen(p):
  global item_notclose
  print('open')
  item_notclose=1
  
def trItemClose(p):
  global item_close
  print('close')
  item_close=1

def mpNext():

  global mu_load,mu_play,mu_pause,mu_pos,item_id0,item_cur,mainw,tr,bt3

  chld=[]
  id0=[]
  stop=0
  end=0
  next=0
  
  while 1:
    event = pygame.event.wait()
    
    print('event.type',event.type,'pg.User1',pygame.USEREVENT+1)
    
    if event.type == pygame.QUIT:
        return

    if event.type == pygame.USEREVENT+2 : #start to play

      id0=item_id0
      stop=0

      if pygame.mixer.music.get_busy() or mu_pause==1 :
        pygame.mixer.music.stop()

        bt3['text']='Play'     #dead lock
        mu_load=0
        mu_play=0
        stop=1
      
      item_id1  =tr.parent(id0)

      chld=tr.get_children(item_id1)
      step=0
      nextsong=''
      end=1

      for o in chld:

        next=0

        if step==0:
            for o2 in id0:
                if o==o2:
                    step=1
                    end =0

        if step==1:
            mydir   =''
            item_cur=o
            o3      =o

            try:
                item_text =tr.item(o3,'text')
            except:
                break
            
            if len(item_text)==0: 
                break

            if item_text[0]=='<':
              item_text2=item_text.split('<',1)
              item_text3=item_text2[1]
              item_text4=item_text3.split('>',1)
              mydir=item_text4[0]
              break
            elif item_text[0]=='|':
              mydir=item_text
              break
            else:
              mydir=item_text

            while 1:
              item_id2  =tr.parent(o3)
              
              if len(item_id2)==0:
                  item_text5=mydir
                  break
                  
              item_text=tr.item(item_id2,'text')
              
              item_text2=item_text.split('<',1)
              item_text3=item_text2[1]
              item_text4=item_text3.split('>',1)
              item_text5=item_text4[0].upper()

              if item_text4[0]=='/':
                  mydir=item_text4[0]+mydir
                  break
              elif len(item_text5)>=2:
                  if item_text5[0]>='C' and item_text5[0]<='Z' and item_text5[1]==':':
                    mydir=item_text5+mydir
                    break
                  else:
                    mydir=item_text4[0]+'/'+mydir
                    o3=item_id2
              else:
                  mydir=item_text4[0]+'/'+mydir
                  o3=item_id2

            print('mydir',mydir)
            
            item_dir2=mydir.split('.',-1)
            item_dir2[-1]=item_dir2[-1].lower()
            if item_dir2[-1]=='mp3':

                try:
                    pygame.mixer.init()
                    pygame.mixer.music.load(mydir)
                    pygame.mixer.music.play()
                except:
                    end=1
                    print('break1')
                    break;

                bt3['text']='Pause'
                mu_load=1
                mu_play=1
                mu_pos =0
                end=0

                ol=[o,]
                tr.selection_set(ol)

                mainw.title(mydir)
                
                pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)

                #vl=pygame.mixer.music.get_volume()
                #vl2=vl*100
                #probar2['value'] = vl2
                #mainw.update()
                
                step=2
                print('continue2')
                continue
            else:
                end=1
                print('break3')
                break
                
        if step==2:
            nextsong=o #calculate next song
            next=1
            print('break4')
            break

    if event.type == pygame.USEREVENT+1: #auto next
    
      if stop==1:
        stop=0
        continue

      if pygame.mixer.music.get_busy() or mu_pause==1 :
        pygame.mixer.music.stop()

        bt3['text']='Play'     #dead lock
        mu_load=0
        mu_play=0
        stop=1
                
      step=0
      id0=[nextsong,]
      nextsong=''
      end=1

      for o in chld:

        next=0

        if step==0:
            for o2 in id0:
                if o==o2:
                    step=1
                    end =0
            

        if step==1:
            mydir   =''
            item_cur=o
            o3      =o

            try:
                item_text =tr.item(o3,'text')
            except:
                break
            
            if len(item_text)==0:
                break

            if item_text[0]=='<':
              item_text2=item_text.split('<',1)
              item_text3=item_text2[1]
              item_text4=item_text3.split('>',1)
              mydir=item_text4[0]
            elif item_text[0]=='|':
              mydir=item_text
              break
            else:
              mydir=item_text

            while 1:
              item_id2  =tr.parent(o3)
              
              if len(item_id2)==0:
                  item_text5=mydir
                  break
                  
              item_text=tr.item(item_id2,'text')
              
              item_text2=item_text.split('<',1)
              item_text3=item_text2[1]
              item_text4=item_text3.split('>',1)
              item_text5=item_text4[0].upper()

              if item_text4[0]=='/':
                  mydir=item_text4[0]+mydir
                  break
              elif len(item_text5)>=2:
                  if item_text5[0]>='C' and item_text5[0]<='Z' and item_text5[1]==':':
                    mydir=item_text5+mydir
                    break
                  else:
                    mydir=item_text4[0]+'/'+mydir
                    o3=item_id2
              else:
                  mydir=item_text4[0]+'/'+mydir
                  o3=item_id2

            item_dir2=mydir.split('.',-1)
            item_dir2[-1]=item_dir2[-1].lower()
            if item_dir2[-1]=='mp3':

                try:
                    pygame.mixer.init()
                    pygame.mixer.music.load(mydir)
                    pygame.mixer.music.play()
                except:
                    end=1
                    print('break1')
                    break;

                bt3['text']='Pause'
                mu_load=1
                mu_play=1
                mu_pos =0
                end=0

                ol=[o,]
                tr.selection_set(ol)

                mainw.title(mydir)
                
                pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)

                #vl=pygame.mixer.music.get_volume()
                #vl2=vl*100
                #probar2['value'] = vl2
                #mainw.update()
                
                step=2
                print('continue2')
                continue
            else:
                end=1
                print('break3')
                break
                
        if step==2:
            nextsong=o  #calculate next song
            next=1
            print('break4')
            break
            
    if event.type == pygame.USEREVENT+3 : #display position
    
      if pygame.mixer.music.get_busy() :
        ps=mu_pos*1000+pygame.mixer.music.get_pos()
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
        lb1.config(text=ps5)

        #position seek bar
        if ps1<16*60 : # <16minues
            po1=(((ps1/(16*60))*g_pbar1)/(g_pbar1+g_pbar2+g_pbar3+g_pbar4))*10000
        elif ps1<32*60 : # <32minutes
            po1=((g_pbar1+((ps1-16*60)/(16*60))*g_pbar2)/(g_pbar1+g_pbar2+g_pbar3+g_pbar4))*10000
        elif ps1<64*60 : # <64minutes
            po1=((g_pbar1+g_pbar2+((ps1-32*60)/(32*60))*g_pbar3)/(g_pbar1+g_pbar2+g_pbar3+g_pbar4))*10000
        elif ps1<128*60 : # <128minutes
            po1=((g_pbar1+g_pbar2+g_pbar3+((ps1-64*60)/(64*60))*g_pbar4)/(g_pbar1+g_pbar2+g_pbar3+g_pbar4))*10000
        else :
            po1=10000
        
        if po1<0 :
            po1=0
        if po1>10000 :
            po1=10000
            
        probar1['value'] = po1
        mainw.update()
    
    if end==1 :
        bt3['text']='Play'     #dead lock
        mu_load=0
        mu_play=0
        end=0


def mainwClose():

    global mainw

    event = pygame.event.Event(pygame.QUIT)
    pygame.event.post(event)
    
    mainw.destroy()

def winResize(e):

    global mainw,bt3,g_bt_init,g_bt_step,g_bt_y1,g_bt_y2,g_bt_y3,g_bt_adj

    #print(e)

    width =e.width
    height=e.height
    
    #print("size",width,height)
    
    if e.x==0 and e.y==0 :

        if g_bt_init==0 :
            if g_bt_step==1 :
                g_bt_y2=height
            elif g_bt_step==2 :
                g_bt_y3=height

            g_bt_step=g_bt_step+1
            
            if g_bt_step>=3 :
                g_bt_init=1
                
                n1=g_bt_y2-g_bt_y3
                if n1>50 :      #its Windows
                    g_bt_adj=3
                else :          #its Ubuntu
                    g_bt_adj=0
                

        #print('y1=',g_bt_y1,'y2=',g_bt_y2,'y3=',g_bt_y3)
      
        if width>=112 and height>=18 :
            #btx=18*8
            #bty=height+19+g_bt_adj
            #bt1.place(x=btx,y=bty)

            btx=23*8
            bty=height+19+g_bt_adj
            bt2.place(x=btx,y=bty)

            btx=int(width/2)-7*8
            bty=height+19+g_bt_adj
            bt3.place(x=btx,y=bty)

            btx=width-25*8
            bty=height+19+g_bt_adj
            bt4.place(x=btx,y=bty)

            btx=width-4*8-3
            bty=height+19+g_bt_adj
            bt5.place(x=btx,y=bty)

            #btx=2*8
            #bty=height+19+g_bt_adj
            #lb1.place(x=btx,y=bty)

            btx=width-15*8
            bty=height+19+g_bt_adj+5
            lb2.place(x=btx,y=bty)

mainw.protocol("WM_DELETE_WINDOW", mainwClose)
mainw.bind('<Configure>', winResize)

tr.bind('<ButtonRelease-1>',trClick)
tr.bind('<<TreeviewOpen>>', trItemOpen)
tr.bind('<<TreeviewClose>>',trItemClose)

pygame.init()
pygame.mixer.music.set_volume(1.0)
pygame.time.set_timer(pygame.USEREVENT+3,500)

thr=Thread(target=mpNext)
thr.start()

mainw.mainloop()


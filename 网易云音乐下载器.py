import cloudmusic
from tkinter import *
from tkinter import messagebox
from selenium import webdriver
# 实现搜索打印到列表框
def get_music():
    music_list = cloudmusic.search(e1.get(),5)
    for music in music_list:
        if len(music.artist) == 1:
            artist = music.artist[0]
        else:
            artist = ""
            for ar in music.artist:
                artist += ar + " "
        music.name = music.name.replace('|', '')
        music.name = music.name.replace('/', '')
        music.name = music.name.replace('?', '')
        music.name = music.name.replace('*', '')
        music.name = music.name.replace('\\', '')
        music.name = music.name.replace('<', '')
        music.name = music.name.replace('>', '')
        music.name = music.name.replace(':', '')
        music.name = music.name.replace('"', '')
        music.name = music.name.replace('？', '')
        music.name = music.name.replace('：', '')
        name = music.name + " - " + artist + "." + music.type

        # print(f'歌曲名称:{name}\n歌手:{gehsou}')
        # print(f'音乐id:{Id}')
        # 文本框
        text.insert(END, '名称:{}'.format(name))
        text.insert(END, '歌手:{}'.format(artist))
        # text.insert(END,'id:{}'.format(Id))
        # 文本框滚动
        text.see(END)
        # 更新
        text.update()
# 列表下载
def downloadall():
    music_list = cloudmusic.search(e1.get(),5)
    for music in music_list:
        name = music.name
        Id = music.id
        musicid = cloudmusic.getMusic(Id)
        musicid.download(level='standard')
        messagebox.showinfo(message="{}下载成功".format(name))
# 单曲下载
def downloadone():
    music_list = cloudmusic.search(e1.get(),1)
    for i in music_list:
        Id = i.id
        name = i.name
        musicid = cloudmusic.getMusic(Id)
        musicid.download(level='standard')
        messagebox.showinfo(message="{}下载成功".format(name))
# 试听功能
def audition():
    music_list = cloudmusic.search(e1.get(),1)
    driver = webdriver.Chrome(r'C:\Users\Desk\chromedriver.exe')
    driver.get(music_list[0].url)
# 主窗口
root = Tk()
root.title('阿琨音乐下载器')
root.geometry('400x450')
# tktable = Button(root,text='搜索',fg='blue',command=get_music)
# tktable.pack()
Label(root,text='输入歌曲名称:').grid(row=0,column=0)
# Label(root,text='作者').grid(row=1,column=0)
e1 = Entry(root)
e1.grid(row=0,column=1,padx=10,pady=5)
text = Listbox(root,width=35,heigh=20)
# text.bind('<Double-Button-1>',downloadone)
text.grid(row=1,columnspan=2)
Button(root,text='搜索',width=10,command=get_music).grid(row=3,column=0,sticky=W,padx=10,pady=5)
button1 = Button(root,text='退出',width=10,command=root.quit)
button1.grid(row=3,column=1,sticky=E,padx=10,pady=5)
# Button(root,text='单曲下载',width=10)\
#     .grid(row=2,column=0,sticky=E,padx=100,pady=100)
button2 = Button(root,text="列表下载",width="8",bd=3,command=downloadall).place(relx=0.8,rely=0.4,relheight=0.08)
button3 = Button(root,text="试听",width="8",bd=3,command=audition).place(relx=0.8,rely=0.6,relheight=0.08)
button4 = Button(root,text="单曲下载",width="8",bd=3,command=downloadone).place(relx=0.8,rely=0.2,relheight=0.08)
root.mainloop()




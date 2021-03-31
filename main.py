import gi
import os
import os.path
from fetch import theme
from fetch import icon
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from random import sample
   
class MainWindow(Gtk.Window):

    
    

    def __init__(self):

        global iconcombo,shellcombo,themecombo,switch1
        

        #########################################################
        #                  MAIN WINDOW CONFIG
        #########################################################
        Gtk.Window.__init__(self)
        self.set_title("Gnome theme")
        self.set_border_width(30)
        self.set_position(Gtk.WindowPosition.CENTER)

        #################### LIST BOX ###########################
        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.add(listbox)

        #########################################################
        #                       ROW - 1
        #########################################################


        row_1 = Gtk.ListBoxRow()
        box_1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        box_1.set_border_width(20)
        box_1.set_spacing(100)
        
        row_1.add(box_1)

        ####################### WIDGET #########################
        label = Gtk.Label()
        label.set_markup("<b>Theme</b>")

        themecombo = Gtk.ComboBoxText()
        themecombo.set_size_request(170,0)
        
        for item in theme:
            themecombo.append_text(item)
         
         
        
        box_1.pack_start(label, True, False, 0)

        box_1.pack_start(themecombo, True, False, 0)

        listbox.add(row_1)

        #########################################################
        #                       ROW - 2
        #########################################################

        row_2 = Gtk.ListBoxRow()
        box_2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        box_2.set_spacing(90)
        box_2.set_border_width(33)
        row_2.add(box_2)

        ####################### WIDGET #########################

        label2 = Gtk.Label()
        label2.set_markup("<b>Shell Theme</b>")

        shellcombo = Gtk.ComboBoxText()
        shellcombo.set_size_request(170,0)
        
        for  item in theme:
            shellcombo.append_text(item)
        

        box_2.pack_start(label2, True, False, 0)

        box_2.pack_start(shellcombo, True, False, 0)

        listbox.add(row_2)

       
        
        #########################################################
        #                       ROW - 3
        #########################################################

        row_3 = Gtk.ListBoxRow()
        box_3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        box_3.set_spacing(90)
        box_3.set_border_width(8)
        row_3.add(box_3)

        ####################### WIDGET #########################

        label3 = Gtk.Label()
        label3.set_markup("<b>Icon</b>")

        iconcombo = Gtk.ComboBoxText()
        iconcombo.set_size_request(170,0)
        
        for  item in icon:
            iconcombo.append_text(item)
            
    

        box_3.pack_start(label3, True, False, 0)

        box_3.pack_start(iconcombo, True, False, 0)

        listbox.add(row_3)
        
        #########################################################
        #                       ROW - 4
        #########################################################

        row_4 = Gtk.ListBoxRow()
        box_4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        box_4.set_spacing(60)
        box_4.set_border_width(32)
        row_4.add(box_4)

        ####################### WIDGET #########################

        label4= Gtk.Label()
        label4.set_markup("<b>Random Wallpaper</b>")
        switch1 = Gtk.Switch()
        box_4.pack_start(label4, True, False, 0)
        box_4.pack_start(switch1, True, False, 0)

        listbox.add(row_4)
        
        
        #########################################################
        #                       ROW - 5A
        #########################################################
        row_5a = Gtk.ListBoxRow()
        box_5a = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        box_5a.set_spacing(0)
        box_5a.set_border_width(2)
        row_5a.add(box_5a)
        
        ####################### WIDGET #########################
        
        info = Gtk.Label(label="Move your downloaded themes,icon,wallpaper and extract if ziped into respected sub directory of gnome-theme located in your home directory")
        info.set_line_wrap(True)
        info.set_max_width_chars(35)
        
        box_5a.pack_start(info, True, False, 0)
        
        listbox.add(row_5a)
        
        #########################################################
        #                       ROW - 5
        #########################################################
        row_5 = Gtk.ListBoxRow()
        box_5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        box_5.set_spacing(50)
        box_5.set_border_width(32)
        row_5.add(box_5)
        
        ####################### WIDGET #########################

        submit = Gtk.Button.new_with_label("Apply")
        submit.connect("clicked",self.on_click_me_clicked)
        
        box_5.pack_start(submit, True, False, 0)
        
        listbox.add(row_5)
        
    def on_click_me_clicked(self, button):
        
        #################################################################################################################
        #                                       CREATE DIR EXISTANCE , CREATE AND SYMLINK
        ##################################################################################################################
        ##### get current path ######
        print(os.getcwd())

        ###################################
        #  set dir to home 
        ###################################
        HOME = os.getenv("HOME")
        os.chdir(HOME)

        ###################################
        # check and create gnome-theme dir             ##------ MAIN DIR--------##
        ###################################

        foldern0 = "gnome-theme"
        flag1 = os.path.isdir(foldern0)
        if not flag1:
            os.makedirs(foldern0)
            print('folder themes created')
        else:
            print('dir gnome-theme exists')

        os.chdir(foldern0)
        print(os.getcwd())

        ###################################
        #   check and create themes dir                ##------ SUB THEMES DIR--------##
        ###################################



        foldern1 = "themes"
        themepath = HOME+'/'+foldern0
        themesys =  "/usr/share/themes"
        flag2 = os.path.isdir(foldern1)
        cmd = "ln -s"+" "+themesys+" "+ themepath

        if not flag2:
            os.system(cmd)
            print('folder theme created')
        else:
            print(' theme dir exists')

        print(cmd)

        ###################################
        #   check and create themes icon              ##------ SUB ICON DIR--------##
        ###################################
        foldern2 = "icons"
        iconpath = HOME+'/'+foldern0
        iconsys = "/usr/share/icons"
        flag3 = os.path.isdir(foldern2)
        cmd1 = "ln -s"+" "+iconsys+" "+iconpath

        if not flag3:
            os.system(cmd1)
            print('folder icon created')
        else:
            print('icons dir exists')

        print(cmd1)


        ###################################
        #  check and create wallpaper dir             ##------ SUB wallpaper DIR--------##
        ###################################

        foldern3 = "wallpapers"
        flag4 = os.path.isdir(foldern3)

        if not flag4:
            os.makedirs(foldern3)
            print('created wallpaper folder ')
        else:
            print(" wall dir exits")
        #############################################################
        #         FETCH THE DATA AND APPEND IT TO AN ARRAY
        ############################################################
        theme = os.listdir(foldern1)

        print(theme)


        icon = os.listdir(foldern2)

        print(icon)

        ###############################################################################********************######################################################################
        
        ############################################################################ 
        #               SETTING APPLICATION THEME
        ############################################################################ 
        themeval = (themecombo.get_active_text())
        themecmd = '''dconf write /org/gnome/desktop/interface/gtk-theme "'{}'" '''.format(themeval)
        if themecombo.get_active_text() == None:
             print("!do select some option")
        else:
          os.system(themecmd)   
        ############################################################################ 
        #               SETTING SHELL THEME
        ############################################################################   
        shellval = (shellcombo.get_active_text())
        shellcmd =  '''dconf write /org/gnome/shell/extensions/user-theme/name "'{}'" '''.format(shellval)
        if themecombo.get_active_text() == None:
             print("!do select some option")
        else:
          os.system(shellcmd)  
        ############################################################################ 
        #              SETTING ICON THEME
        ############################################################################   
        iconval = (iconcombo.get_active_text())
        iconcmd = '''dconf write /org/gnome/desktop/interface/icon-theme "'{}'" '''.format(iconval)
        if themecombo.get_active_text() == None:
             print("!do select some option")
        else:
          os.system(iconcmd)
        ############################################################################ 
        #              RANDOM WALLPAPER
        ############################################################################ 
        
        waldir = HOME+"/gnome-theme/wallpapers"
        
        if switch1.get_active() == False:
            print("switch is off ugh")
        else:
            walist = os.listdir(waldir)
            wallpaper = sample(walist,1)
            print(wallpaper[0])
            walcmd = '''gsettings set org.gnome.desktop.background picture-uri "'file://'''+HOME+"/gnome-theme/wallpapers"+'/'+wallpaper[0]+'\'"'
            os.system(walcmd)
            
            
window = MainWindow()

window.connect("delete-event", Gtk.main_quit)

window.show_all()


Gtk.main()








import os
import os.path

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
wallpath = HOME+'/'+foldern0
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


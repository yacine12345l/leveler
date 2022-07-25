"""
#------# League of Legends Folder Location #------#

Location of your league of legends folder.

DEFAULT = 'C:\\Riot Games\\League of Legends\\'
"""

lol_folder_location = 'C:\\Riot Games\\League of Legends\\'

"""
#------# USE RECYCLED NICKNAMES #------#

Riot Games doesnt clear nicknames after perma ban.
It means, that nick might be banned forever.
Their api doesn't  allow to check if nick is banned or just was used and changed.
If you set this to true, you might crash a bot, when creating an accout.

DEFAULT = False
"""
use_recycled_nicknames = False

"""
#------# NICK NAMES PARTIALS #------#

Set how many partials will be used to generate nick.
More partials = more strange nick.
Do not set 1, these nick are 100% already taken.
You can try 3-4, but i strongly recommend you to do not change it.

Also use account-creator/nickPartialsAdder.py to add more possibilities to nick generator.
The best you can do is do it from scratch....

DEFAULT = 2
"""
nickname_partials = 2
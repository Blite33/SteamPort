
"""
Welcome to SteamPort!
The code comments will guide you through the purpose of each line.
This is another version of the code which was found on the website:
#def copytree(src, dst, symlinks=False, ignore=None):
#    for item in os.listdir(src):
#        s = os.path.join(src, item)
#        d = os.path.join(dst, item)
#        if os.path.isdir(s):
#            shutil.copytree(s, d, symlinks, ignore)
#        else:
#            shutil.copy2(s, d)
For the link and credit to the code, go to:
https://stackoverflow.com/questions/1868714/how-do-i-copy-an-entire-directory-of-files-into-an-existing-directory-using-pyth
"""

build = 75

unsuccessfull_builds = 24

unsuccessfull_builds_beta = 4

unsuccessfull = False

beta = False

demo = False

fork_build = 28

fork = 4

console_skin = "% done, transferred"
cns = console_skin


# Imports:
import shutil, os

def copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                shutil.copy2(s, d)

#soc = input("source: ")
soc = r'D:\\SteamLibrary\\'

#des = input("destination: ")
des= r'S:\\SteamLibrary\\'

def copydir(soc, des, file, percent, cns):
    if os.path.exists(soc + file) == True:
        copytree(soc + file, des + file)
        print(percent, cns, file)
    else:
        print("Some files seem to be missing from your steam library including the ", file, " folder. Continuing transfer.")

def copyfile(soc, dec, file, percent, cns):
    if os.path.isfile(soc + file) == True:
        shutil.copy2(soc + file, des)
        print(percent, cns, file)
    else:
        print("Some files seem to be missing from your steam library including: ", file, ". Continuing transfer.")

copydir(soc, des, r'appcache', "11", cns)

copydir(soc, des, r'bin', "30", cns)

copydir(soc, des, r'clientui', "31", cns)

copydir(soc, des, r'config', "32", cns)

copydir(soc, des, r'controller_base', "34", cns)

copydir(soc, des, r'dumps', "35", cns)

copydir(soc, des, r'friends', "35.3", cns)

copydir(soc, des, r'graphics', "36", cns)

copydir(soc, des, r'html5app', "36.1", cns)

copydir(soc, des, r'logs', "36.3", cns)

copydir(soc, des, r'music', "36.4", cns)

copydir(soc, des, r'package', "46", cns)

copydir(soc, des, r'public', "47", cns)

copydir(soc, des, r'resource', "47.2", cns)

copydir(soc, des, r'servers', "47.22", cns)

copydir(soc, des, r'skins', "47.24", cns)

copydir(soc, des, r'steam', "47.24", cns)

copydir(soc, des, r'steamui', "47.34", cns)

copydir(soc, des, r'tenfoot', "70", cns)

copydir(soc, des, r'userdata', "78", cns)

copyfile(soc, des, r'.crash', "78", cns)

copyfile(soc, des, r'ClientRegistry.blob', "78", cns)

copyfile(soc, des, r'crashhandler.dll', "78", cns)

copyfile(soc, des, r'crashhandler64.dll', "78", cns)

copyfile(soc, des, r'CSERHelper.dll', "78", cns)

copyfile(soc, des, r'd3dcompiler_46.dll', "78", cns)

copyfile(soc, des, r'd3dcompiler_46_64.dll', "78", cns)

copyfile(soc, des, r'fossilize_engine_filters.json', "78", cns)

copyfile(soc, des, r'GameOverlayRenderer.dll', "78", cns)

copyfile(soc, des, r'GameOverlayRenderer64.dll', "78", cns)

copyfile(soc, des, r'GameOverlayUI.exe', "78", cns)

copyfile(soc, des, r'GfnRuntimeSdk.dll', "78", cns)

copyfile(soc, des, r'icui18n.dll', "78", cns)

copyfile(soc, des, r'icuuc.dll', "78", cns)

copyfile(soc, des, r'libavcodec-57.dll', "78", cns)

copyfile(soc, des, r'libavformat-57.dll', "78", cns)

copyfile(soc, des, r'libavresample-3.dll', "78", cns)

copyfile(soc, des, r'libavutil-55.dll', "78", cns)

copyfile(soc, des, r'libfreetype-6.dll', "78", cns)

copyfile(soc, des, r'libswscale-4.dll', "78", cns)

copyfile(soc, des, r'libx264-142.dll', "78", cns)

copyfile(soc, des, r'libx264-142.dll.crypt', "78", cns)

copyfile(soc, des, r'libx264-142.dll.md5', "78", cns)

copyfile(soc, des, r'openvr_api.dll', "78", cns)

copyfile(soc, des, r'SDL2.dll', "78", cns)

copyfile(soc, des, r'ssfn35751201823239953', "78", cns)

copyfile(soc, des, r'ssfn6185694093012287183', "78", cns)

copyfile(soc, des, r'steam.dll', "78", cns)

copyfile(soc, des, r'steam.exe', "78", cns)

copyfile(soc, des, r'Steam2.dll', "78", cns)

copyfile(soc, des, r'steam.signatures', "78", cns)

copyfile(soc, des, r'steamclient.dll', "78", cns)

copyfile(soc, des, r'steamclient64.dll', "78", cns)

copyfile(soc, des, r'steamerrorreporter.exe', "78", cns)

copyfile(soc, des, r'steamerrorreporter64.exe', "78", cns)

copyfile(soc, des, r'SteamFossilizeVulkanLayer.json', "78", cns)

copyfile(soc, des, r'SteamFossilizeVulkanLayer64.json', "78", cns)

copyfile(soc, des, r'SteamOverlayVulkanLayer.dll', "78", cns)

copyfile(soc, des, r'SteamOverlayVulkanLayer.json', "78", cns)

copyfile(soc, des, r'SteamOverlayVulkanLayer64.dll', "78", cns)

copyfile(soc, des, r'SteamOverlayVulkanLayer64.json', "78", cns)

copyfile(soc, des, r'SteamUI.dll', "78", cns)

copyfile(soc, des, r'steamwebrtc.dll', "78", cns)

copyfile(soc, des, r'streaming_client.exe', "78", cns)

copyfile(soc, des, r'ThirdPartyLegalNotices.css', "78", cns)

copyfile(soc, des, r'ThirdPartyLegalNotices.doc', "78", cns)

copyfile(soc, des, r'ThirdPartyLegalNotices.html', "78", cns)

copyfile(soc, des, r'tier0_s.dll', "78", cns)

copyfile(soc, des, r'tier0_s64.dll', "78", cns)

copyfile(soc, des, r'v8.dll', "78", cns)

copyfile(soc, des, r'video.dll', "78", cns)

copyfile(soc, des, r'VkLayer_steam_fossilize.dll', "78", cns)

copyfile(soc, des, r'VkLayer_steam_fossilize64.dll', "78", cns)

copyfile(soc, des, r'vstdlib_s.dll', "78", cns)

copyfile(soc, des, r'vstdlib_s64.dll', "78", cns)

copyfile(soc, des, r'WriteMiniDump.exe', "78", cns)


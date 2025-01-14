import demoji

#The demoji module also requires an initial download of data from the Unicode Consotium's emoji code repository as the emoji list itself is frequently updated and changed
# demoji.download_codes()
emoji_list = """This python program course is awesome 😂😋😚😶🙄🤩😴😇🤢🤪🤑😭"""
print(demoji.findall(emoji_list))

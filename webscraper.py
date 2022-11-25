import urllib.request
from pprint import pprint

def getSongTitles(): 
        fp = urllib.request.urlopen("INSERT_LINK") #IMPORTANT: insert the link to the billboard chart you would like to retrieve songs from where it says INSERT_LINK. For example: https://www.billboard.com/charts/hot-100/2022-10-15/
        mybytes = fp.read() 

        mystr = mybytes.decode("utf8") 
        fp.close() 

        lines = mystr.split('\n') 

        songTitles = [] 

        for i in range(len(lines)): 
            if '"title-of-a-story" class="c-title' in lines[i] and 'u-max-width-230@tablet-only' in lines[i]: 
                songTitle = lines[i + 5].strip() 
                songTitles.append(songTitle) 

        for j in range(0, len(songTitles), 1):
            curr = songTitles[j]
            if("'" in curr):
                curr.replace("'", "")

        return songTitles 

def main():
    f = open("INSERT_FILE", "w") #IMPORTANT: insert the name of the text file you would like to write in where it says INSERT_FILE
    songTitles = getSongTitles() 
    for i in range(len(songTitles)):
        f.write(songTitles[i] + "\n")
    f.close()
    
main()

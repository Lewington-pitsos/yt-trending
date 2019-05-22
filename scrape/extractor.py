import os

class Extractor():
    def __init__(self):
        self.logPath = "/home/lewington/code/scrapers/yt-trending/logs/"
        self.writeFileName = "/home/lewington/code/scrapers/yt-trending/titles.txt"
    
    def allTitles(self):
        allTitles = []
        allLogs = os.listdir(self.logPath)
        for filename in allLogs:
            log = open(os.path.join(self.logPath + filename), "r")
            allTitles += self.titlesFromLog(log)

        self.saveDistinctTitles(allTitles)

    def titlesFromLog(self, log):
        logTitles = []
        for logLine in log:
            if "saving video" in logLine:
                logTitles.append(logLine.rstrip("\n")[14:])
        log.close()
        return logTitles

    def saveDistinctTitles(self, titles):
        distinctTitles = list(dict.fromkeys(titles))
        titleFile = open(self.writeFileName, "w")
        for title in distinctTitles:
            titleFile.write(title + "\n")
        
        titleFile.close()






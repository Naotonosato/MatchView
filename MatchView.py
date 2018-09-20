from kivy.uix.recycleview import RecycleView
from kivy.app import App

class MatchView(RecycleView):

    def __init__(self,**kwargs):
        super(MatchView,self).__init__(**kwargs)

        self.titles     = ['aiueo','kakikukeko','tyuukannsikennyada','marasonnkirai']
        self.match_data = {}

    def match(self,word):

        self.match_data = {}
        
        for title in self.titles:
            i = 0
            if title.find(word) >= 0:
                if not self.match_data.get(word):
                    self.match_data[word] = {}
                if not self.match_data[word].get(title):
                    self.match_data[word][title] = {title:[]}
                while True:
                    index = title.find(word,i)
                    if index >= 0:
                        i += index+len(word)
                        self.match_data[word][title][title].append(index)
                    else:
                        break

        self.data=[]
        for w in self.match_data:
            for t in self.match_data[w]:
                indexes = self.match_data[w][t][t][::-1]
                for i in indexes:
                    t = t[:i]+'[color=#AAAAAA]'+w+'[/color]'+t[i+len(w):]
      
                self.data.append({'text':t,'color':(0,0,0,0.2),'markup':True})


class MatchViewApp(App):
    pass

if __name__ == '__main__':

    MatchViewApp().run()
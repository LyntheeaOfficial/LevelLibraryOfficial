from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window


# define our different screens
class Opening(Screen):
    pass


class LibraryMenu(Screen):
    pass


class AskTheLibrarian(Screen):
    def clear(self):
        self.ids.test2.text = self.ids.test.text + "\n\nIn the prototype version, \nthe Level Library will only print your responses back to you."
        self.ids.test.text = ""


class ResearchSummary(Screen):
    def clear(self):
        self.ids.test2.text = "Source Summary… \nThe prototype version does not generate an official summary of your sources \n\n\"At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.\""
        self.ids.test.text = ""


class LearningCenter(Screen):
    def clear(self):
        # player = VideoPlayer(source="video-out.mp4", state="play", options={"eos": "loop"})
        self.ids.test2.text = "CC: \"Right now, the Level Library prototype only houses a demonstration of what would happen when a topic to learn about is searched on the page."
        self.ids.test.text = ""
        self.ids.rawr.source = "e102prototypevideo.mp4"
        # return player


class MoreAbtLL(Screen):
    pass


class AboutUs(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('whatever.kv')


class LevelLibraryApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return kv


if __name__ == "__main__":
    LevelLibraryApp().run()

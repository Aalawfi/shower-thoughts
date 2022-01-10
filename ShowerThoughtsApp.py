import kivy 
from kivy.app import App
# TODO: FLoatLayout or GridLayout ? 
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty
from kivy.graphics import Rectangle
from kivy.uix.textinput import TextInput, FL_IS_LINEBREAK
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput


class MyTextInput(TextInput):
    minimum_width = NumericProperty(0)
    def _split_smart(self, text):
        # modified to always split on newline only
        lines = text.split(u'\n')
        lines_flags = [0] + [FL_IS_LINEBREAK] * (len(lines) - 1)
        return lines, lines_flags

    def _refresh_text(self, text, *largs):
        # this is modified slightly just to calculate minimum_width

        # Refresh all the lines from a new text.
        # By using cache in internal functions, this method should be fast.
        mode = 'all'
        if len(largs) > 1:
            mode, start, finish, _lines, _lines_flags, len_lines = largs
            # start = max(0, start)
            cursor = None
        else:
            cursor = self.cursor_index()
            _lines, self._lines_flags = self._split_smart(text)
        _lines_labels = []
        _line_rects = []
        _create_label = self._create_line_label

        # calculate minimum width
        min_width = 0
        for x in _lines:
            lbl = _create_label(x)
            min_width = max(min_width, lbl.width)
            _lines_labels.append(lbl)
            _line_rects.append(Rectangle(size=lbl.size))
        self.minimum_width = min_width + self.padding[0] + self.padding[2]

        if mode == 'all':
            self._lines_labels = _lines_labels
            self._lines_rects = _line_rects
            self._lines = _lines
        elif mode == 'del':
            if finish > start:
                self._insert_lines(start,
                                   finish if start == finish else (finish + 1),
                                   len_lines, _lines_flags,
                                   _lines, _lines_labels, _line_rects)
        elif mode == 'insert':
            self._insert_lines(
                start,
                finish if (start == finish and not len_lines)
                else (finish + 1),
                len_lines, _lines_flags, _lines, _lines_labels,
                _line_rects)

        min_line_ht = self._label_cached.get_extents('_')[1]
        # with markup texture can be of height `1`
        self.line_height = max(_lines_labels[0].height, min_line_ht)
        # self.line_spacing = 2
        # now, if the text change, maybe the cursor is not at the same place as
        # before. so, try to set the cursor on the good place
        row = self.cursor_row
        self.cursor = self.get_cursor_from_index(self.cursor_index()
                                                 if cursor is None else cursor)
        # if we back to a new line, reset the scroll, otherwise, the effect is
        # ugly
        if self.cursor_row != row:
            self.scroll_x = 0
        # with the new text don't forget to update graphics again
        self._trigger_update_graphics()

    def on_text(self, *args):
        # added to update minimum width on each change
        cc, cr = self.cursor
        text = self._lines[cr]
        lbl = self._create_line_label(text)
        self.minimum_width = max(self.minimum_width, lbl.width + self.padding[0] + self.padding[2])

class Layout (GridLayout):
    first_name = ObjectProperty(None)
    last_name = ObjectProperty(None)
    phone_number = ObjectProperty(None)
    def __init__(self, **kwargs): 
        super(Layout, self).__init__(**kwargs)

    def generate(self): 
        print("first name: ", self.first_name.text, "last name: ", self.last_name.text,
         "phone number: ", self.phone_number.text)
         #TODO: JSONify the above info 
         #TODO send the JSON to back end

class ShowerThoughtsApp(App):
   def build(self):
       return Layout()
if __name__ == '__main__':
     ShowerThoughtsApp().run()
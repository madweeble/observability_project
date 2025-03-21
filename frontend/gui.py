from tkinter import *
import requests

THEME_COLOUR = '#375362'


class Interface:
    def __init__(self):
        self.window = Tk()
        self.window.title('GUI Window')
        self.window.config(padx=20, pady=20, bg=THEME_COLOUR)
        self.window.minsize(width=500, height=300)

        self.my_label = Label(text='Title', bg=THEME_COLOUR, fg='white', font=('Arial', 24))
        self.my_label.pack()

        # create 2 rows
        self.row0 = Frame(self.window, bg=THEME_COLOUR)
        self.row0.pack(side=TOP, fill=Y, padx=10, pady=10, anchor=NE)
        self.row1 = Frame(self.window, bg=THEME_COLOUR)
        self.row1.pack(side=TOP, fill=Y, padx=10, pady=10, anchor=NE)
        self.row2 = Frame(self.window, bg=THEME_COLOUR)
        self.row2.pack(side=RIGHT, fill=Y, padx=10, pady=10, anchor=SE)

        # add 2 labels
        self.term_title = Label(self.row0, text='Term', bg=THEME_COLOUR, fg='white', font=('Arial', 16, 'bold'))
        self.term_title.pack(side=LEFT)
        self.intent_title = Label(self.row1, text='Intent', bg=THEME_COLOUR, fg='white', font=('Arial', 16, 'bold'))
        self.intent_title.pack(side=LEFT)

        # add 2 entry boxes
        self.term_textbox = Entry(self.row0, width=40)
        self.term_textbox.pack(side=RIGHT, padx=10)
        self.intent_textbox = Entry(self.row1, width=40)
        self.intent_textbox.pack(side=RIGHT, padx=10)

        self.button = Button(self.row2, text='Submit', command=self.button_clicked)
        self.button.pack(side=RIGHT)

    def run(self):
        self.window.mainloop()

    def button_clicked(self):
        print('submitted')
        term = self.term_textbox.get()
        intent = self.intent_textbox.get()
        print(f'term: {term}, intent: {intent}')

        # Call the create_item API
        api_url = 'http://localhost:8888/text/'
        data = {'term': term, 'intent': intent}
        try:
            response = requests.post(api_url, json=data)
            if response.status_code == 200:
                print('Item created successfully!')
                print('Response:', response.json())
            else:
                print('Error creating item:', response.text)
        except requests.exceptions.RequestException as e:
            print('Error:', e)
            print('Confirm that the FastAPI server is running.')


if __name__ == '__main__':
    interface = Interface()
    interface.run()

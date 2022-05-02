import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import json


class Catalogue(App):

    def build(self):

        return MyGridLayout()


class MyGridLayout(GridLayout):
    def press(self, instance):
        product = self.product.text
        description = self.description.text
        price = self.price.text

        print(product)
        print(description)
        print(price)
        with open('data.json') as f:
            data = json.load(f)
        with open('new_file.json', 'w') as f:
            json.dump(data, f, indent=2)
            out_file = open("myfile.json", "w")
            json.dump(product, out_file, indent=2, sort_keys=True)
            json.dump(description, out_file, indent=2, sort_keys=True)
            json.dump(price, out_file, indent=2, sort_keys=True)
            out_file.close()
            print("New json file is created from data.json file")

        self.product.text = ""
        self.description.text = ""
        self.price.text = ""

        # wb = load_workbook("Cathalogue.xlsx")
        # ws = wb.active
        # counter = ws.cell(7, 18).value
        # column = ws.cell(7, 19).value
        # print("counter is", counter)
        # print("column is", column)
        # ws.cell(column, 1, name)
        # ws.cell(column, 2, description)
        # ws.cell(column, 3, price)
        # counter = counter+1
        # column = column + 1
        # ws.cell(7, 18, counter)
        # ws.cell(7, 19, column)
        # wb.save("Catalogo.xlsx")

    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 1
        self.top_grid = GridLayout()
        self.top_grid.cols = 2
        # product
        self.add_widget(self.top_grid)
        self.top_grid.add_widget(Label(text="Producto", font_size=40))
        self.product = TextInput(multiline=True)
        self.top_grid.add_widget(self.product)
        # description
        self.top_grid.add_widget(Label(text="Descripción", font_size=40))
        self.description = TextInput(multiline=True)
        self.top_grid.add_widget(self.description)
        # price
        self.top_grid.add_widget(Label(text="Precio", font_size=40))
        self.price = TextInput(multiline=True)
        self.top_grid.add_widget(self.price)
        # submit button
        self.submit = Button(text="Enviar", height=30)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)


if __name__ == '__main__':
    Catalogue().run()

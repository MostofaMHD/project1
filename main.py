from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from PIL import Image as PilImage
from kivy.core.image import Image as CoreImage
import random


class SnakeWaterGunApp(App):
    def __init__(self):
        super().__init__()
        self.balance = 6000

    def play_game(self, user_choice):
        options = ["Snake", "Water", "Gun"]
        comp_choice = random.choice(options)

        money = [50, 100, 200, 300, 500, 999, 1000, 10000, 2000, 12000, 5000]
        prize_money = random.choice(money)

        result = ""
        if user_choice == comp_choice:
            result = "It's a draw!"
        elif (
            (user_choice == "Snake" and comp_choice == "Water")
            or (user_choice == "Water" and comp_choice == "Gun")
            or (user_choice == "Gun" and comp_choice == "Snake")
        ):
            result = f"You Win {prize_money}!"
            self.balance += prize_money
        else:
            result = f"You Lose! Deducting 2000 from balance."
            self.balance -= 2000

        self.feeling_label.text = result
        self.balance_label.text = f"Balance: {self.balance}"

        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=f"Computer chose {comp_choice}\n{result}\nBalance: {self.balance}"))

        popup = Popup(title='Game Result', content=content, size_hint=(None, None), size=(400, 200))
        popup.open()

        if self.balance <= 0:
            content = BoxLayout(orientation='vertical')
            content.add_widget(Label(text="Balance has reached 0. Game Over!"))

            popup = Popup(title='Game Over', content=content, size_hint=(None, None), size=(300, 150))
            popup.open()

    def on_button_click(self, choice):
        self.play_game(choice)

    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Load the background image
        background_image_path = "image.jpeg"
        background_image = PilImage.open(background_image_path)
        background_image.save("temp.png")  # Kivy requires saving the image first
        background_photo = CoreImage("temp.png")

        # Set the background image
        background_label = Image(source="temp.png", allow_stretch=True)
        layout.add_widget(background_label)

        # Create labels for feeling and balance at the top
        self.feeling_label = Label(text="Feeling: Ready to Play!")
        layout.add_widget(self.feeling_label)

        self.balance_label = Label(text=f"Balance: {self.balance}")
        layout.add_widget(self.balance_label)

        # Create buttons for user choices at the bottom
        snake_button = Button(text="Snake", on_press=lambda x: self.on_button_click("Snake"))
        layout.add_widget(snake_button)

        water_button = Button(text="Water", on_press=lambda x: self.on_button_click("Water"))
        layout.add_widget(water_button)

        gun_button = Button(text="Gun", on_press=lambda x: self.on_button_click("Gun"))
        layout.add_widget(gun_button)

        return layout


if __name__ == '__main__':
    SnakeWaterGunApp().run()
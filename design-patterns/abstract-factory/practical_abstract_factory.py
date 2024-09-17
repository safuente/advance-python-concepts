from abc import ABC, abstractmethod


# Abstract Product Interfaces

class Button(ABC):
    @abstractmethod
    def click(self) -> str:
        pass


class Checkbox(ABC):
    @abstractmethod
    def check(self) -> str:
        pass


# Concrete Product Implementations for the Light Theme

class LightButton(Button):
    def click(self) -> str:
        return "Light Button clicked!"


class LightCheckbox(Checkbox):
    def check(self) -> str:
        return "Light Checkbox checked!"


# Concrete Product Implementations for the Dark Theme

class DarkButton(Button):
    def click(self) -> str:
        return "Dark Button clicked!"


class DarkCheckbox(Checkbox):
    def check(self) -> str:
        return "Dark Checkbox checked!"


# Abstract Factory Interface

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


# Concrete Factory for the Light Theme

class LightThemeFactory(GUIFactory):
    def create_button(self) -> Button:
        return LightButton()

    def create_checkbox(self) -> Checkbox:
        return LightCheckbox()


# Concrete Factory for the Dark Theme

class DarkThemeFactory(GUIFactory):
    def create_button(self) -> Button:
        return DarkButton()

    def create_checkbox(self) -> Checkbox:
        return DarkCheckbox()


# Client Code that Uses the Abstract Factory

def client_code(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    print(button.click())
    print(checkbox.check())


if __name__ == "__main__":
    theme = input("Choose theme (light/dark): ").lower()

    if theme == "light":
        factory = LightThemeFactory()
    elif theme == "dark":
        factory = DarkThemeFactory()
    else:
        print("Unknown theme, defaulting to light.")
        factory = LightThemeFactory()

    client_code(factory)

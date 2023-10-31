"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx
from datetime import date


docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"

class MountState(rx.State):
    events: list[str] = []

    def on_mount(self):
        d0 = date(2023, 9, 23)
        d1 = date.today()
        delta = d1 - d0
        print(delta.days)
        self.events = [
            "Heute ist Tag " + str(delta.days)
        ]


def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            rx.foreach(MountState.events, rx.text),
            on_mount=MountState.on_mount,

            spacing="1.5em",
            font_size="2em",
            padding_top="10%",
        ),
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()

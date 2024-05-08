from textual.app import App
from textual import events
from textual.widgets import Header, Footer, TextView

class ChatGPTApp(App):
    async def on_mount(self):
        self.header = Header(text="ChatGPT")
        self.footer = Footer(text="Enter '/help' to learn about my functionality.")

        self.view = TextView(
            text="Привет! Чем я могу помочь?",
            width="100%",
            height="90%",
            wrap=True,
        )

        self.window.append(self.header)
        self.window.append(self.view)
        self.window.append(self.footer)

    async def on_start(self):
        self.footer.text = "Enter '/help' to learn about my functionality."

    async def handle_help_command(self, event):
        self.view.append("\nВведите команду '/help', чтобы узнать мои возможности.")

    async def handle_bot_command(self, event):
        self.view.append("\nВведите команду '/bot', чтобы получить информацию о сервере поддержки и приглашении.")

    async def on_key(self, event: events.Key) -> None:
        if event.key_sequence == "/help":
            await self.handle_help_command(event)
        elif event.key_sequence == "/bot":
            await self.handle_bot_command(event)

    async def on_shutdown(self):
        self.footer.text = "Спасибо за использование! До свидания."

app = ChatGPTApp()
app.run()
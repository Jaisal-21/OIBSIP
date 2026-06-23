import threading
import time

from plyer import notification
from speech import speak


def set_reminder(task, minutes):

    def reminder_thread():

        time.sleep(minutes * 60)

        notification.notify(
            title="Vyra Reminder",
            message=task,
            timeout=10
        )

        speak(f"Reminder. {task}")

    threading.Thread(
        target=reminder_thread,
        daemon=True
    ).start()
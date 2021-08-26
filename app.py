from plyer import notification

title = 'Hello World'

message = 'Good Night, Moon'

notification.notify(
    title = title,
    message = message,
    app_icon = None,
    timeout = 10, # time to display message for
    # ticker: notification status bar text
    toast = False # return full notification
)
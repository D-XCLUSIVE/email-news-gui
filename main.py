# used the code generated from chatgpt because the one provided is not working 
import FreeSimpleGUI as sg
import time
import requests
from send_email import send_email  # Ensure this import is correct
# topic = "tesla"
api_key = "e8ccf27349984b389e27b088bffb08ea"
label = sg.Text("Enter Topics")
topic =sg.InputText(tooltip="Enter topic", key="topic",)
label2 = sg.Text("Enter Email")
reciever = sg.InputText( key="reciever")
run = sg.Button('send', size=5, key="run", tooltip="run program")

sg.theme("Black")



window = sg.Window('Email News',
                   layout=[[label], [topic],
                           [label2], [reciever], [run]],
                           
                    font=('Helvetica', 10))

while True:
    event, values  = window.read()
    
    if event == sg.WIN_CLOSED:
        break
   

    match event:
        case "run":
            topic = values['topic']
            url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&apiKey={api_key}&language=en"

            try:
                response = requests.get(url)
                response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
                content = response.json()

                subject = "Latest Tesla News"
                body = ""
                # the first 20 articles are processed and included in the email body. Here’s a refined version of the code to ensure it meets your requirements clearly
                articles = content.get("articles", [])[:20]

                for article in articles:
                    title = article.get("title")
                    description = article.get("description")
                    subject = "SUbject: Today's news"

                    # improved with links in email
                    url = article.get("url")
                    if title:
                        body += f"{subject}\n{title}\n{description}\n{url}\n\n"  # Fix string concatenation and formatting

                body = body.encode("utf-8")
                message = body
                reciever = values['reciever']
                send_email(message, reciever)

            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
        case sg.WIN_CLOSED:
            break

window.close()

# try:
#     response = requests.get(url)
#     response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
#     content = response.json()

#     subject = "Latest Tesla News"
#     body = ""
#     # the first 20 articles are processed and included in the email body. Here’s a refined version of the code to ensure it meets your requirements clearly
#     articles = content.get("articles", [])[:20]

#     for article in articles:
#         title = article.get("title")
#         description = article.get("description")
#         subject = "SUbject: Today's news"

#         # improved with links in email
#         url = article.get("url")
#         if title:
#             body += f"{subject}\n{title}\n{description}\n{url}\n\n"  # Fix string concatenation and formatting

#     body = body.encode("utf-8")
#     send_email(message=body)

# except requests.exceptions.RequestException as e:
#     print(f"An error occurred: {e}")

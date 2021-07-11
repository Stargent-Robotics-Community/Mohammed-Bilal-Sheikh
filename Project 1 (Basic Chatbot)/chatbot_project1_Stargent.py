##Chat Bot for Subject Selection Councilling for 11th and 12th
#Importing Section
import pyttsx3
import speech_recognition as sr
bot = pyttsx3.init()
recog = sr.Recognizer()
recog.energy_threshold = 400
recog.dynamic_energy_threshold = True
def listen():
    while True:
        with sr.Microphone() as src:
            recog.adjust_for_ambient_noise(src, duration=1)
            
            print(f"\nListening.....")
            try:
                au = recog.listen(src)
                
            except:
                say(bot_name,"Please could you speak a little faster.")
                continue

        try:
            txt = recog.recognize_google(au)
            break
        except:
            say(bot_name,"Sorry that was not clear, please repeat.")
            continue

    return txt

def say(name_bot,txt_say):
    print(f"\n{name_bot}: {txt_say}")
    bot.say(f"{txt_say}")
    bot.runAndWait()

def final_chats(g_or_b, det):
    if g_or_b == "good":
        say(bot_name,"Oh That is wonderful news. You are all set for the future. Good for you. Now work hard towards achieving your goals. All the best.")
        say(bot_name,"But, if you have any queries, please let me know. I'll let the proper authorities know and they'll come back to you.")
        unsolved_query = listen()
        print(f"\n{user_name}: {unsolved_query.capitalize()}")
        if "no" in unsolved_query:
            say(bot_name,"Thank you for your time. I hope I could help. All the best for the future.")
        else:
            say(bot_name,"Thank you for your time. We will come back to you as soon as possible. All the best for the future.")
    else:
        say(bot_name,"Oh! I am really sorry that I was not of effective assistance.")
        say(bot_name,"If you have any particular queries, please let me know. I'll let the proper authorities know and they'll come back to you.")
        unsolved_query = listen()
        print(f"\n{user_name}: {unsolved_query.capitalize()}")
        if "no" in unsolved_query:
            say(bot_name,"Thank you for your time. Sorry again that I could not help. Still, all the best for the future, you never know you might not need any consultation and crack life all on your own.")
        else:
            say(bot_name,"Thank you for your time. Sorry again that I could not help. We will come back to you as soon as possible. All the best for the future.")
    print("\n\n\n"+("-"*50))
    print("\n\nResult of Consultation:\n")
    for i in det.keys():
        print(f"{i} : {det[i]}")
    print(f"Unsolved Query : {unsolved_query}")
    print("\n"+("-"*50))
    exit()

def bio_or_math():
    say(bot_name,f"Say, {user_name} are you more inclined towards Mathematics or Biology?")
    while True: 
        text = listen()
        print(f"\n{user_name}: {text}")
        if "math" in text:
            say(bot_name,"Nice.")
            s = "Science + Mathematics"
            break
        elif "bio" in text:
            say(bot_name,"Nice.")
            s = "Science + Biology"
            break
        else:
            say(bot_name,"Sorry I couldn't understand, please repeat.")
            continue
    return s

def math_or_cs():
    say(bot_name,f"Say, {user_name} are you more inclined towards Mathematics or Computer Science?")
    while True: 
        text = listen()
        print(f"\n{user_name}: {text}")
        if "math" in text:
            say(bot_name,"Nice.")
            s = "Commerce + Mathematics"
            break
        elif "computer" in text or "sci" in text:
            say(bot_name,"Nice.")
            s = "Commerce + Computer Science"
            break
        else:
            say(bot_name,"Sorry I couldn't understand, please repeat.")
            continue
    return s

bot_name = "John"
user_name = "User"
sub = ""
details = {"Name" : user_name, "Subject" : sub, "Councillor" : bot_name}
voices = bot.getProperty('voices')
bot.setProperty('rate',150)
bot.setProperty('volume',20)

say(bot_name,"Hello, my name is John. What is your name?")
while True:
    text = listen()
    tup = text.partition("name is")
    if tup[1] == "" and tup[2] == "":
        say(bot_name, "Please repeat as I could not get your name.")
        continue
    else:
        user_name = tup[2]
        print(f"\n{user_name}: {text.capitalize()}")
        details["Name"] = user_name
        break
   
say(bot_name,f"Hello {user_name}. Hope you are doing great. Today I or Emily will help you in selecting your Stream.")

say(bot_name,"Do you want to speak with me or Emily as your mentor?")

while True:
    text = listen()    
    print(f"\n{user_name}: {text.capitalize()}")
    if "emily" in text or "her" in text or "em" in text or "Em" in text:
        bot.setProperty('voice',voices[1].id)
        bot_name = "Emily"
        say(bot_name,"Hi, my name is Emily. Voice set to female. Thank you for wanting to talk to me.")
    elif "you" in text or "john" in text:
        say(bot_name,"Thank you for wanting to talk to me.")
    else:
        say(bot_name,"Sorry I couldn't understand, please repeat.")
        continue
    details["Councillor"] = bot_name
    break

say(bot_name,"So, let's talk about your choices. As you might know there is Humanities, Commerce and Science. Have you decided what you want to opt for yet?")

while True:
    text = listen()
    print(f"\n{user_name}: {text.capitalize()}")
    if "yes" in text:
        say(bot_name,"Oh That's very good. Would you be so kind so as to tell me which Stream you have chosen?")
        while True:
            subject = listen()
            print(f"\n{user_name}: {subject.capitalize()}")
            if "science" in subject:
                sub = bio_or_math()
                details["Subject"] = sub
                final_chats("good",details)
            elif "Commerce" in subject:
                sub = math_or_cs()
                details["Subject"] = sub
                final_chats("good",details)
            elif "humanities" in subject or "art" in subject:
                sub = "Humanities"
                details["Subject"] = sub
                final_chats("good",details)
            else:
                say(bot_name,"Sorry I couldn't understand, please repeat.")
                continue
            
        
    elif "no" in text:
        say(bot_name,"Don't worry we will figure it out together. That is why I am here.")
        say(bot_name,"Let us start with your grades. Don't be shy or anxious, I am no one to judge you. Tell me, what percentage did you score in your 10th Finals?")
        
        grade = listen()
        print(f"\n{user_name}: {grade.capitalize()}")
        per = grade.index("%")
        if len(grade[per-3:per]) == 3:
            res = grade[per-3:per]
        else:
            res = grade[per-2:per]
            
        if int(res) >= 60:
            say(bot_name,"Oh wow, that is a wonderful score. I think that you'd do great things in Science.")
            say(bot_name,"But just to be sure, you are interested in taking Science right?")
            while True:
                stream_match = listen()
                print(f"\n{user_name}: {stream_match}")
                if "yes" in stream_match:
                    sub = bio_or_math()
                    details["Subject"] = sub
                    final_chats("good",details)

                elif "no" in stream_match:
                    say(bot_name,"Oh! no worries. Let me know are you interested in Business and Entrepreneurship or Art-Forms and Creativity?")
                    text = listen()
                    print(f"\n{user_name}: {text}")
                    if "business" in text or "ship" in text:
                        say(bot_name,"Then you can give Commerce a try. I hope you love it and gain a lot of success in the future.")
                        sub = math_or_cs()
                        details["Subject"] = sub
                        final_chats("good",details)
                    elif "art" in text or "creativity" in text:
                        say(bot_name,"Then you can give Humanities a try. I hope you love it and gain a lot of success in the future.")
                        sub = "Humanities"
                        details["Subject"] = sub
                        final_chats("good",details)
                    else:
                        say(bot_name,f"Sorry {user_name} I am unable to answer that.")
                        sub = "Unable to help decide"
                        details["Subject"] = sub
                        final_chats("bad",details)
                
                else:
                    say(bot_name,"Sorry I couldn't understand, please repeat.")
                    continue

            
        elif int(res) < 60 and int(res) >= 50:
            say(bot_name,"Oh wow, not bad, not bad at all. I think that you'd do great things in Commerce.")
            say(bot_name,"But just to be sure, you are interested in taking Commerce right?")
            while True:
                stream_match = listen()
                print(f"\n{user_name}: {stream_match}")
                if "yes" in stream_match:
                    sub = math_or_cs()
                    details["Subject"] = sub
                    final_chats("good",details)
                    
                elif "no" in stream_match:
                    say(bot_name,"Oh! no worries. Let me know are you interested in Art-Forms and Creativity?")
                    text = listen()
                    print(f"\n{user_name}: {text}")
                    if "art" in text or "creativity" in text:
                        say(bot_name,"Then you can give Humanities a try. I hope you love it and gain a lot of success in the future.")
                        sub = "Humanities"
                        details["Subject"] = sub
                        final_chats("good",details)
                    else:
                        say(bot_name,f"Sorry {user_name} I am unable to answer that.")
                        sub = "Unable to help decide"
                        details["Subject"] = sub
                        final_chats("bad",details)
    
                else:
                    say(bot_name,"Sorry I couldn't understand, please repeat.")
                    continue
        
        else:
            say(bot_name,"Don't worry about it. Maybe you don't like logical subjects, and just to need to let lose in Humanities.")
            say(bot_name,"But just to be sure, you are interested in taking Humanities right?")
            while True:
                stream_match = listen()
                print(f"\n{user_name}: {stream_match}")
                if "yes" in stream_match:
                    sub = "Humanities"
                    details["Subject"] = sub
                    final_chats("good",details)

                elif "no" in stream_match:
                    say(bot_name,f"Sorry {user_name} but, due to less score, unfortunately you might not be able to get anything higher.")
                    say(bot_name,"You can take the road not taken. But, know that there will be a lot of hurdles. All the best.")
                    sub = "Unable to help decide"
                    details["Subject"] = sub
                    final_chats("bad",details)

                else:
                    say(bot_name,"Sorry I couldn't understand, please repeat.")
                    continue

    else:
        say(bot_name,"Sorry I couldn't understand, please repeat.")
        continue

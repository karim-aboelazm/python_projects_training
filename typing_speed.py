import time 

def typing_speed(text):
    start_time = time.time()
    input_text = input(f"Type The Text: {text}\nType: ")
    end_time = time.time()
    duration = end_time - start_time
    character_typed = len(input_text)
    type_speed = character_typed / duration
    return type_speed

text = "Hello my name is python , I am a programming language"
ts = typing_speed(text)
print(f"Your typing speed is {ts:.2f} character per secound")
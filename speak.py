from elevenlabs import generate, play, set_api_key
set_api_key("<Your api key>")
def speak(text):
    audio = generate(
        text=text,
        voice="Elli",
        model='eleven_multilingual_v1'
    )
    play(audio)

if __name__ == "__main__":
    text = input("Enter what you want to hear")
    speak(text)
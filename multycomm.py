from deepgram import DeepgramClient

DEEPGRAM_API_KEY = "bb404bfc7f160ae821aca13e97cd2965ed56b885"

AUDIO_URL = "https://github.com/Baizaa-Yousuf/multycomm/raw/refs/heads/main/TEST.mp3"

def main():
    try:
        deepgram = DeepgramClient(api_key="bb404bfc7f160ae821aca13e97cd2965ed56b885")

        response = deepgram.listen.v1.media.transcribe_url(
            url=AUDIO_URL,
            model="nova-3",
            language="en",
            summarize="v2",
            sentiment=True,
            smart_format=True,
            punctuate=True,
            paragraphs=True,
            diarize=True
        )

        # Print the full response object
        print(response)

        # Or access the transcript directly
        print("\nTranscript:")
        print(response.results.channels[0].alternatives[0].transcript)

    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    main()
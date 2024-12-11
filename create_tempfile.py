import io

def audio_bytes_into_temp_file(audio_bytes):
  buffer = io.BytesIO()
  buffer.name = 'my_audio.mp3'
  audio.export(buffer, format="mp3")
  return audio_bytes.export(buffer,'mp3')

#temp_file = audio_bytes_into_temp_file(audio)
#temp_file.name

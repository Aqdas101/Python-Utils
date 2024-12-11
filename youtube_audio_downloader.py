def dowload_youtube_video(url):
  '''
  Get URL and Save the audio in the current 
  Directory.
  '''

  from pytube import YouTube
  yt = YouTube(url)
  global audio_stream
  audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
  audio_stream.download()
  return 'download successfully'

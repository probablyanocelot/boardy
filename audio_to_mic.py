    import sounddevice as sd
    import numpy as np
    import wave
    import sys
    
    device = "some device"

    def play_audio_through_vad(filename, device_name="Your Virtual Audio Device Name"):
        try:
          with wave.open(filename, 'rb') as wf:
              sample_rate = wf.getframerate()
              audio_data = wf.readframes(wf.getnframes())
              audio_array = np.frombuffer(audio_data, dtype=np.int16)
              
              devices = sd.query_devices()
              device_index = None
              for i, device in enumerate(devices):
                  if device['name'] == device_name and device['hostapi'] == 0:
                      device_index = i
                      break
              if device_index is None:
                  print(f"Virtual audio device '{device_name}' not found.")
                  return
              
              sd.play(audio_array, samplerate=sample_rate, device=device_index)
              sd.wait()
        except Exception as e:
          print(f"Error playing audio: {e}")
          
    if __name__ == "__main__":
       if len(sys.argv) > 1:
           print("Arguments passed:")
           for arg in sys.argv[1:]:
               print(arg)
           
           try:
               play_audio_through_vad(sys.argv[1], device_name=device)
       else:
           print("No arguments passed.")

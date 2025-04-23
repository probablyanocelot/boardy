    import sys
    from play import play_audio_through_vad as play

    device = "some device"

          
    if __name__ == "__main__":
       if len(sys.argv) > 1:
           print("Arguments passed:")
           for arg in sys.argv[1:]:
               print(arg)
           
           try:
               play(sys.argv[1], device_name=device)
           except Exception as e:
               print(f"Error playing audio: {e}")
       else:
           print("No arguments passed.")

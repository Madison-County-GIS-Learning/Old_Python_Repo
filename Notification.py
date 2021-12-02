def notificationSound(text ='abcdefg'):
    import winsound, time, \
        os  # code from https://realpython.com/playing-and-recording-sound-python/#playing-audio-files
    ##Play wave file for notification # Additional information: https://www.geeksforgeeks.org/morse-code-translator-python/    OR    https://www.tutorialspoint.com/morse-code-translator-in-python
    MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                       'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                       'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                       '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--',
                       '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}
    text = text.upper()
    for i in text:
        print(i + '  ' + MORSE_CODE_DICT[i])
        HzHigh = 1000  # toneHigh
        HzLow = 800  # toneLow
        for letter in MORSE_CODE_DICT[i]:
            if letter == '.':
                rate = 25  #Changed from 50
                Hz = HzLow
            elif letter == '-':
                rate = 100  #Changed from 200
                Hz = HzHigh
            winsound.Beep(Hz, rate)
            time.sleep(1)

    # filename = r'C:\Windows\Media\Ring05.wav'
    # winsound.PlaySound(filename, winsound.SND_FILENAME)
    # rate = 400
    # count = 0
    # for i in text:
    # count = count +1
    # print(count)
    # print(i)
    # HzHigh = 1000 #toneHigh
    # HzLow = 900 #toneLow
    # for i in range(1):
    # winsound.Beep(HzHigh, rate)  # Beep at 1000 Hz for 300 ms
    # time.sleep(0.1)
    # winsound.Beep(HzHigh, rate)  # Beep at 1000 Hz for 300 ms
    # winsound.Beep(HzHigh, rate)  # Beep at 1000 Hz for 300 ms
    # winsound.Beep(HzHigh, rate)  # Beep at 1000 Hz for 300 ms
    # time.sleep(0.1)
    # winsound.Beep(HzHigh, rate)  # Beep at 1000 Hz for 300 ms
    # winsound.Beep(HzHigh, rate)  # Beep at 1000 Hz for 300 ms
    # time.sleep(0.1)
    # winsound.Beep(HzHigh, rate)  # Beep at 1000 Hz for 300 ms
    # winsound.Beep(HzHigh, rate)  # Beep at 1000 Hz for 300 ms
    # time.sleep(0.1)
    # winsound.Beep(HzHigh, rate)  # Beep at 1000 Hz for 300 ms
    # winsound.Beep(HzLow, int(rate/4))  # Beep at 1000 Hz for 90 ms
    # winsound.Beep(HzHigh, rate)  # Beep at 1000 Hz for 300 ms
    # winsound.Beep(HzHigh, rate)  # Beep at 1000 Hz for 300 ms
    # time.sleep(30)

## Placeholder portion of the script.

def endTone(wavName = 'Windows Hardware Remove.wav'): #    ''Alarm05.wav'):
    import winsound, time, os    #code from https://realpython.com/playing-and-recording-sound-python/#playing-audio-files
    path = r'C:\Windows\Media\\'
    #filename = r'C:\Windows\Media\Ring05.wav'
    filename = path + wavName
    winsound.PlaySound(filename, winsound.SND_FILENAME)
    #filename = path + 'ringout.wav'
    # winsound.PlaySound(filename, winsound.SND_FILENAME)
    # winsound.PlaySound(filename, winsound.SND_FILENAME)

## Placeholder portion of the script.

def crash(DegreeOfError = 5):
    ## This audio notification is intended to identify when the script fails.
    ## The degree of Error (1-10) is intended to advise if a crash needs immediate resolve.

    if DegreeOfError < 1:
        DegreeOfError = 1
    elif DegreeOfError > 10:
        DegreeOfError = 10
    else:
        pass
    import winsound, time, os
    path = r'C:\Windows\Media\\'
    #filename = r'C:\Windows\Media\Windows Critical Stop.wav'
    filename = path + 'Windows Critical Stop.wav'
    for i in range(0, DegreeOfError):
        winsound.PlaySound(filename, winsound.SND_FILENAME)


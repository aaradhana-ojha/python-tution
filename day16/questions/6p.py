'''Write PushSong(song) and PopSong() methods/functions in Python to add a new song and 
delete a song from a List of songs, considering them to act as push and pop operations of 
the Stack data structure'''

def PushSong(stack, song):
    stack.append(song)
    print("Song '" + song + "' pushed onto the stack.")

def PopSong(stack):
    if not stack:
        print("Stack is empty. Cannot pop.")
        return None
    song = stack.pop()
    print("Song '" + song + "' popped from the stack.")
    return song

song_stack = []

PushSong(song_stack, "Song 1: Imagine")
PushSong(song_stack, "Song 2: Bohemian Rhapsody")
PushSong(song_stack, "Song 3: Stairway to Heaven")
PushSong(song_stack, "Song 4: Hotel California")

print("Current stack:", song_stack)

PopSong(song_stack)
PopSong(song_stack)
PopSong(song_stack)
PopSong(song_stack)
PopSong(song_stack)

print("Current stack:", song_stack)

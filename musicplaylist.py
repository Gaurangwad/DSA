# Node class to represent each song
class Node:
    def __init__(self, song):
        self.song = song  # Song name
        self.prev = None  # Pointer to the previous song
        self.next = None  # Pointer to the next song

# Doubly Linked List class to manage the playlist
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Head of the playlist
        self.tail = None  # Tail of the playlist
        self.current = None  # Current song being played

    # Method to add a song to the playlist
    def add_song(self, song):
        new_song = Node(song)  # Create a new node
        if self.head is None:  # If the playlist is empty
            self.head = new_song
            self.tail = new_song
            self.current = new_song
        else:
            new_song.prev = self.tail  # Link new song to the tail
            self.tail.next = new_song
            self.tail = new_song  # Update the tail
        print(f"Song added: {song}")

    # Method to remove a song from the playlist
    def remove_song(self, song):
        if self.head is None:  # If the playlist is empty
            print("Playlist is empty!")
            return

        # Traverse the playlist to find the song
        current = self.head
        while current:
            if current.song == song:
                if current.prev:  # If the song is not the head
                    current.prev.next = current.next
                else:
                    self.head = current.next  # Update the head

                if current.next:  # If the song is not the tail
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev  # Update the tail

                if self.current == current:  # If the current song is being removed
                    self.current = current.next if current.next else current.prev

                print(f"Song removed: {song}")
                return
            current = current.next

        print(f"Song not found: {song}")

    # Method to move to the next song
    def next_song(self):
        if self.current and self.current.next:
            self.current = self.current.next
            print(f"Playing next song: {self.current.song}")
        else:
            print("No next song available!")

    # Method to move to the previous song
    def previous_song(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            print(f"Playing previous song: {self.current.song}")
        else:
            print("No previous song available!")

    # Method to display the current song
    def display_current_song(self):
        if self.current:
            print(f"Current song: {self.current.song}")
        else:
            print("No song is currently playing!")

# Main program
if __name__ == "__main__":
    playlist = DoublyLinkedList()

    while True:
        print("\nMusic Playlist Manager")
        print("1. Add Song")
        print("2. Remove Song")
        print("3. Play Next Song")
        print("4. Play Previous Song")
        print("5. Display Current Song")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            song = input("Enter the song name to add: ")
            playlist.add_song(song)
        elif choice == "2":
            song = input("Enter the song name to remove: ")
            playlist.remove_song(song)
        elif choice == "3":
            playlist.next_song()
        elif choice == "4":
            playlist.previous_song()
        elif choice == "5":
            playlist.display_current_song()
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
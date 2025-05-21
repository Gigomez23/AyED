from node import Node


class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.length = 0

    def add_song(self, song):
        new_node = Node(song)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.current = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def remove_song(self, song):
        current = self.head
        while current:
            if current.data == song:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                if self.current == current:
                    self.current = current.next if current.next else current.prev

                self.length -= 1
                return True
            current = current.next
        return False

    def next_song(self):
        if self.current and self.current.next:
            self.current = self.current.next
            return self.current.data
        return None

    def prev_song(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            return self.current.data
        return None

    def get_current_song(self):
        return self.current.data if self.current else None

    def show_playlist(self):
        songs = []
        current = self.head
        while current:
            prefix = ">" if current == self.current else " "
            songs.append(f"{prefix} {current.data}")
            current = current.next
        return "\n".join(songs)
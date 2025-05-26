from evaluacion.models.playlist import Playlist


def menu3():
    playlist = Playlist()

    while True:
        print("\n--- Menú de Playlist ---")
        print("1. Agregar canción")
        print("2. Eliminar canción")
        print("3. Reproducir siguiente canción")
        print("4. Reproducir canción anterior")
        print("5. Mostrar lista de reproducción")
        print("6. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            song = input("Ingrese el nombre de la canción: ")
            playlist.add_song(song)
            print(f"Canción '{song}' agregada.")

        elif choice == "2":
            song = input("Ingrese el nombre de la canción a eliminar: ")
            if playlist.remove_song(song):
                print(f"Canción '{song}' eliminada.")
            else:
                print(f"Canción '{song}' no encontrada.")

        elif choice == "3":
            next_song = playlist.next_song()
            if next_song:
                print(f"Reproduciendo siguiente canción: {next_song}")
            else:
                print("No hay más canciones siguientes.")

        elif choice == "4":
            prev_song = playlist.prev_song()
            if prev_song:
                print(f"Reproduciendo canción anterior: {prev_song}")
            else:
                print("No hay canciones anteriores.")

        elif choice == "5":
            print("\nLista de reproducción actual:")
            print(playlist.show_playlist())

        elif choice == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu3()
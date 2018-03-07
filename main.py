import music_holder

if __name__ == "__main__":
    filename = str(input())
    holder = music_holder.Music_Holder(filename)
    holder.print_name()


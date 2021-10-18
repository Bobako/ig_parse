import sys
import pickle

from ig_parser import Parser

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        if sys.argv[1] == "auth":
            if len(sys.argv) >= 4:
                login = sys.argv[2]
                password = sys.argv[3]
                proxy = None
                if len(sys.argv) == 5:
                    proxy = sys.argv[4]
                parser = Parser(login, password, proxy=proxy)
                with open("parser.pickle", "wb") as file:
                    pickle.dump(parser, file)
            else:
                print("Не хватает аргументов")

        else:
            with open("parser.pickle", "rb") as file:
                parser = pickle.load(file)
            if sys.argv[1] == "stories":
                username = sys.argv[2]
                print(parser.get_stories(username))
            elif sys.argv[1] == "hl_list":
                username = sys.argv[2]
                print(parser.get_highlights_list(username))
            elif sys.argv[1] == "hl":
                hl_id = sys.argv[2]
                print(parser.get_highlight_stories(hl_id))
            elif sys.argv[1] == "posts":
                _, _, username, start, fin = sys.argv
                start = int(start)
                fin = int(fin)
                print(parser.get_posts(username, start, fin))
            elif sys.argv[1] == "posts_d":
                _, _, username, start, fin = sys.argv
                start = int(start)
                fin = int(fin)
                print(parser.get_posts_by_date(username, start, fin))
            elif sys.argv[1] == "reels":
                _, _, username, start, fin = sys.argv
                start = int(start)
                fin = int(fin)
                print(parser.get_reels(username, start, fin))
            elif sys.argv[1] == "reels_d":
                _, _, username, start, fin = sys.argv
                start = int(start)
                fin = int(fin)
                print(parser.get_reels_by_date(username, start, fin))
            elif sys.argv[1] == "ava":
                _, _, username = sys.argv
                print(parser.get_profile_pic(username))
            elif sys.argv[1] == "uid":
                _, _, username = sys.argv
                print(parser.get_user_id(username))
    else:
        print("Use with args")






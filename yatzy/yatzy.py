import terminal_view


def main():
    try:
        terminal_view.run()
    except (KeyboardInterrupt, EOFError):
        print()
        print("Spelet avbröts.")


if __name__ == "__main__":
    main()

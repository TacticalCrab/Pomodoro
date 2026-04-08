class TerminalInput:
    INPUT_CHAR = ">"

    @staticmethod
    def get_int(text: str, default = None):
        default_text = f" (default: {default})" if default is not None else ""

        while True:
            value = input(f"{text}{default_text}{TerminalInput.INPUT_CHAR} ")
            if len(value) == 0:
                return default

            try:
                return int(value)
            except ValueError:
                pass

    @staticmethod
    def get_range(text: str, start: int, end: int, default = None):
        start_end_text = f"({start} - {end})" if end - start > 0 else ""
        space = " " if text and start_end_text else ""
        print(f"{text}{space}{start_end_text}", end="")

        while True:
            value = input(f"{TerminalInput.INPUT_CHAR} ")
            if len(value) == 0:
                return default

            try:
                integer = int(value)
            except ValueError:
                continue

            if integer < start or integer > end:
                print("Number not in range. Try again.")
                continue

            return integer
class StartView:

    def get_input(self, message:str):
        inputSequence = input(message)

        return inputSequence

    def print_message(self, message:str):
        print(message)
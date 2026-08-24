#input_handler.

'''
A class for handling CLI/console input.
'''

from collections.abc import Callable
from typing import Any

class InputHandler:
    """Class for capturing and parsing commands from the CLI
       It allows the setting of prespecified commands using ':'
       that the user can call during input"""
    def __init__(self, 
                 command_map: dict[str, Callable[[], Any]]):
        self.command_map = command_map

    def _categorise(self, user_input: str) -> tuple[bool, str]: 
        text = user_input.strip()
        if text.startswith(":"):
            command = text.lower().split()[0]
            return True, command    # True: command has been entered, return input
        return False, text          # False: text has been entered, return input

    def _get_command(self, command_name: str) -> Callable[[], Any] | None:
        command = self.command_map.get(command_name)        # check if command is in command_map
        if command is None:                                 # if not, show error message
            print("[system message: invalid command, try again]")
        return command

    def handle(self, user_input: str) -> tuple[bool, Any]:   # categorise input 
        is_command, value = self._categorise(user_input)
        if not is_command:
            return False, value

        command = self._get_command(value)                   
        return True, command

    def _try_command(self, user_input: str) -> tuple[bool, Any]:
        is_command, value = self._categorise(user_input)
        if not is_command:
            return False, value

        command = self._get_command(value)
        if command is None:
            return True, None

        return True, command()      # execute command if valid

# ----- accept certain values (or command) only
    def conditional_accept(self, accepted: list[str], prompt: str = "...  ") -> Any:
        accepted_set = set(accepted)

        while True:
            user_input = input(prompt)
            is_command, value = self._try_command(user_input)  # check if a command has been entered

            if is_command:
                if value is not None:
                    return value                # if so, return it
                continue
                
            if value in accepted_set:           # compare input vs accepted list
                return value
            
            print("Possible options are:")      # remind user of valid responses
            for response in accepted:
                print(response)
                continue                        # continue the loop

# ----- accept certain types (or command) only
    def conditional_type(self, accepted_type: str, prompt: str = "...  ") -> Any:
        converters: dict[str, Callable[[str], Any]] = {
            "str": str,
            "int": int,
            "float": float,
        }
        converter = converters.get(accepted_type)
        if converter is None:
            print("[system message: invalid desired type]")
            return None
        
        while True:
            user_input = input(prompt)
            is_command, value = self._try_command(user_input)  # check if a command has been entered

            if is_command:
                if value is not None:
                    return value
                continue
            else:
                               
                try:
                    val = converter(value)      # check if input is of valid type
                    return val                  # if so, return
                    break
                except ValueError:              # if not, continue loop
                    print(f"[system message: input of type {accepted_type} required, please try again]")
                    continue

                
          
                
                
                
                
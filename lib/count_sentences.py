#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    print("The value must be a string.")
    if not isinstance(value, str):
      print("The value must be a string.")
    else:
      self.value = value

  def is_sentence(self):
    return self.value.endswith(".")

  def is_question(self):
    return self.value.endswith("?")

  def is_exclamation(self):
    return self.value.endswith("!")

  def count_sentences(self):
    # Define sentence-ending punctuation
        sentence_endings = {'.', '!', '?'}
        
        # Strip leading and trailing whitespace and handle empty string
        stripped_value = self.value.strip()
        if not stripped_value:
            return 0
        
        # Initialize sentence count
        count = 0
        
        # Iterate through the string and count sentences
        for i in range(len(stripped_value) - 1):
            if stripped_value[i] in sentence_endings and stripped_value[i+1] not in sentence_endings:
                count += 1
        
        # Check the last character to see if it ends with a punctuation mark
        if stripped_value[-1] in sentence_endings:
            count += 1
        
        return count

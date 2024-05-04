"""
Simple script which generates a report consisting of 
word count and character count
"""

from typing import Any


def get_book_text(path: str) -> None:
    """Returns the text of the book"""
    with open(path) as f:
        return f.read()


def get_num_words(text: str) -> int:
    """Returns the number of words in the text"""
    words = text.split()
    return len(words)


def get_character_count(text: str) -> dict[str, int]:
    """Returns a mapping of each character and the number of times it appears"""
    character_count_map = {}
    for word in text.lower():
        for char in word:
            character_count_map[char] = 1 + character_count_map.get(char, 0)

    return character_count_map

def sort_on(hash_map: dict) -> int:
    """Key to sort the dict by"""
    return hash_map["count"]

def chars_dict_to_sorted_list(chars_dict: dict) -> list[dict[str, Any]]:
    """
    Transforms the dict into a list of dicts
    Returns a sorted list based on the number  of 
    the highest occuring character
    """
    sorted_list = []
    for ch, count in chars_dict.items():
        if ch.isalpha():
            sorted_list.append({"character": ch, "count": count})
    sorted_list.sort(reverse=True, key=sort_on)
    return  sorted_list

def generate_report(num_words: int, chars_sorted_list: list[dict[str, Any]]) -> None:
    """Generates the report"""
    print(f"{num_words} words found in the document\n")

    print()
    for chars_dict in chars_sorted_list:
        print(f"The character '{chars_dict["character"]}' character was found {chars_dict["count"]} times")

def main():
    """
    Main function called upon execution
    Prints a report generated based on provided book
    """
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_character_count(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print("--- Begin report of books/frankenstein.txt ---")
    generate_report(num_words=num_words, chars_sorted_list=chars_sorted_list)
    print("--- End report ---\n")


if __name__ == "__main__":
    """Main entry point to script"""
    main()

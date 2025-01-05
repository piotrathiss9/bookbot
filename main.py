def main():
    PATH = "books/frankenstein.txt"
    contents = read_contents(PATH)
    words = count_words(contents)
    c_count = count_chars(contents)
    report = format_report(PATH, words, c_count)
    print(report)


def format_report(path: str, words: int, c_count: dict):
    report = f"--- Begin report of {path} ---"
    report += f"{words} words found in the document \n\n"
    for key, value in c_count.items():
        report += f"The '{key}' character was found {value} times \n"
    report += "--- End report ---"
    return report


def read_contents(path: str):
    with open(path) as f:
        contents = f.read()
        return contents


def count_words(contents: str):
    count = 0
    contents = contents.split()
    for word in contents:
        count += 1
    return count


def count_chars(contents: str):
    contents = contents.lower()
    count_dictionary = {}
    for character in contents:
        if character in count_dictionary:
            count_dictionary[f"{character}"] += 1
        else:
            count_dictionary[f"{character}"] = 1
    return count_dictionary


main()

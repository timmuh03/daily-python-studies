'''
12/2/25
Given a string in camel case, return the snake case version of the string using the following rules:

The input string will contain only letters (A-Z and a-z) and will always start with a lowercase letter.
Every uppercase letter in the camel case string starts a new word.
Convert all letters to lowercase.
Separate words with an underscore (_).
'''

def camel_to_snake(camel):

    return camel




if __name__ == "__main__":
    print("camelCase to snake_case - Test Cases\n")

    tests = [
        ("helloWorld",          "hello_world"),          # Basic case
        ("camelCase",           "camel_case"),           # Starts with lowercase
        ("aSimpleTest",         "a_simple_test"),        # Multiple capitals
        ("thisIsATest",         "this_is_a_test"),       # Classic example
        ("onlyOneWord",         "only_one_word"),        # Single uppercase
        ("already_snake",       "already_snake"),        # No uppercase - unchanged
        ("a",                   "a"),                    # Single lowercase letter
        ("abc",                 "abc"),                  # All lowercase - unchanged
        ("aBC",                 "a_b_c"),                # Consecutive capitals
        ("XMLHttpRequest",      "xml_http_request"),     # Real-world example
        ("iPhone",              "i_phone"),              # Starts with lowercase i
        ("version2Beta",        "version2_beta"),        # Number in middle
        ("aVeryLongCamelString","a_very_long_camel_string"),
    ]

    for camel, expected in tests:
        result = camel_to_snake(camel)
        status = "PASS" if result == expected else "FAIL"
        print(f"{camel:25} - {result:30} | Expected: {expected} [{status}]")
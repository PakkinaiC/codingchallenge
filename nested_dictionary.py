#!/usr/bin/env python3

def nested_dictionary(obj: dict, key: str, delimiter: str = "/"):
    keys = key.split(delimiter)
    current = obj

    for key_path in keys:
        if isinstance(current, dict) and key_path in current:
            current = current[key_path]
        else:
            raise KeyError(f"Key path '{key_path}' not found in object.")
    return current


# TEST CASES #
def test_nested_dictionary():
    scenarios = [
        ({"a":{"b":{"c":"d"}}},"a/b/c","d"),
        ({"x":{"y":{"z":"a"}}},"x/y/z","a"),
        ({"a":{"b":None}},"a/b",None),
        ({"num":{"value": 21}},"num/value",22),
        ({"flag":{"enabled":True}},"flag/enabled",True),
        ({"a":{"b":{"c":{"d":{"e":"f"}}}}},"a/b/c/d/e","f"),
        ({"a":{"b":{"c":"d"}}},"a/x/c",KeyError),
        ({"a":{"b":{"c":{}}}},"a/b/c",{})
    ]

    passed = 0
    for i, (obj, path, expected) in enumerate(scenarios):
        try:
            output = nested_dictionary(obj, path)
            assert output == expected, f"Test {i+1} failed: expected {expected}, got {output}"
            print(f"Test {i+1} passed.")
            passed += 1
        except KeyError as e:
            if expected is KeyError:
                print(f"Test {i+1} passed. (KeyError as expected)")
                passed += 1
            else:
                print(f"Test {i+1} failed. Unexpected KeyError: {e}")
        except AssertionError as e:
            print(str(e))
    
    print(f"\nSummary: {passed}/{len(scenarios)} scenarios passed.")


if __name__ == "__main__":
    test_nested_dictionary()

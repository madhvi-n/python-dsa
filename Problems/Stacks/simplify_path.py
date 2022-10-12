"""
https://leetcode.com/problems/simplify-path/

Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system,
convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level,
and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'.
For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory
(i.e., no period '.' or double period '..')
Return the simplified canonical path.
"""


def simplify_path(path: str):
    stack = []
    cur = ""

    for c in path + "/":
        if c == "/":
            if cur == "..":
                if stack:
                    stack.pop()
            elif cur != "" and cur != ".":
                stack.append(cur)
            cur = ""
        else:
            cur += c
    return "/" + "/".join(stack)


def main():
    print(simplify_path("/home/"))
    print(simplify_path("/../"))
    print(simplify_path("/home//foo/"))
    print(simplify_path("/../abc/.//def/"))


if __name__ == "__main__":
    main()

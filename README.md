# Triangle Finder 🛠️

## Overview 📋
This Python script identifies all possible triangular triplets in a given array of integers. A triplet `(a, b, c)` is considered triangular if it satisfies the triangle inequality: `a + b > c`, `b + c > a`, and `c + a > b`.

## Features ✨
- **Input Handling** 🖱️: Prompts the user to input the size and elements of the list.
- **Triangle Detection** 🔍: Checks all possible triplets in the array to determine if they form a valid triangle.
- **Output** 📈: Returns the count of valid triangular triplets and lists each triplet.

## Time Complexity ⏱️
- Input collection: O(n), where `n` is the number of elements in the array.
- Triangle detection (nested loops): O(n³) due to three nested loops iterating over the array.
- Output printing: O(n) for printing the triplets.
- Overall complexity: O(n³) due to the triplet-checking loop.

## Usage 🚀
1. Run the script.
2. Enter the number of elements for the list (`n`).
3. Input `n` integers for the list.
4. The script outputs the count of valid triangular triplets and lists each triplet. If no triplets are found, it outputs "not triangular".

## Example 📝
```
Enter the Elements of The List: 4
Enter number 1: 3
Enter number 2: 4
Enter number 3: 5
Enter number 4: 6
count = 3
(3, 4, 5),
(3, 4, 6),
(4, 5, 6),
```
Explanation: The array `[3, 4, 5, 6]` contains three valid triangular triplets: `(3, 4, 5)`, `(3, 4, 6)`, and `(4, 5, 6)`.

## Notes 📌
- The script assumes all input elements are positive integers, as negative or zero values may not form valid triangles.
- The O(n³) complexity can be inefficient for large arrays. Consider optimizations (e.g., sorting the array first) for better performance in specific use cases.

## Requirements 🛠️
- Python 3.x

## License ⚖️
This project is unlicensed and free to use.

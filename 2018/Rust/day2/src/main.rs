use std::collections::HashMap;
const PUZZLE: &str = include_str!("input.txt");

fn main() {
    let mut doubles = 0;
    let mut triples = 0;
    for line in PUZZLE.lines() {
        let letters = count_letters(line);
        if letters.values().any(|&x| x == 2) {
            doubles += 1;
        }
        if letters.values().any(|&x| x == 3) {
            triples += 1;
        }
    }
    println!("Problem1: {}", doubles * triples);

    for (index, line) in PUZZLE.lines().enumerate() {
        for line2 in PUZZLE.lines().skip(index + 1) {
            if line.chars()
                .zip(line2.chars())
                .filter(|(x, y)| x != y)
                .count() == 1 {
                    let result = line.chars()
                        .zip(line2.chars())
                        .filter(|(x, y)| x == y)
                        .map(|(x, _)| x)
                        .collect::<String>();
                assert_eq!("rteotyxzbodglnpkudawhijsc", result);
                println!("Problem2: {}", result);
                return;
            }
        }
    }
}

fn count_letters(line: &str) -> HashMap<char, i16> {
    let mut letters = HashMap::new();
    for letter in line.chars() {
        let counter = letters.entry(letter).or_insert(0);
        *counter += 1;
    }
    letters
}

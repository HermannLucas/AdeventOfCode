const PUZZLE: &str = include_str!("../input.txt");

fn part2(mut input: usize) -> usize {
    let mut result = Vec::new();
    while input >= 6 {
        input = input.div_euclid(3) - 2;
        result.push(input);
    }
    result.iter().sum()
}
fn main() {
    let result: usize = PUZZLE
        .lines()
        .map(|i| i.parse::<usize>().unwrap())
        .map(|m| m.div_euclid(3) - 2)
        .sum();
    println!("One: {:?}", result);

    let result: usize = PUZZLE
        .lines()
        .map(|i| i.parse::<usize>().unwrap())
        .map(|m| part2(m))
        .sum();
    println!("Two: {:?}", result);
}

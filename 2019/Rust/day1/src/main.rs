const PUZZLE: &str = include_str!("../input.txt");

fn main() {
    let result: usize = PUZZLE
        .lines()
        .map(|i| i.parse::<usize>().unwrap())
        .map(|m| m.div_euclid(3) - 2)
        .sum();
    println!("One: {:?}", result);
}

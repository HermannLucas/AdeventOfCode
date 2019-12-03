const PUZZLE: &str = include_str!("../input.txt");

fn part2(mut input: usize) -> usize {
    let mut result = 0;
    loop {
        if input < 9 {
            return result;
        }
        input = input.div_euclid(3) - 2;
        result += input;
    }
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
        .map(part2)
        .sum();
    println!("Two: {:?}", result);
}

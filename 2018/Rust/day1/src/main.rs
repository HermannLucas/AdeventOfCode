use std::collections::HashSet;
const PUZZLE: &str = include_str!("input.txt");

fn main() {
    println!("{}", PUZZLE.lines().map(|x| x.parse::<i32>().unwrap()).sum::<i32>());

    let mut frequencies = HashSet::new();
    let mut sum = 0;

    println!("{}", PUZZLE
        .lines()
        .into_iter()
        .cycle()
        .find_map(|c| {
    		sum += c.parse::<i32>().unwrap();
    		frequencies.replace(sum)
    	})
        .unwrap());
}

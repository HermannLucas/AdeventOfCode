use std::collections::HashMap;
use std::convert::TryFrom;
use std::iter::FromIterator;

const PUZZLE: &str = include_str!("../input.txt");

enum Direction {
    Up(usize),
    Down(usize),
    Left(usize),
    Right(usize),
}

impl TryFrom<&str> for Direction {
    type Error = Box<dyn std::error::Error>;

    fn try_from(direction: &str) -> Result<Self, Self::Error> {
        match direction.split_at(1) {
            ("U", i) => Ok(Direction::Up(i.parse()?)),
            ("D", i) => Ok(Direction::Down(i.parse()?)),
            ("L", i) => Ok(Direction::Left(i.parse()?)),
            ("R", i) => Ok(Direction::Right(i.parse()?)),
            _ => Err(From::from("Unkown direction")),
        }
    }
}

struct Cable(Vec<Direction>);

impl Cable {
    fn new() -> Self {
        Cable(Vec::new())
    }

    fn add(&mut self, direction: Direction) {
        self.0.push(direction);
    }
}

impl FromIterator<Direction> for Cable {
    fn from_iter<I: IntoIterator<Item = Direction>>(iter: I) -> Self {
        let mut cable = Cable::new();
        for i in iter {
            cable.add(i);
        }
        cable
    }
}

impl TryFrom<Vec<&str>> for Cable {
    type Error = Box<dyn std::error::Error>;

    fn try_from(cable: Vec<&str>) -> Result<Self, Self::Error> {
        Ok(cable
            .iter()
            .map(|d| Direction::try_from(*d).unwrap())
            .collect())
    }
}

impl IntoIterator for Cable {
    type Item = Direction;
    type IntoIter = ::std::vec::IntoIter<Self::Item>;

    fn into_iter(self) -> Self::IntoIter {
        self.0.into_iter()
    }
}

struct Grid(HashMap<(usize, usize), Vec<usize>>);

impl Grid {
    fn new() -> Self {
        Grid(HashMap::new())
    }

    fn lay_cable(&mut self, pos: (usize, usize), cable_name: usize) {
        self.0
            .entry(pos)
            .and_modify(|v| v.push(cable_name))
            .or_insert(vec![cable_name]);
    }

    fn follow_cable(&mut self, cable: Cable, cable_name: usize) {
        let mut x = 0;
        let mut y = 0;

        for dir in cable.into_iter() {
            match dir {
                Direction::Up(dist) => {
                    for _ in 0..dist {
                        y += 1;
                        self.lay_cable((x, y), cable_name);
                    }
                }
                Direction::Down(dist) => {
                    for _ in 0..dist {
                        y -= 1;
                        self.lay_cable((x, y), cable_name);
                    }
                }
                Direction::Left(dist) => {
                    for _ in 0..dist {
                        x += 1;
                        self.lay_cable((x, y), cable_name);
                    }
                }
                Direction::Right(dist) => {
                    for _ in 0..dist {
                        x -= 1;
                        self.lay_cable((x, y), cable_name);
                    }
                }
            }
        }
    }
}

fn part1(cable1: Vec<&str>, cable2: Vec<&str>) -> usize {
    unimplemented!();
}

fn main() {
    println!("Hello, world!");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn part1_test() {
        let cable1 = vec!["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"];
        let cable2 = vec!["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"];

        assert_eq!(part1(cable1, cable2), 159);
    }
}

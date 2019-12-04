use std::collections::HashMap;
use std::convert::TryFrom;
use std::iter::FromIterator;

const PUZZLE: &str = include_str!("../input.txt");

#[derive(Debug)]
enum Direction {
    Up(isize),
    Down(isize),
    Left(isize),
    Right(isize),
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

#[derive(Debug)]
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

struct Grid(HashMap<(isize, isize), Vec<usize>>);

impl Grid {
    fn new() -> Self {
        Grid(HashMap::new())
    }

    fn lay_cable(&mut self, pos: (isize, isize), cable_name: usize) {
        self.0
            .entry(pos)
            .and_modify(|v| v.push(cable_name))
            .or_insert_with(|| vec![cable_name]);
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

    fn clean_cables(&mut self) {
        self.0.iter_mut().for_each(|(_, v)| {
            v.sort_unstable();
            v.dedup()
        });
    }
}

fn part1(cable1: Cable, cable2: Cable) -> isize {
    let mut grid = Grid::new();

    grid.follow_cable(cable1, 1);
    grid.follow_cable(cable2, 2);
    grid.clean_cables();

    grid.0
        .into_iter()
        .filter(|(_, v)| v.len() > 1)
        .map(|(k, _)| k.0.abs() + k.1.abs())
        .min()
        .unwrap()
}

fn main() {
    let puzzle: Vec<_> = PUZZLE
        .lines()
        .map(|l| l.split(',').collect::<Vec<&str>>())
        .collect();
    let cable1 = Cable::try_from(puzzle[0].clone()).unwrap();
    let cable2 = Cable::try_from(puzzle[1].clone()).unwrap();
    println!("Part one: {:?}", part1(cable1, cable2));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn part1_test() {
        let cable1 = Cable::try_from(vec![
            "R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72",
        ])
        .unwrap();
        let cable2 =
            Cable::try_from(vec!["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]).unwrap();

        assert_eq!(part1(cable1, cable2), 159);
    }
}

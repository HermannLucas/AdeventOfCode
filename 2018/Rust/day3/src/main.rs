use std::collections::HashMap;
use std::collections::HashSet;
const PUZZLE: &str = include_str!("input.txt");

#[derive(Hash, Eq, PartialEq)]
struct Cell {
    x: u16,
    y: u16,
}

struct Canvas {
    cells: HashMap<Cell, Vec<u16>>
}

impl Canvas {
    fn add_claim(&mut self, claim: Claim) {
        for y in claim.start.y..claim.end.y {
            for x in claim.start.x..claim.end.x {
                let ids = self.cells.entry(Cell {x: x, y: y}).or_insert(Vec::new());
                ids.push(claim.id);
            }
        }
    }
}

struct Claim {
    id: u16,
    start: Cell,
    end: Cell
}

impl Claim {
    fn create(line: Vec<u16>) -> Claim {
        Claim {
            id: line[0],
            start: Cell{x: line[1], y: line[2]},
            end: Cell{x: line[1] + line[3], y: line[2] + line[4]}
        }
    }
}

fn main() {
    let mut fabric =  Canvas {cells: HashMap::new()};
    for line in PUZZLE.lines() {
        fabric.add_claim(Claim::create(line.split(|c|
            c == ' ' ||
            c == '@' ||
            c == ',' ||
            c == ':' ||
            c == 'x' ||
            c == '#')
            .filter_map(|c| c.parse::<u16>().ok()).collect::<Vec<_>>()));
    }
    let result = fabric.cells.values().filter(|c| c.len() > 1).count();
    assert_eq!(108961, result);
    println!("Problem 1:{}", result);
    
    // Start of Problem 2
    let mut id_list = HashSet::new();
    for (_cell, ids) in fabric.cells.iter() {
        for id in ids.iter() {
            if !id_list.contains(id) {
                if !is_overlap(&fabric, id) {
                    assert_eq!(&681, id);
                    println!("Problem 2:{}", id);
                    return
                }
                id_list.insert(id);
            }
        }
    }
}

fn is_overlap(canvas: &Canvas, id: &u16) -> bool {
    for (_cell, ids) in canvas.cells.iter() {
        if ids.contains(id) && ids.len() > 1 {
            return true
        }
    }
    return false
}

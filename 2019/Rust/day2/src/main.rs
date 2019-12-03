const PUZZLE: &str = include_str!("../input.txt");

struct Computer {
    program: Vec<usize>,
    noun: usize,
    verb: usize,
    instruction_pointer: usize,
}

impl Computer {
    fn new(program: Vec<usize>) -> Self {
        Computer {
            program,
            noun: 0,
            verb: 0,
            instruction_pointer: 0,
        }
    }

    fn run_program(&mut self) -> Result<usize, Box<dyn std::error::Error>> {
        self.instruction_pointer = 0;
        let mut memory = self.program.clone();
        memory[1] = self.noun;
        memory[2] = self.verb;
        loop {
            let opcode = memory.get(self.instruction_pointer);
            if opcode == Some(&1) {
                let dest = memory[self.instruction_pointer + 3];
                memory[dest] = memory[memory[self.instruction_pointer + 1]]
                    + memory[memory[self.instruction_pointer + 2]];
                self.instruction_pointer += 4;
            } else if opcode == Some(&2) {
                let dest = memory[self.instruction_pointer + 3];
                memory[dest] = memory[memory[self.instruction_pointer + 1]]
                    * memory[memory[self.instruction_pointer + 2]];
                self.instruction_pointer += 4;
            } else if opcode == Some(&99) {
                return Ok(memory[0]);
            } else {
                return Err(From::from("Invalid opcode"));
            }
        }
    }

    fn set_noun(&mut self, noun: usize) {
        self.noun = noun;
    }

    fn set_verb(&mut self, verb: usize) {
        self.verb = verb;
    }
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let puzzle: Vec<usize> = PUZZLE
        .trim()
        .split(',')
        .map(|o| o.parse::<usize>().unwrap())
        .collect();

    let mut computer = Computer::new(puzzle);
    computer.set_noun(12);
    computer.set_verb(2);
    println!("Part one: {:?}", computer.run_program()?);

    let mut noun = 0;
    let mut verb = 0;
    computer.set_noun(noun);
    computer.set_verb(verb);
    let objective = 19690720;
    while let Ok(result) = computer.run_program() {
        if result == objective {
            break;
        } else {
            if verb < 99 {
                verb += 1;
            } else if noun < 99 {
                verb = 0;
                noun += 1;
            } else {
                return Err(From::from(format!(
                    "Could not find objective of {:?}",
                    objective
                )));
            }
        }
        computer.set_noun(noun);
        computer.set_verb(verb);
    }

    println!("Part two: {:?}", 100 * computer.noun + computer.verb);

    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn part_1() {
        // assert_eq!(run_1(vec![1, 0, 0, 0, 99]).unwrap(), vec![2, 0, 0, 0, 99]);
        // assert_eq!(run_1(vec![2, 3, 0, 3, 99]).unwrap(), vec![2, 3, 0, 6, 99]);
        // assert_eq!(
        //     run_1(vec![2, 4, 4, 5, 99, 0]).unwrap(),
        //     vec![2, 4, 4, 5, 99, 9801]
        // );
        // assert_eq!(
        //     run_1(vec![1, 1, 1, 4, 99, 5, 6, 0, 99]).unwrap(),
        //     vec![30, 1, 1, 4, 2, 5, 6, 0, 99]
        // );
    }
}

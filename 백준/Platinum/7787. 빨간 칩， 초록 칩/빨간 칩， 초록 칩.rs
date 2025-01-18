use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let r: u32 = next().parse().unwrap();
    let g: u32 = next().parse().unwrap();
    let mut winner = "B";

    if (r + g) % 2 != 0 {
        winner = "A";
    }
    if r.min(g) % 2 == 0 && ((r + g) / 2) % 2 != 0 {
        winner = "A";
    }
    print!("{} player wins", winner);
}

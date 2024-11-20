use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().lines();

    let first_line = input.next().unwrap().unwrap();
    let mut iter = first_line.split_whitespace();
    let x: i32 = iter.next().unwrap().parse().unwrap();
    let y: i32 = iter.next().unwrap().parse().unwrap();
    let z: i32 = ((y - x) as f64).sqrt() as i32;

    if y - x == 0 {
        print!("0");
    } else if z * z == y - x {
        print!("{}", 2 * z - 1);
    } else if y - x - z * z <= z {
        print!("{}", 2 * z);
    } else {
        print!("{}", 2 * z + 1);
    }
}

use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n = next().parse::<i32>().unwrap();
    if n % 2 != 0 {
        print!("Soomin");
    } else {
        print!("Song");
    }
}

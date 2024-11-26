use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: i32 = next().parse().unwrap();

    if n == 2 {
        print!("1");
    } else if n == 3 {
        print!("3");
    } else {
        print!("{}", n * 3 - 4);
    }
}

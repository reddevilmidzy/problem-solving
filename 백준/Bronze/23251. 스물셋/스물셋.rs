use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let t: usize = next().parse().unwrap();
    let mut res = String::new();

    for _ in 0..t {
        let n: usize = next().parse().unwrap();
        res.push_str((23 * n).to_string().as_str());
        res.push('\n');
    }
    print!("{res}");
}

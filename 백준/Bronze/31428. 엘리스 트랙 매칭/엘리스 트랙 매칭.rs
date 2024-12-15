use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();

    let tracks: Vec<String> = (0..n).map(|_| next().parse().unwrap()).collect();

    let elice: String = next().parse().unwrap();
    let mut cnt: u16 = 0;

    for track in &tracks {
        if &elice == track {
            cnt += 1;
        }
    }
    print!("{cnt}");
}

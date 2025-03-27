use std::io::{Read, stdin};

fn main() {
    let mut bits = vec![0; 1 << 20];
    let mut end = false;
    while !end {
        let mut buffer = String::new();
        let mut byte = [0; 1];
        while stdin().read(&mut byte).unwrap() > 0 {
            if byte[0] == b' ' {
                break;
            } else if byte[0] == b'\n' {
                end = true;
                break;
            }
            buffer.push(byte[0] as char);
        }

        if let Ok(num) = buffer.trim().parse::<usize>() {
            if (bits[num / 32] & (1 << (num % 32))) == 0 {
                print!("{num} ");
                bits[num / 32] |= 1 << (num % 32);
            }
        }
    }
}

use std::io::{read_to_string, stdin};
use std::fmt::Write;

fn solve(apple: usize, peach: usize) -> String {
    if peach % 2 != 0 {
        return "NO".to_string();
    }
    let mut res = String::new();
    writeln!(res, "YES").unwrap();
    if peach == 2 {
        if apple > 0 {
            writeln!(res, "{} {}", 1, apple + peach).unwrap();
            writeln!(res, "{}", "O".repeat(apple + peach)).unwrap();
        } else {
            writeln!(res, "1 2").unwrap();
            writeln!(res, "OO").unwrap();
        }
    } else if peach >= 4 {
        let tmp = (peach - 2) / 2;
        let size = apple + peach - tmp;
        let mut upper = String::new();
        let mut lower = ".".to_string();
        for i in 0..tmp {
            if i % 2 == 0 {
                upper.push_str(".O");
            } else {
                lower.push_str(".O");
            }
        }

        upper.push_str(&*".".repeat(size - upper.len()));
        lower.push_str(&*".".repeat(size - lower.len()));
        writeln!(res, "3 {}", size).unwrap();
        writeln!(res, "{}", upper).unwrap();
        writeln!(res, "{}", "O".repeat(size)).unwrap();
        writeln!(res, "{}", lower).unwrap();
    } else if peach == 0 {
        if apple == 1 {
            writeln!(res, "1 1").unwrap();
            writeln!(res, "O").unwrap();
        } else if apple == 4 {
            writeln!(res, "2 2").unwrap();
            writeln!(res, "OO\nOO").unwrap();
        } else if apple == 7 {
            writeln!(res, "3 3").unwrap();
            writeln!(res, "OO.\nOOO\n.OO").unwrap();
        } else if apple >= 8 && (apple - 8) % 2 == 0 {
            let tmp = (apple - 8) / 2 + 1;
            writeln!(res, "3 {}", (apple - 2) / 2).unwrap();
            writeln!(res, "{}", "O".repeat((apple - 2) / 2)).unwrap();
            writeln!(res, "O{}O", ".".repeat(tmp)).unwrap();
            writeln!(res, "{}", "O".repeat((apple - 2) / 2)).unwrap();
        } else if apple >= 11 && (apple - 11) % 2 == 0 {
            let tmp = (apple - 11) / 2 + 1;
            writeln!(res, "4 {}", 3 + tmp).unwrap();
            writeln!(res, "{}OO", ".".repeat(tmp + 1)).unwrap();
            writeln!(res, "{}", "O".repeat(3 + tmp)).unwrap();
            writeln!(res, "O{}O.", ".".repeat(tmp)).unwrap();
            writeln!(res, "{}.", "O".repeat(2 + tmp)).unwrap();
        } else {
            return "NO".to_string();
        }
    } else {
        return "NO".to_string();
    }
    res
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let apple: usize = next().parse().unwrap();
    let peach: usize = next().parse().unwrap();

    let res = solve(apple, peach);
    print!("{res}");
}

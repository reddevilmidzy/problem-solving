use std::fmt::Write;

fn main() {
    let n = 814;
    let mut res = String::with_capacity(n);

    // 가장 가까운 두점
    writeln!(res, "-8140 -8140").unwrap();
    writeln!(res, "-8139 -8140").unwrap();

    for i in 1..(n - 1) as i32 {
        writeln!(res, "{} {}", -8139 + i * 3, -8139 + i * 3).unwrap();
    }
    print!("{res}");
}

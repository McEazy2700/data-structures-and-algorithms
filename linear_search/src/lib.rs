#[cfg(test)]
mod tests {
    use crate::linear_serch;

    #[test]
    pub fn test_linear_search() {
        let arr = [1, 23, 45, 63, 7];
        let needle = 63;
        let index = linear_serch::linear_search(arr.iter(), &needle).unwrap();
        println!("index {}", index);
        assert_eq!(index, 3)
    }
}
mod linear_serch;

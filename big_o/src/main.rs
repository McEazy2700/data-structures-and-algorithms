fn main() {
    /*What: Big O is a way to categorize you algorithim on time or memory bassed
     * on the input. It is not meant to be an exert measurement. It tels you how
     * your algorithim will react as your input grows.*/

    /*Why: It often helps us make descision on why we should or should not use a
     * specific data-structure.*/

    /// A function with an O(n) time complexity. This means the time it takes to
    /// run the algorithm is linear with the amount of input. For every unit of
    /// input, there is an extra loop the function has to do.
    fn sum_char_codes(n: String) -> usize {
        let mut sum = 0;
        for character in n.chars() {
            sum += character.len_utf16();
        }
        return sum
    }
    println!("{}", sum_char_codes("something".to_string()));

    /* Main Concept of Big-O 
     * 1. Growth with respect to input.
     * 2. Constants are always dropped.
     * 3. Worst case scenerio is usually the best way to measure*/
}

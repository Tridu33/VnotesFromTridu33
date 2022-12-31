#[derive(Debug, Clone)]
pub struct TagRule {
    first_char: char,
    append_characters: String,
}

impl TagRule {
    pub fn new<S: Into<String>>(first_char: char, append_characters: S) -> TagRule {
        TagRule{
            first_char: first_char,
            append_characters: append_characters.into(),
        }
    }

    pub fn applies_to(&self, string: &str) -> bool {
        match string.chars().next() {
            Some(c) => self.first_char == c,
            _ => false,
        }
    }

    pub fn follow(&self, input: &str) -> String {
        let buf = input.to_string() + &self.append_characters;
        buf
    }

    pub fn first_char(&self) -> char { self.first_char }
    pub fn append_characters(&self) -> String { self.append_characters.clone() }
}

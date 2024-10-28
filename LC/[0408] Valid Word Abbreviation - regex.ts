function validWordAbbreviation(word: string, abbr: string): boolean {
  if (/([a-z]|^)0/.test(abbr)) {
    return false;
  }

  const regexStr = abbr
    .replace(/(\d+)/g, ".{$1}");
  const regex = new RegExp(`^${regexStr}$`);
  return regex.test(word);
};
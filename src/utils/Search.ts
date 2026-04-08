import matrixData from "../data/matrix-data.json";

// returns a shortened version of a string (<50 chars)
// used in search displays
export function truncatedDescription(text: string, length?: number) {
  const l = length ?? 50;
  const words = text.split(" ");
  if (words.length > l) {
    return words.slice(0, l).join(" ") + "...";
  }
  return text;
}

// lowercase, remove diacritics, turn punctuation into spaces, collapse whitespace
export function normalize(s: string) {
  return s
    .toLowerCase()
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[^a-z0-9]+/g, " ")
    .trim()
    .replace(/\s+/g, " ");
}

export function countOccurrences(haystack: string, needle: string) {
  if (!needle) return 0;
  let count = 0;
  let idx = 0;
  for (;;) {
    idx = haystack.indexOf(needle, idx);
    if (idx === -1) break;
    count++;
    idx += needle.length;
  }
  return count;
}

export function performSearch(searchQuery: string) {
  if (!searchQuery) return [];

  // Normalize + tokenize query: "Account takeover" -> ["account","takeover"]
  const tokens = normalize(searchQuery).split(" ").filter(Boolean);

  const results = [];

  for (const i of matrixData) {
    const id = i.id ?? "";
    const name = i.name ?? "";
    const desc = i.description ?? "";

    // Normalized fields (case-insensitive, punctuation-insensitive)
    const idN = normalize(id);
    const nameN = normalize(name);
    const descN = normalize(desc);

    const allText = `${idN} ${nameN} ${descN}`;

    // Require ALL tokens to be present somewhere (AND search)
    const allTokensPresent = tokens.every((t) => allText.includes(t));
    if (!allTokensPresent) continue;

    // Scoring: weight matches in id/name/description
    let score = 0;
    for (const t of tokens) {
      score += 5 * countOccurrences(idN, t);
      score += 3 * countOccurrences(nameN, t);
      score += 1 * countOccurrences(descN, t);
    }

    // Bonus if exact normalized phrase occurs (keeps phrase results on top)
    const phrase = normalize(searchQuery);
    if (allText.includes(phrase)) score += 10;

    if (score > 0) results.push({ ...i, searchScore: score });
  }

  return results.sort((a, b) => b.searchScore - a.searchScore);
}

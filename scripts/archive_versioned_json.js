const fs = require("fs");
const path = require("path");
const { f3Version } = require("../package.json");

if (!/^\d+\.\d+$/.test(f3Version)) {
  throw new Error(`Invalid f3Version in package.json: ${f3Version}`);
}

const outputs = [
  ["public/f3-v1.json", `public/f3-v${f3Version}.json`],
  ["public/f3-stix.json", `public/f3-stix-v${f3Version}.json`],
  ["public/f3-navigator.json", `public/f3-navigator-v${f3Version}.json`],
];

for (const [source, destination] of outputs) {
  if (!fs.existsSync(source)) {
    throw new Error(`Generated JSON file is missing: ${source}`);
  }

  JSON.parse(fs.readFileSync(source, "utf8"));
  fs.copyFileSync(source, destination);
  console.log(
    `Archived ${path.basename(source)} as ${path.basename(destination)}`,
  );
}

console.log(
  "Existing JSON files for earlier F3 versions remain unchanged for historical comparisons.",
);

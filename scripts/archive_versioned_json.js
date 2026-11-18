const fs = require("fs");
const path = require("path");
const { f3Version } = require("../package.json");

if (!/^\d+\.\d+$/.test(f3Version)) {
  throw new Error(`Invalid f3Version in package.json: ${f3Version}`);
}

const outputs = [
  ["public/f3-v1.json", `public/f3-v${f3Version}.json`, true],
  ["public/f3-stix.json", `public/f3-stix-v${f3Version}.json`, true],
  ["public/f3-navigator.json", `public/f3-navigator-v${f3Version}.json`, true],
  ["public/F3-v1.xlsx", `public/f3-excel-v${f3Version}.xlsx`, false],
];

for (const [source, destination, isJson] of outputs) {
  if (!fs.existsSync(source)) {
    throw new Error(`Release artifact is missing: ${source}`);
  }

  if (isJson) {
    JSON.parse(fs.readFileSync(source, "utf8"));
  }
  fs.copyFileSync(source, destination);
  console.log(
    `Archived ${path.basename(source)} as ${path.basename(destination)}`,
  );
}

console.log(
  "Existing files for earlier F3 versions remain unchanged for historical comparisons.",
);

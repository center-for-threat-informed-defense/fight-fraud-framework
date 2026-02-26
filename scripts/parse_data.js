const ExcelJS = require("exceljs");
const fs = require("fs");
const SOURCE_FILE = "src/data/FFF Complete.xlsx";
const DESTINATION_FILE = "src/data/Techniques.json";

console.log("here..");

(async function () {
  const wb = new ExcelJS.Workbook();
  // initialize new list for techniques
  const techniques = [];
  await wb.xlsx.readFile(SOURCE_FILE);

  console.log("Reading from Calculator spreadsheet...");
  const worksheet = wb.getWorksheet("Techniques");
  worksheet.eachRow({ includeEmpty: false }, function (row) {
    const tid = row.getCell(1).value;

    const technique = {
      id: tid,
      name: row.getCell(2).value,
      description: convertRichTextToMarkdown(row.getCell(3).value),
      tactics: row.getCell(4).value.split(", "),
      subtechniques: [],
      isAttack: tid.charAt(0) === "T" ? true : false,
      version: "1.0",
      lastModified: new Date().toISOString(),
    };

    if (tid.split(".").length > 1) {
      const parent = techniques.find(
        (t) => t.id === technique.id.split(".")[0],
      );
      parent.subtechniques.push(technique.id);
      console.log("subtechnique added to parent ", parent);
    }
    techniques.push(technique);
  });

  const str = JSON.stringify(techniques, null, 4);
  fs.writeFile(DESTINATION_FILE, str, (error) => {
    if (error) {
      console.error(error);
      throw error;
    }
  });
  console.log("Export technique data to Techniques.json");
})();

function convertRichTextToMarkdown(richTextValue) {
  if (!richTextValue || !Array.isArray(richTextValue.richText)) {
    return String(richTextValue || "");
  }

  let markdownString = "";

  richTextValue.richText.forEach(({ font, text }) => {
    let segment = text;
    // Apply bold formatting
    if (font?.bold) {
      segment = `**${segment}**`;
    }
    // Apply italic formatting
    if (font?.italic) {
      segment = `*${segment}*`;
    }
    // Apply strikethrough formatting (Markdown uses '~~' for strikethrough)
    if (font?.strike) {
      segment = `~~${segment}~~`;
    }
    // Handle hyperlinks if they exist in the cell
    // Note: Hyperlinks might be a separate property in the cell value object,
    // this example focuses on inline font styles.
    // The link should be applied to the 'text' property if available in the richText part.

    markdownString += segment;
  });

  // Basic cleanup for consecutive formatting, if necessary
  markdownString = markdownString
    .replace(/\*\*\*\*/g, "") // Remove empty bold
    .replace(/\*\**/g, "") // Remove empty italic
    .replace(/~~~*/g, ""); // Remove empty strikethrough
  console.log("parsing rich text ", richTextValue, " into ", markdownString);

  return markdownString;
}

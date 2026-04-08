const ExcelJS = require("exceljs");
const fs = require("fs");
const SOURCE_FILE = "src/data/FFF Complete.xlsx";
const DESTINATION_FILE = "src/data/matrix-data.json";

(async function () {
  const wb = new ExcelJS.Workbook();
  // initialize new list for techniques
  const techniques = [];
  await wb.xlsx.readFile(SOURCE_FILE);
  console.log("Reading from Compiled technique spreadsheet...");
  console.log("Grabbing tactics");

  const worksheet2 = wb.getWorksheet("Tactics");
  worksheet2.eachRow({ includeEmpty: false }, function (row, rowNum) {
    if (rowNum === 1) {
      return;
    } // skip heading row
    const technique = {
      id: row.getCell(1).value,
      name: row.getCell(2).value,
      description: convertRichTextToMarkdown(row.getCell(3).value),
      isAttack: row.getCell(1).value.charAt(0) === "T" ? true : false,
      version: "1.0",
      lastModified: new Date().toISOString(),
      tactic: true,
    };
    techniques.push(technique);
  });
  console.log("Grabbing techniques");

  const worksheet = wb.getWorksheet("Techniques");
  worksheet.eachRow({ includeEmpty: false }, function (row, rowNum) {
    if (rowNum === 1) {
      return;
    } // skip heading row
    const tid = row.getCell(1).value;

    // Safely normalize the tactics cell to a string and split
    let tacticsCellValue = row.getCell(4).value;
    if (tacticsCellValue && typeof tacticsCellValue === "object") {
      if ("result" in tacticsCellValue) {
        tacticsCellValue = tacticsCellValue.result;
      } else if ("text" in tacticsCellValue) {
        tacticsCellValue = tacticsCellValue.text;
      } else if (
        "richText" in tacticsCellValue &&
        Array.isArray(tacticsCellValue.richText)
      ) {
        tacticsCellValue = tacticsCellValue.richText
          .map((part) => part.text)
          .join("");
      }
    }
    const tactics =
      typeof tacticsCellValue === "string" && tacticsCellValue.trim().length > 0
        ? tacticsCellValue.split(/\s*,\s*/)
        : [];

    const technique = {
      id: tid,
      name: row.getCell(2).value,
      description: convertRichTextToMarkdown(row.getCell(3).value),
      tactics: tactics,
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

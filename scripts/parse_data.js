const ExcelJS = require("exceljs");
const fs = require("fs");
const SOURCE_FILE = "src/data/FFF Complete.xlsx";
const DESTINATION_FILE = "src/data/matrix-data.json";
const PUBLIC_FILE = "public/f3-v1.json";
const PUBLIC_SPREADSHEET = "public/F3-v1.xlsx";
const PREVIOUS_PUBLIC_FILE = "public/f3-v1.1.json";
const CURRENT_VERSION = "1.2";

(async function () {
  const wb = new ExcelJS.Workbook();
  // initialize new list for techniques
  const techniques = [];
  const previousTechniques = new Map(
    JSON.parse(fs.readFileSync(PREVIOUS_PUBLIC_FILE, "utf8")).map((item) => [
      item.id,
      item,
    ]),
  );
  // Tables are presentation metadata and are not needed for the data export.
  // Ignoring them also avoids ExcelJS table-part parsing issues in workbooks
  // edited by current versions of Excel and openpyxl.
  await wb.xlsx.readFile(SOURCE_FILE, { ignoreNodes: ["tableParts"] });
  console.log("Reading from Compiled technique spreadsheet...");
  console.log("Grabbing tactics");

  const worksheet2 = wb.getWorksheet("Tactics");
  worksheet2.eachRow({ includeEmpty: false }, function (row, rowNum) {
    if (rowNum === 1) {
      return;
    } // skip heading row
    const name = row.getCell(2).value;
    const description = convertRichTextToMarkdown(row.getCell(3).value);
    const previous = previousTechniques.get(row.getCell(1).value);
    if (
      previous &&
      (normalizeComparisonText(previous.name) !== normalizeComparisonText(name) ||
        normalizeComparisonText(previous.description) !==
          normalizeComparisonText(description))
    ) {
      throw new Error(
        `Tactic ${row.getCell(1).value} changed, but the Tactics sheet has no Modified Date column.`,
      );
    }
    const technique = {
      id: row.getCell(1).value,
      name: name,
      description: description,
      isAttack: row.getCell(1).value.charAt(0) === "T" ? true : false,
      version: CURRENT_VERSION,
      lastModified: previous?.lastModified || new Date().toISOString(),
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

    const name = row.getCell(2).value;
    const description = convertRichTextToMarkdown(row.getCell(3).value);
    const isAttack = tid.charAt(0) === "T" ? true : false;
    const previous = previousTechniques.get(tid);
    const modifiedDate = dateCellToIso(row.getCell(7).value);
    const addedDate = dateCellToIso(row.getCell(6).value);
    const coreChanged =
      previous &&
      (normalizeComparisonText(previous.name) !== normalizeComparisonText(name) ||
        normalizeComparisonText(previous.description) !==
          normalizeComparisonText(description) ||
        previous.isAttack !== isAttack ||
        JSON.stringify(previous.tactics || []) !== JSON.stringify(tactics));

    if (coreChanged && !modifiedDate) {
      throw new Error(
        `Technique ${tid} changed without a Modified Date in the workbook.`,
      );
    }

    const lastModified = modifiedDate || previous?.lastModified || addedDate;
    if (!lastModified) {
      throw new Error(
        `Technique ${tid} has no Modified Date, prior published timestamp, or Added Date.`,
      );
    }

    const technique = {
      id: tid,
      name: name,
      description: description,
      tactics: tactics,
      subtechniques: [],
      isAttack: isAttack,
      version: CURRENT_VERSION,
      lastModified: lastModified,
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
  console.log("Export technique data to matrix-data.json");
  fs.writeFile(PUBLIC_FILE, str, (error) => {
    if (error) {
      console.error(error);
      throw error;
    }
  });
  console.log("Export technique data to public file location");
  // here i want to copy the excel workbook from one directory into another
  fs.copyFile(SOURCE_FILE, PUBLIC_SPREADSHEET, (err) => {
    if (err) throw err;
    console.log(`Copied Excel workbook to ${PUBLIC_SPREADSHEET}`);
  });
})();

function dateCellToIso(value) {
  if (!value) {
    return null;
  }
  if (value instanceof Date) {
    return value.toISOString();
  }
  if (typeof value === "object" && "result" in value) {
    return dateCellToIso(value.result);
  }
  const parsed = new Date(value);
  if (Number.isNaN(parsed.getTime())) {
    throw new Error(`Invalid workbook date: ${value}`);
  }
  return parsed.toISOString();
}

function normalizeComparisonText(value) {
  return String(value || "")
    .replace(/\s+/g, " ")
    .trim();
}

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

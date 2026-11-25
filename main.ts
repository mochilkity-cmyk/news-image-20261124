// news-image-20261124 — one image summing up Tuesday 24 November 2026.
// The entry is a single PNG (entry.png) drawn in this repository; this
// program only copies it to the grader's output directory, so both runs
// write the same bytes. The image itself is the entry — the program adds
// nothing to it. Node 22, standard library only. Deterministic by
// construction: a single file copy, no timestamps or randomness.
//
// Run locally:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
copyFileSync(new URL("./entry.png", import.meta.url), join(outDir, "entry.png"));

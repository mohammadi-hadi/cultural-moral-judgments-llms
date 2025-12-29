#!/bin/bash
# Build script for LNCS Springer submission
# This script compiles the LaTeX document with BibTeX bibliography

echo "=== Building LNCS Paper ==="
echo "Step 1: First pdflatex run..."
pdflatex main.tex

echo ""
echo "Step 2: Running bibtex..."
bibtex main

echo ""
echo "Step 3: Second pdflatex run (resolve references)..."
pdflatex main.tex

echo ""
echo "Step 4: Third pdflatex run (finalize)..."
pdflatex main.tex

echo ""
echo "=== Build Complete ==="
echo "Output file: main.pdf"
echo ""
echo "Cleaning auxiliary files..."
rm -f *.aux *.bbl *.blg *.log *.out *.toc

echo "Done!"